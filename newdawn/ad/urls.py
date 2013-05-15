from django.conf.urls import patterns, url
from .views import AdCreateView, AdUpdateView, AdDetailView, AdFormView

urlpatterns = patterns("",
	url(
		regex=r'^new/$',
		view=AdFormView.as_view(),
		name="new"
	),
	url(
		regex=r'^create/$',
		view=AdCreateView.as_view(),
		name="create"
	),
	url(
		regex=r'^update/(?P<pk>\d+)/$',
		view=AdUpdateView.as_view(),
		name="update"
	),
	url(
		regex=r'^detail/(?P<pk>\d+)/$',
		view=AdDetailView.as_view(),
		name="detail"
	)
)