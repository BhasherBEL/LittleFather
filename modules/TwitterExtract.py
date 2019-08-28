#!/usr/local/bin/python
# coding: utf-8

name = 'TwitterExtract'
version = '1.0.0'
author = 'Bhasher'
requirements = ['re', 'time', 'datetime']
cache = {}


def on_load() -> None or bool:
	pass


def on_unload() -> None or bool:
	pass


def run(args: dict = None) -> None or bool:
	if args is None:
		args = {}

	import Data
	from Interface import custom_input

	import re
	import time

	url = custom_input() if 'search' not in args else args['search']

	if not re.match(r'^(https?://)?(www\.[a-z]{2-3})?twitter\.[a-z]{2,3}/[a-z_0-9]+\??([a-zA-Z]+=[a-zA-Z0-9]+&?)*$', url):
		print('l\'url n\'est pas une url de compte twitter')
		return

	Data.driver.get(url)

	content = {}

	def add_content(title: str, class_name: str, attribute: str = 'innerText'):
		value = Data.driver.find_element_by_class_name(class_name).get_attribute(attribute).lstrip().rstrip()
		if value:
			content[title] = value

	bg = Data.driver.find_element_by_class_name('ProfileCanopy-headerBg').find_element_by_tag_name('img').get_attribute('src')
	if bg:
		content['bg'] = bg

	add_content('avatar', 'ProfileAvatar-image', 'src')

	card = Data.driver.find_element_by_class_name('ProfileHeaderCard')

	if card:
		add_content('name', 'ProfileHeaderCard-name')
		add_content('pseudo', 'ProfileHeaderCard-screenname')
		add_content('bio', 'ProfileHeaderCard-bio')
		add_content('localisation', 'ProfileHeaderCard-location')
		add_content('site', 'ProfileHeaderCard-url')
		add_content('join_date', 'ProfileHeaderCard-joinDateText', 'title')
		add_content('birthdate', 'ProfileHeaderCard-birthdate')

	if 'join_date' in content.keys():
		content['join_date'] = title_date_to_timestamp(content['join_date'])

	if 'pseudo' in content.keys() and content['pseudo'][0] == '@':
		content['pseudo'] = content['pseudo'][1:]

	nav = Data.driver.find_element_by_class_name('ProfileNav-list')

	def add_nav_content(title: str, el_name: str):
		value = (
			Data.driver
			.find_element_by_class_name('ProfileNav-item--' + el_name)
			.find_element_by_class_name('ProfileNav-value')
			.get_attribute('data-count')
		)

		if value:
			try:
				value = int(value)
			except ValueError:
				pass

			content[title] = value

	if nav:
		add_nav_content('tweets', 'tweets')
		add_nav_content('following', 'following')
		add_nav_content('followers', 'followers')
		add_nav_content('likes', 'favorites')

	if 'tweets' in content.keys() and 'join_date' in content.keys():
		content['mean_tweets_per_month'] = int(content['tweets']/((time.time()-content['join_date'])/2628000))

	cache_name = content['pseudo'] if 'pseudo' in content.keys() else url

	cache[cache_name] = content


def title_date_to_timestamp(strdate: str):
	import time
	import datetime

	try:
		return int(datetime.datetime(*time.strptime(strdate, '%H:%M - %d %b %Y')[:6]).timestamp())
	except:
		return None
