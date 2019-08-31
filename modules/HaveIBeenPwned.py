#!/usr/local/bin/python
# coding: utf-8

name = 'HaveIBeenPwned'
version = '1.0.0'
author = 'Bhasher'
requirements = ['selenium', 'time']
cache = {}


def run(args: dict = None) -> None or bool:
	from Interface import custom_input
	import Data

	from selenium.webdriver.common.keys import Keys
	import time

	if args is None:
		args = []

	email = custom_input() if 'email' not in args.keys() else args['email']
	print_arg = 'print' in args.keys() and args['print']

	Data.driver.get('https://haveibeenpwned.com/')

	Data.driver.find_element_by_id('Account').send_keys(email, Keys.ENTER)

	for i in range(5):
		if 'in' in Data.driver.find_element_by_id('pwnedWebsiteBanner').get_attribute('class'):
			break
		else:
			time.sleep(1)

	time.sleep(2)

	pwned_list = []

	for div in Data.driver.find_element_by_id('pwnedSites').find_elements_by_class_name('pwnedWebsite'):
		name = div.find_element_by_class_name('pwnedCompanyTitle').get_attribute('innerText')
		text = div.find_element_by_class_name('pwnedCompanyTitle').find_element_by_xpath('..').get_attribute('innerText')
		compromised_data = div.find_element_by_class_name('dataClasses').get_attribute('innerText').split(': ')[1].split(', ')
		pwned_list.append([name, text, compromised_data])
		if print_arg:
			print(text, compromised_data)

	cache[email] = pwned_list
