#!/usr/local/bin/python
# coding: utf-8

from enum import Enum
import sys


class ErrorLevel(Enum):
	low = 0
	normal = 1
	high = 2
	critical = 3


def raise_error(error: Exception or str, level: ErrorLevel = ErrorLevel.normal):
	if isinstance(error, Exception):
		print(type(error).__name__, '(' + level.name + '):', error)
	else:
		print(level.name + ' error:', error)

	if level == ErrorLevel.critical:
		sys.exit(1)
