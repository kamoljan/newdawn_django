from django.conf.urls import patterns, url
from .views import ad_search

urlpatterns = patterns(
    "",
    url(regex=r'^$', view=ad_search, name="search"),
)
