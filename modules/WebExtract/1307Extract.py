#!/usr/local/bin/python
# coding: utf-8

name = '1307Extract'
version = '1.0.0'
author = 'Bhasher'

success_class = 'fn'
regex = r'^(https?://)?(www\.)?1(3|2)07\.be'
content = {}

captcha_msg = 'Pardon Our Interruption...'


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
	add_content('name', 'fn')
	add_content('address', 'adr')
	add_content('phone_number', 'tel')

	return content
