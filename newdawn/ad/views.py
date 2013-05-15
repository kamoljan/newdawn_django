from django.contrib import messages
from django.views.generic import (CreateView, UpdateView, DetailView)
from django.views.generic.edit import FormView
from django.template import RequestContext
from django.forms.models import modelformset_factory

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

	def form_invalid(self, form):
		# Dome something
		print(self.request.POST)
		return super(AdFormView, self).form_invalid(form)

	def form_valid(self, form):
		print(self.request.POST)
		return super(AdFormView, self).form_valid(form)

	def get(self, request):
		return self.render_to_response({'form': AdForm()})


class AdCreateView(LoginRequiredMixin, AdActionMixin, CreateView):
	form_class = AdForm
	model = Ad
	action = "created"
	fields = ['']
	#AdFormSet = modelformset_factory(Ad)

	def form_invalid(self, form):
		# Dome something
		return super(AdCreateView, self).form_valid(form)

	def post(self, request):
		self.object = None
		return super(AdCreateView, self).post(request)

	def get(self, request):
		self.object = None
		return super(AdCreateView, self).get

	# def action(self):
	# 	return render(request, 'polls/detail.html', {'poll': p, 'error_message': "You didn't select a choice."})


class AdUpdateView(LoginRequiredMixin, AdActionMixin, UpdateView):
	form_class = AdForm
	model = Ad
	action = "updated"


class AdDetailView(DetailView):
	model = Ad