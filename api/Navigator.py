#!/usr/local/bin/python
# coding: utf-8

from LittleFather import __file__ as lf_file

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

DELAY = 5


def init_driver() -> webdriver.Firefox:
	driver = webdriver.Firefox(executable_path=os.path.join(os.path.dirname(os.path.abspath(lf_file)), 'geckodriver'))
	driver.wait = WebDriverWait(driver, DELAY)
	return driver


def search(driver: webdriver.Firefox, query: str, n: int = 20, lang='fr') -> list:
	driver.get('http://www.google.com?hl=' + lang + '&lr=lang_' + lang + '&num=' + str(n))

	output = []

	try:
		box = driver.find_element_by_name('q')
		button = driver.find_element_by_name('btnK')
		box.send_keys(query)
		box.send_keys(Keys.RETURN)
		button.click()
	except TimeoutException:
		print("Box or Button not found in google.com")
	except ElementNotInteractableException:
		print('Interact box error')

	try:
		WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.CLASS_NAME, 'r')))
		for el in driver.find_elements_by_class_name('r'):
			output.append(el.find_element_by_tag_name('a').get_attribute('href'))
	except TimeoutException:
		print('No results found.')

	return output
