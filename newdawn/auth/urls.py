#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import *

#urlpatterns = patterns('',
#	(r'^$', auth_index),
#	(r'^login/$', auth_index),
#	(r'^logged/$', auth_logged),
#	(r'^logout/$', auth_logout),
#	(r'^error/$', auth_error),
#)

urlpatterns = patterns(
    "",
    url(regex=r'^logged/$', view=auth_logged, name="logged",),
    url(regex=r'^logout/$', view=auth_logout, name="logout",),
    url(regex=r'^error/$', view=auth_error, name="error",),
    url(regex=r'^login/$', view=auth_index, name="login",),
)
