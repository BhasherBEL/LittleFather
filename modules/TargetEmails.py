#!/usr/local/bin/python
# coding: utf-8

import Mods
from Data import target_data
import itertools

name = 'TargetEmails'
version = '1.0.0'
author = 'Bhasher'
requirements = ['time', 'selenium', 're']
cache = {}


def on_load() -> None or bool:
	pass


def on_unload() -> None or bool:
	pass


def run(args: dict = None) -> None or bool:
	from Interface import custom_input
	import Data
	from api import Regex, List, String

	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.common.by import By
	from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
	import time
	import re

	links = []
	search = custom_input() if 'search' not in args.keys() else args['search']
	num = 20 if 'num' not in args.keys() else args['num']

	if 'GoogleSearch' in Mods.modules.keys():
		Mods.modules['GoogleSearch'].run(
			{
				'search': search,
				'i': num,
				'display': False,
			}
		)

		for link in Mods.modules['GoogleSearch'].cache['searches'][search]:
			if link not in links:
				links.append(link)
	else:
		absent_module('GoogleSearch')

	emails = []
	candidates = ['emails', 'first_names', 'last_names', 'pseudos']

	for link in links:
		Data.driver.execute_script('window.location.href=\'' + link + '\'')
		time.sleep(1)
		try:
			Data.driver.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
		except TimeoutException:
			continue

		try:
			emails += re.findall(Regex.email, Data.driver.find_element_by_tag_name('body').get_attribute('innerHTML'))
		except StaleElementReferenceException:
			continue

	emails = list(set(emails))

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

	emails_info = reversed(List.sort_by_subtab(emails_info, 0))

	cache[search] = emails_info

	if 'print' in args.keys() and args['print']:
		print('Emails')
		for email in emails_info:
			print('  -', email)


def absent_module(name: str) -> None:
	print('Le module', name, 'est absent. Veuillez l\'ajouter pour un meilleur fonctionnement du module TargetLinks.')


def print_cache() -> None:
	print(len(cache['links']), 'liens en cache:', cache)
