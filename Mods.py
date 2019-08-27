#!/usr/local/bin/python
# coding: utf-8

from api import DirLoad

import os


modules = {}


class Module(object):
	name = ''
	version = ''
	author = ''
	requirements = []
	cache = {}
	__cache = cache

	def on_load(self) -> None or bool:
		pass

	def on_unload(self) -> None or bool:
		pass

	def run(self) -> None or bool:
		pass

	def print_cache(self) -> None:
		print(self.cache)


def load_modules(path: str = None) -> None:

	global modules

	if modules:
		unload_modules()

	if path is None or path == '':
		path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'modules')

	modules = DirLoad.load_for_dir(
		path=path,
		output_class=Module,
		required_vars=['name', 'version'],
		optional_vars=['author', 'requirements', 'cache'],
		required_funcs=['run'],
		optional_funcs=['on_load', 'on_unload', 'print_cache']
	)

	for module in modules.values():
		module.__cache = module.cache
		module.on_load()

	print(len(modules), 'modules loaded.')


def unload_modules() -> None:
	for module in modules.values():
		module.on_unload()

