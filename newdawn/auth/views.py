from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.messages.api import get_messages

from social_auth import __version__ as version
from social_auth.utils import setting


def auth_index(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return auth_logged(request)
    else:
        return render_to_response('auth/auth_login.html', {'version': version}, RequestContext(request))


def auth_logged(request):
    names = request.user.social_auth.values_list('provider', flat=True)
    context = dict((name.lower().replace('-', '_'), True) for name in names)
    context['version'] = version
    context['last_login'] = request.session.get('social_auth_last_login_backend')
    return render_to_response('auth/auth_login.html', context, RequestContext(request))


def auth_error(request):
    error_msg = get_messages(request)
    return render_to_response('auth/auth_error.html', {'version': version, 'error_msg': error_msg},
                              RequestContext(request))


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def form(request):
    if request.method == 'POST' and request.POST.get('username'):
        name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
        request.session['saved_username'] = request.POST['username']
        backend = request.session[name]['backend']
        return redirect('socialauth_complete', backend=backend)
    return render_to_response('auth/auth_form.html', {}, RequestContext(request))


def form2(request):
    if request.method == 'POST' and request.POST.get('first_name'):
        request.session['saved_first_name'] = request.POST['first_name']
        name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
        backend = request.session[name]['backend']
        return redirect('socialauth_complete', backend=backend)
    return render_to_response('auth/auth_form2.html', {}, RequestContext(request))


def close_login_popup(request):
    return render_to_response('close_popup.html', {}, RequestContext(request))