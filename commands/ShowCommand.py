#!/usr/local/bin/python
# coding: utf-8

from Data import target_data

from terminaltables import AsciiTable


name = 'show'
version = '1.0.0'
author = 'Bhasher'
dependencies = []


def execute(args: list):
	if len(args) == 0:
		data = [['Name', 'Value']]
		for key, value in target_data.items():
			if isinstance(value, list):
				data.append([key, ', '.join(value)])
			else:
				data.append([key, value])
		print(AsciiTable(data).table)
	elif len(args) == 1 and args[0] in target_data:
		print(AsciiTable([['Name', 'Value'], [args[0], ', '.join(target_data[args[0]])]]).table)
	else:
		usage()


def usage():
	print('Usage: show [data_type]')
