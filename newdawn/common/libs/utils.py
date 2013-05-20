#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from django.conf import settings
import random
import hashlib
import time


# TODO: use it in AI
def generate_secret_token():
	max_range_number = 18446744073709551616L
	raw = str(random.randrange(0, max_range_number)) + settings.SECRET_KEY + str(time.time())
	return hashlib.sha256(raw).hexdigest()


def cint(value):
	try:
		return int(value)
	except:
		return None