#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.messages.api import get_messages

from social_auth import __version__ as version


def auth_index(request):
	if request.user.is_authenticated():
		return auth_logged(request)
	else:
		return render_to_response('auth/auth_home.html', {'version': version}, RequestContext(request))


def auth_logged(request):
	names = request.user.social_auth.values_list('provider', flat=True)
	context = dict((name.lower().replace('-', '_'), True) for name in names)
	context['version'] = version
	context['last_login'] = request.session.get('social_auth_last_login_backend')
	return render_to_response('auth/auth_home.html', context, RequestContext(request))


def auth_error(request):
	error_msg = get_messages(request)
	return render_to_response('auth/auth_error.html', {'version': version, 'error_msg': error_msg}, RequestContext(request))


def auth_logout(request):
	logout(request)
	return HttpResponseRedirect('/')
