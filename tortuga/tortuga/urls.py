import os
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  
from django.views.generic.simple import direct_to_template
from sdk.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tortuga.views.home', name='home'),
    (r'^$',direct_to_template, {'template': 'index.html'}),
    (r'^models/$',modelsView),
    (r'^model/(\d+)/$',modelView),
    (r'^model/(\d+)/(\d+\.\d+)/$',versionView),
    (r'^submodel/$',direct_to_template, {'template': 'submodel.html'}),
    (r'^delete/(\d+)/$',deleteView),
    (r'^delete/(\d+)/(\d+\.\d+)/$',deleteView),

    (r'^srls/$',srlsView),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

rulespath=os.path.join(settings.MEDIA_ROOT,'rules').replace('\\','/')
ifcpath=os.path.join(settings.MEDIA_ROOT,'files').replace('\\','/')

urlpatterns += staticfiles_urlpatterns()  
urlpatterns += patterns('',
        url(r'^rules/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': rulespath
        }))
urlpatterns += patterns('',
        url(r'^files/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': ifcpath, 'show_indexes':True,
        }))
