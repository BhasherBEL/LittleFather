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

		command = input_value[0]
		args = [] if len(input_value) == 1 else input_value[1:]

		if command in Coms.commands:
			Coms.commands[command].execute(args)
		elif command == 'exit':
			return
		else:
			print('unknown command')


def custom_input():
	return input()
