#!/usr/local/bin/python
# coding: utf-8

name = 'GoogleSearch'
version = '1.0.0'
author = 'Bhasher'
requirements = []
cache = {
	'searches': {}
}


def on_load() -> None or bool:
	pass


def on_unload() -> None or bool:
	pass


def run(args: dict = None) -> None or bool:
	if args is None:
		args = {}

	from api.Navigator import search
	import Data
	from Interface import custom_input

	value = custom_input() if 'search' not in args else args['search']
	i = 20 if 'i' not in args else args['i']

	cache['searches'][value] = search(Data.driver, value, i)

	if 'display' not in args or args['display']:
		print(cache['searches'][value])
