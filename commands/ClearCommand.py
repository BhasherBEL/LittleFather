#!/usr/local/bin/python
# coding: utf-8

from Data import target_data


name = 'clear'
version = '1.0.0'
author = 'Bhasher'
dependencies = []


def execute(args: list):
	if len(args) == 1 and args[0] in target_data:
		target_data[args[0]] = []
	else:
		usage()


def usage():
	print('Usage: clear <data_type>')
