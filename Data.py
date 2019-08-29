#!/usr/local/bin/python
# coding: utf-8

from selenium import webdriver

driver: webdriver.Firefox = None

target_data = {
	'first_names': [],
	'last_names': [],
	'pseudos': [],
	'phone_numbers': [],
	'addresses': [],
	'emails': [],
	'autocomplete': True,
}
