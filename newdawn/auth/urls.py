#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from auth.views import *

urlpatterns = patterns('',
    (r'^$', auth_index),
    (r'^login/$', auth_index),
    (r'^logged/$', auth_logged),
    (r'^logout/$', auth_logout),
    (r'^error/$', auth_error),
)