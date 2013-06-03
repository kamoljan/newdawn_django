#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import messages
# from django.views.generic.edit import FormView, CreateView
from django.views.generic import DetailView, FormView
from django.http import HttpResponseRedirect

from braces.views import LoginRequiredMixin
from .forms import AdForm
from .models import Ad
from common.libs.sushiapi import save_image_to_sushi_with_string
from common.libs.utils import generate_secret_token


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
		#return super(AdFormView, self).form_valid(form)

	def get(self, request):
		return self.render_to_response({'form': AdForm()})


#class AdView(LoginRequiredMixin, AdActionMixin, DetailView):
class AdView(AdActionMixin, DetailView):
	model = Ad

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(AdView, self).get_context_data(**kwargs)
		# Add in a QuerySet of settings param
		context['SUSHI_PUBLIC_URL'] = settings.SUSHI_PUBLIC_URL
		return context
