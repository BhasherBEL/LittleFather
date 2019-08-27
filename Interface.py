#!/usr/local/bin/python
# coding: utf-8

import Coms

import sys


path = ['~']


def run() -> None:
	while True:
		input_value = input('LittleFather(' + '/'.join(path) + ') $ ').split(' ')
		if len(input_value) == 0:
			continue

		if not interpret(input_value):
			break


def custom_input():
	return input()


def interpret(args: list) -> bool:
	command = args[0]
	args = [] if len(args) == 1 else args[1:]

	if command in Coms.commands:
		Coms.commands[command].execute(args)
	elif command == 'exit':
		return False
	else:
		print('unknown command')

	return True
