#!/usr/local/bin/python
# coding: utf-8

from api.Error import raise_error, ErrorLevel

import os
import importlib
import importlib.util


def load_for_dir(path: str, output_class: classmethod, required_vars: list = None, optional_vars: list = None, required_funcs: list = None, optional_funcs: list = None, requirement_check: bool = None) -> dict:

	if required_vars is None:
		required_vars = []
	if optional_vars is None:
		optional_vars = []
	if required_funcs is None:
		required_funcs = []
	if optional_funcs is None:
		optional_funcs = []
	if requirement_check is None:
		requirement_check = 'requirements' in required_vars or 'requirements' in optional_vars

	try:
		files = os.listdir(path)
	except FileNotFoundError as error:
		raise_error(error, ErrorLevel.critical)
	else:
		modules = {}
		for file in files:
			os.path.abspath(file)
			divided = file.split('.')
			file_name = str(divided[0])
			file = os.path.join(path, file)

			if not os.path.isfile(file) or (file_name.startswith('__') and file_name.endswith('__')):
				continue

			if len(divided) != 2 or divided[1] != 'py':
				raise_error(file_name + ' is not a python file.', ErrorLevel.high)
				continue

			spec = importlib.util.spec_from_file_location(file_name, os.path.relpath(file))
			file_module = importlib.util.module_from_spec(spec)

			try:
				spec.loader.exec_module(file_module)
			except Exception as e:
				raise_error(e, ErrorLevel.high)
				continue

			module = output_class()

			if hasattr(file_module, 'disable') and file_module.disable:
				continue

			content_state = True
			for required_var in required_vars:
				if hasattr(file_module, required_var) and not callable(getattr(file_module, required_var)):
					setattr(module, required_var, getattr(file_module, required_var))
				else:
					raise_error('\'' + required_var + '\' variable is not present in ' + file_name + ' module.', ErrorLevel.high)
					content_state = False
					break

			for optional_var in optional_vars:
				if hasattr(file_module, optional_var) and not callable(getattr(file_module, optional_var)):
					setattr(module, optional_var, getattr(file_module, optional_var))

			for required_func in required_funcs:
				if hasattr(file_module, required_func) and callable(getattr(file_module, required_func)):
					setattr(module, required_func, getattr(file_module, required_func))
				else:
					raise_error('\'' + required_func + '\' function is not present in ' + file_name + ' module.', ErrorLevel.high)
					content_state = False
					break

			for optional_func in optional_funcs:
				if hasattr(file_module, optional_func) and callable(getattr(file_module, optional_func)):
					setattr(module, optional_func, getattr(file_module, optional_func))

			if not content_state:
				continue

			if not hasattr(module, 'name'):
				module.name = file_name

			if requirement_check:
				requirement_state = True
				for requirement in module.requirements:
					if importlib.find_loader(requirement) is None:
						raise_error(
							'requirement \'' + requirement + '\' is not present in module ' + file_name + '.',
							ErrorLevel.high
						)
						requirement_state = False
						break

				if not requirement_state:
					continue

			modules[module.name] = module

		return modules
