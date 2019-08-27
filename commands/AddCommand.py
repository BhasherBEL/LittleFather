#!/usr/local/bin/python
# coding: utf-8

from Data import target_data


name = 'add'
version = '1.0.0'
author = 'Bhasher'
dependencies = []


def execute(args: list) -> None:
	if len(args) >= 2 and args[0] in target_data:
		target_data[args[0]] += args[1:]
	else:
		usage()


def usage() -> None:
	print('Usage: add <data_type> <data_value 1> [data_value 2] ...')
