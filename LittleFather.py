#!/usr/local/bin/python
# coding: utf-8

import Mods
import Coms
import Interface
from api import Navigator
import Data

import locale
from sys import platform


def check_locale():
	try:
		locale.setlocale(locale.LC_TIME, 'fr_FR.utf8')
	except locale.Error:
		print('/!\\ Veuillez installer la langue française sur votre ordinateur. /!\\')
		if platform == "win32":
			print('Tutoriel: https://www.thewindowsclub.com/install-uninstall-languages-windows-10')
		else:
			print('Commande unix: \'sudo apt-get install language-pack-fr\'')
			print('Tapez \'locale -a | grep fr_FR.utf8\' pour verifier l\'installation')
		exit(1)


def main():
	check_locale()
	with Navigator.init_driver() as Data.driver:
		Mods.load_modules()
		Coms.load_commands()

		Interface.run()

		Mods.unload_modules()


if __name__ == '__main__':
	main()
