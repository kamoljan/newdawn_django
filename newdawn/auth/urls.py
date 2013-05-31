#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
	(r'^$', auth_index),
	(r'^login/$', auth_index),
	(r'^logged/$', auth_logged),
	(r'^logout/$', auth_logout),
	(r'^error/$', auth_error),
)

# urlpatterns = patterns("",
# 	url(
# 		regex=r'^logged/$',
# 		view=auth_logged,
# 	),
# )