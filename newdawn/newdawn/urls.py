from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from search.views import ad_search

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),

    # Examples:
    # url(r'^$', 'newdawn.views.home', name='home'),
    # url(r'^newdawn/', include('newdawn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ad/', include('ad.urls', namespace='ad')),
    #url(r'^search/$', TemplateView.as_view(template_name='search/search_form.html'), name='search'),
    url(r'^search$', include('search.urls', namespace='search')),
)
