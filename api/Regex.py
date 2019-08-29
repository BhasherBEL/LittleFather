#!/usr/local/bin/python
# coding: utf-8

import re


email = re.compile(r'([a-zA-Z0-9_\-+\.]+@(?:[a-zA-Z0-9\-_+]+\.)+(?:[a-zA-Z]{2,3}&^(?:png)))')
