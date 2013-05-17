from django.conf.urls import patterns, url
from .views import AdFormView

urlpatterns = patterns("",
	url(
		regex=r'^new/$',
		view=AdFormView.as_view(),
		name="new"
	),
)