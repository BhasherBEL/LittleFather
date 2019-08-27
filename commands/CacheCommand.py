#!/usr/local/bin/python
# coding: utf-8

from Mods import modules


name = 'cache'
version = '1.0.0'
author = 'Bhasher'
dependencies = []


def execute(args: list) -> None:
	if len(args) == 1 or len(args) == 2 and args[0] in modules.keys():
		if len(args) == 2 and args[1] == 'clear':
				modules[args[0]].cache = modules[args[0]].__cache
		modules[args[0]].print_cache()
	else:
		usage()


def usage() -> None:
	print('Usage: cache <' + ', '.join(modules.keys()) + '> [clear]')


