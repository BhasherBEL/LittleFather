#!/usr/local/bin/python
# coding: utf-8

from Mods import modules
from api import Error


name = 'launch'
version = '1.0.0'
author = 'Bhasher'
dependencies = ['re']


def execute(args: list) -> None:
	import re

	if len(args) >= 1 and args[0] in modules.keys():
		margs = {}
		pm = ' '.join(args[1:])
		for __ in pm:
			m = re.match(r'[a-zA-Z0-9]+=(\'.*\'|".*"|[^ ]+)', pm)
			if m is None:
				break
			pm = pm[0: m.start()] + pm[m.end() + 1:]
			splitted = m.group(0).split('=')
			if len(splitted) >= 2:
				margs[splitted[0]] = parse('='.join(splitted[1:]))
		modules[args[0]].run(margs)
	else:
		usage()


def usage() -> None:
	print('Usage: launch <' + ', '.join(modules.keys()) + '>')


def parse(string: str) -> str or int or float or bool:
	try:
		if string.isdigit() or (string.startswith('-') and string[1:].isdigit()):
			return int(string)
		elif string.lower() == 'true':
			return True
		elif string.lower() == 'false':
			return False
		elif string.replace('.', '', 1).replace('-', '').isdigit():
			return float(string)
		return string
	except ValueError as e:
		Error.raise_error(e, Error.ErrorLevel.high)


