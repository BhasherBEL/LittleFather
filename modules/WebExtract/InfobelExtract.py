#!/usr/local/bin/python
# coding: utf-8

name = 'InfobelExtract'
version = '1.0.0'
author = 'Bhasher'

success_class = 'customer-item-name'
regex = r'^(https?://)?(www\.)?(local.)?infobel\.[a-zA-Z]{2,3}'
content = {}

# captcha_msg = 'customer-item-name'


def add_content(title: str, class_name: str, attribute: str = 'innerText') -> None:
	import Data
	from selenium.common.exceptions import NoSuchElementException

	try:
		value = Data.driver.find_element_by_class_name(class_name).get_attribute(attribute).lstrip().rstrip()
		if value:
			content[title] = value
	except NoSuchElementException:
		pass


def extract() -> dict:
	import Data

	add_content('name', 'customer-item-name')
	add_content('address', 'address')

	for div in Data.driver.find_elements_by_tag_name('div'):
		if 'phones' in div.get_attribute('id'):
			content['phone_number'] = div.get_attribute('innerText')
			break

	for a in Data.driver.find_elements_by_tag_name('a'):
		if 'source-email' in a.get_attribute('id'):
			content['email'] = a.get_attribute('innerText')
			break

	content['labels'] = [label.get_attribute('innerText') for label in Data.driver.find_elements_by_class_name('customer-item-label')]

	return content
