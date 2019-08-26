#!/usr/local/bin/python
# coding: utf-8

from Coms import commands


name = 'usage'
version = '1.0.0'
author = 'Bhasher'
dependencies = []


def execute(args: list) -> None:
	if len(args) == 1 and args[0] in commands.keys():
		commands[args[0]].usage()
	else:
		usage()


def usage() -> None:
	print('Usage: usage <' + ', '.join(commands.keys()) + '>')


