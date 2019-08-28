#!/usr/local/bin/python
# coding: utf-8

name = '1307Extract'
version = '1.0.0'
author = 'Bhasher'

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


def extract(url: str) -> dict:
	import Data
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.common.by import By
	from selenium.common.exceptions import TimeoutException

	Data.driver.get(url)

	try:
		Data.driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'fn')))
	except TimeoutException:
		if captcha_msg in Data.driver.find_element_by_tag_name('body').get_attribute('innerText'):
			input('Veuillez remplir le captcha, puis appuyer sur enter.')
		else:
			print('No results found.')

	add_content('name', 'fn')
	add_content('address', 'adr')
	add_content('phone_number', 'tel')

	return content
