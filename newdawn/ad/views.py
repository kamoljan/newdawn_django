from django.contrib import messages
from django.views.generic import (CreateView, UpdateView, DetailView)
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from braces.views import LoginRequiredMixin
from .models import Ad
from .forms import AdForm


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
		form = AdForm(self.request.POST)
		ad = form.save(commit=False)
		ad.image_fid = 'image_fid.lah'
		ad.thumb_fid = 'thumb_fid.lah'
		ad.ad_status = 1
		ad.user_ip = self.request.META['REMOTE_ADDR']
		ad.latitude = 2
		ad.longitude = 3
		ad.secret_token = 'secretlah'
		ad.save()
		return HttpResponseRedirect('/')  # Redirect after POST
		#return super(AdFormView, self).form_valid(form)

	def get(self, request):
		return self.render_to_response({'form': AdForm()})


class AdCreateView(LoginRequiredMixin, AdActionMixin, CreateView):
	form_class = AdForm
	model = Ad
	action = "created"
	fields = ['']
	#AdFormSet = modelformset_factory(Ad)


class AdUpdateView(LoginRequiredMixin, AdActionMixin, UpdateView):
	form_class = AdForm
	model = Ad
	action = "updated"


class AdDetailView(DetailView):
	model = Ad