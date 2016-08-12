from django.conf.urls import patterns, include, url
from django.contrib import admin
from venture.views import login,index,logout,register
from django.conf import settings  
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'venture.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/register/$', register),
)
if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )