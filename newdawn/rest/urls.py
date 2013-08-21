from django.conf.urls import patterns, url
from .views import rest_search

urlpatterns = patterns(
    "",
    url(regex=r'^$', view=rest_search, name="rest"),
)


