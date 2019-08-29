#!/usr/local/bin/python
# coding: utf-8


def sort_by_subtab(sub_li: list, index: int) -> list:
	# reverse = None (Sorts in Ascending order)
	# key is set to sort using second element of
	# sublist lambda has been used
	sub_li.sort(key=lambda x: x[index])
	return sub_li
