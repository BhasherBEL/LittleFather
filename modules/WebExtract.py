#!/usr/local/bin/python
# coding: utf-8

name = 'WebExtract'
version = '1.0.0'
author = 'Bhasher'
requirements = ['selenium', 'os', 're', 'time']
cache = {
	'websites': {},
	'outputs': {},
}


class Website(object):
	name = None
	version = None
	author = None
	content = {}
	regex = None
	captcha_msg = None

	def is_website(self, url) -> bool:
		import re

		return re.match(self.regex, url) is not None

	def extract(self, url) -> dict:
		return self.content


def on_load() -> None or bool:
	from api import DirLoad

	import os

	cache['websites'] = DirLoad.load_for_dir(
		path=os.path.join(os.path.dirname(os.path.abspath(__name__)), 'modules', 'WebExtract'),
		output_class=Website,
		required_vars=['name', 'version', 'regex'],
		optional_vars=['author', 'content', 'captcha_msg'],
		required_funcs=['extract'],
		optional_funcs=['is_website'],
	)

	print(len(cache['websites']), 'WebExtract submodules load.')


def on_unload() -> None or bool:
	pass


def run(args: dict = None) -> None or bool:
	if args is None:
		args = {}

	from Interface import custom_input

	url = custom_input() if 'search' not in args.keys() else args['search']

	if 'websites' not in cache.keys():
		print('Impossible d\'executer le module sans la liste des sites. Veuillez redémarrer le module.')
		return False

	output = None

	for content in cache['websites'].values():
		if content.is_website(url):
			output = content.extract(url)

	if output is None:
		print('website not found for', url)
		return False

	cache['outputs'][url] = output

	if 'print' in args.keys() and args['print']:
		print(output)
