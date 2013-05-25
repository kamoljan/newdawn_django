from django.conf.urls import patterns, url
from .views import AdFormView, AdView

urlpatterns = patterns("",
	url(
		regex=r'^new/$',
		view=AdFormView.as_view(),
		name="new"
	),
	url(
		regex=r'^view/(?P<pk>\d+)$',
		view=AdView.as_view(),
		name="view"
	),
)