#!/usr/local/bin/python
# coding: utf-8

name = 'WebExtract'
version = '1.0.0'
author = 'Bhasher'
requirements = ['selenium', 'os', 're', 'time']
cache = {
	'websites': {},
	'outputs': {},
	'analyse': {
		'emails': []
	},
}


class Website(object):
	success_class = None
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
		required_vars=['name', 'version', 'regex', 'success_class'],
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
	import Data

	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.common.by import By
	from selenium.common.exceptions import TimeoutException

	url = custom_input() if 'search' not in args.keys() else args['search']

	if 'websites' not in cache.keys():
		print('Impossible d\'executer le module sans la liste des sites. Veuillez redémarrer le module.')
		return False

	output = None

	Data.driver.get(url)

	for content in cache['websites'].values():
		if content.is_website(url):
			try:
				Data.driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, content.success_class)))
			except TimeoutException:
				if hasattr(content, 'captcha_msg') and getattr(content, 'captcha_msg') in Data.driver.find_element_by_tag_name('body').get_attribute('innerText'):
					input('Veuillez remplir le captcha, puis appuyer sur enter.')
				else:
					print('No results found.')
			output = content.extract()

	if 'print_analyse' in args.keys():
		analyse(args['print_analyse'])
	else:
		analyse()

	if output is None:
		print('website not found for', url)
		return False

	cache['outputs'][url] = output

	if 'print' in args.keys() and args['print']:
		print(output)


def analyse(print_analyse: bool = False) -> None:
	import Data
	from api import Regex, String, List

	import re

	html = Data.driver.find_element_by_tag_name('body').get_attribute('innerHTML')

	emails = list(set(re.findall(Regex.email, html))) + ['e.thiran@profs.e-ndc.org', 'catherine.thiran@skynet.be']
	print_emails = emails

	if print_analyse:

		candidates = ['emails', 'first_names', 'last_names', 'pseudos']

		if any(Data.target_data[candidate] for candidate in candidates):

			emails_info = []

			for email in emails:

				sec_email = email.split('@')[0]

				el = None
				score = 0

				for candidate in candidates:
					for element in Data.target_data[candidate]:
						if candidate == 'emails':
							element = element.split('@')[0]
						if isinstance(element, str):
							new_score = String.levenshtein_index(element.lower(), sec_email.lower())
							if new_score > score:
								score = new_score
								el = element

				emails_info.append([round(score, 2), email, el])

			print_emails = reversed(List.sort_by_subtab(emails_info, 0))

		print('Emails')
		for email in print_emails:
			print('  -', email)

	cache['analyse']['emails'] += emails
