from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # Uncomment the next line to enable the admin:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^auth/', include('auth.urls', namespace='auth')),
    url(r'^ad/', include('ad.urls', namespace='ad')),
    url(r'^search$', include('search.urls', namespace='search')),
    url(r'^rest$', include('rest.urls', namespace='rest')),
    url(r'^social/', include('social_auth.urls')),
)
