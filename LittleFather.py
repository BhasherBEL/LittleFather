#!/usr/local/bin/python
# coding: utf-8

import Mods
import Coms
import Interface
from api import Navigator
import Data


def main():
	with Navigator.init_driver() as Data.driver:
		Mods.load_modules()
		Coms.load_commands()

		Interface.run()

		Mods.unload_modules()


if __name__ == '__main__':
	main()
