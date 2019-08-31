#!/usr/local/bin/python
# coding: utf-8

name = 'ModuleType'                  			# Required
version = '1.0.0'                    			# Required
author = 'Bhasher'           					# Not Required
requirements = []    			    			# Not Required


def on_load() -> None or bool:       			# Not Required
	pass


def on_unload() -> None or bool:     			# Not Required
	pass


def run(args: dict = None) -> None or bool:		# Required
	if args is None:
		args = []
