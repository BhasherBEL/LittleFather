#!/usr/local/bin/python
# coding: utf-8

from Coms import global_data


name = 'set'
version = '1.0.0'
author = 'Bhasher'
dependencies = []


def execute(args: list) -> None:
	if len(args) >= 2 and args[0] in global_data:
		global_data[args[0]] = args[1:]
	else:
		usage()


def usage() -> None:
	print('Usage: set <data_type> <data_value 1> [data_value 2] ...')
