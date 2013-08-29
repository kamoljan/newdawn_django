#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from django.conf import settings
from django.contrib import messages
from django.views.generic import DetailView, FormView
from django.http import HttpResponseRedirect

from braces.views import LoginRequiredMixin

from common.libs.sushiapi import save_image_to_sushi_with_string
from common.libs.utils import generate_secret_token

from .forms import AdForm
from .models import Ad

# Get an instance of a logger
logger = logging.getLogger(__name__)


class AdActionMixin(object):
    @property
    def action(self):
        msg = "{0} is missing action."
        msg = msg.format(self.__class__)
        raise NotImplementedError(msg)

    def form_valid(self, form):
        msg = "Ad {0}!"
        msg = msg.format(self.action)
        messages.info(self.request, msg)
        return super(AdActionMixin, self).form_valid(form)


class AdFormView(LoginRequiredMixin, AdActionMixin, FormView):
    form_class = AdForm
    success_url = '/'
    template_name = 'ad/ad_form.html'
    action = "formed"

    def form_valid(self, form):
        form = AdForm(self.request.POST, self.request.FILES)
        ad = form.save(commit=False)
        ad.image_fid = save_image_to_sushi_with_string(self.request.FILES['image_fid'])
        ad.thumb_fid = ad.image_fid  # TODO: fix it later
        ad.user_ip = self.request.META['REMOTE_ADDR']
        ad.secret_token = generate_secret_token()
        ad.save()
        return HttpResponseRedirect('/')  # Redirect after POST

    def get(self, request):
        email = ''
        user_name = request.user.username
        provider_string = ''
        if user_name != '':
            email = request.user.email
            provider = request.user.social_auth.values_list('provider', flat=True)
            for name in provider:
                provider_string += name.lower().replace('-', '_')

        return self.render_to_response({'form': AdForm(initial={'user_name': user_name,
                                                                'user_email': email})})


class AdView(AdActionMixin, DetailView):
    model = Ad

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AdView, self).get_context_data(**kwargs)
        # Add in a QuerySet of settings param
        context['SUSHI_PUBLIC_URL'] = settings.SUSHI_PUBLIC_URL
        # get common ad info
        ad = kwargs.get('object', None)
        context['ads'] = Ad.objects.filter(ad_status=0, user_email=ad.user_email).exclude(id=ad.id)[0:2]

        return context
