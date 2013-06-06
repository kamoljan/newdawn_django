#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns(
    "",
    url(regex=r'^login/$', view=auth_index, name="login",),
    url(regex=r'^logged/$', view=auth_logged, name="logged",),
    url(regex=r'^logout/$', view=auth_logout, name="logout",),
    url(regex=r'^error/$', view=auth_error, name="error",),
)
