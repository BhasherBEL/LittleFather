#!/usr/local/bin/python
# coding: utf-8

import Mods
from Data import target_data
import itertools

name = 'TargetLinks'
version = '1.0.0'
author = 'Bhasher'
requirements = []
cache = {'links': []}


def on_load() -> None or bool:
	pass


def on_unload() -> None or bool:
	pass


def run(args: dict = None) -> None or bool:
	datas = [value for lov in target_data.values() if isinstance(lov, list) for value in lov if value and isinstance(value, str)]
	links = []
	combinations = []
	for i in range(1, len(datas)+1):
		combinations += list(itertools.combinations(datas, i))
	combinations = [' '.join(combination) for combination in combinations]
	print('Lancement de', len(combinations), 'recherches.')
	try:
		if 'GoogleSearch' in Mods.modules.keys():
			for data in combinations:
				print('GoogleSearch', data, '...')

				Mods.modules['GoogleSearch'].run(
					{
						'search': data,
						'i': 100,
						'display': False,
					}
				)

				for link in Mods.modules['GoogleSearch'].cache['searches'][data]:
					if link not in links:
						links.append(link)
		else:
			absent_module('GoogleSearch')
	except KeyboardInterrupt:
		pass
	cache['links'] = list(reversed(links))


def absent_module(name: str) -> None:
	print('Le module', name, 'est absent. Veuillez l\'ajouter pour un meilleur fonctionnement du module TargetLinks.')


def print_cache() -> None:
	print(len(cache['links']), 'liens en cache:', cache)
