from django.conf.urls import patterns, url
from .views import ad_search

urlpatterns = patterns("",
	url(
		regex=r'^ad_search$',
		view=ad_search,
		name="search"
	),
)