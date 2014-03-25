from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangositeabc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('djangositeabc.apps.catalogo.urls')),
    url(r'^',include('djangositeabc.apps.tableservice.urls')),

)
