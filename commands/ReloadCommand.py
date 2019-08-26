#!/usr/local/bin/python
# coding: utf-8

import Coms
import Mods


name = 'reload'
version = '1.0.0'
author = 'Bhasher'
dependencies = []


def execute(args: list):
	if len(args) == 0:
		Coms.load_commands()
		Mods.load_modules()
	elif len(args) == 1:
		if args[0].lower() == 'commands':
			Coms.load_commands()
		elif args[0].lower() == 'modules':
			Mods.load_modules()
	else:
		usage()


def usage():
	print('Usage: reload [commands|modules]')
