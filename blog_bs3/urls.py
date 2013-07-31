from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'post.views.home', name='home'),
    url(r'^sign_in', 'post.views.sign_up', name='sign_up'),
    url(r'^log_out', 'post.views.log_out', name='log_out'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
