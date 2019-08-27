#!/usr/local/bin/python
# coding: utf-8

from api import DirLoad

import os


commands = {}


class Command(object):
	name = ''
	version = ''
	author = ''
	requirements = []

	def execute(self):
		pass

	def usage(self):
		pass


def load_commands(path: str = None) -> None:
	global commands

	if path is None or path == '':
		path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'commands')

	commands = DirLoad.load_for_dir(
		path=path,
		output_class=Command,
		required_vars=['name', 'version'],
		optional_vars=['author', 'requirements'],
		required_funcs=['execute'],
		optional_funcs=['usage']
	)

	print(len(commands), 'commands loaded.')
