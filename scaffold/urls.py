from django.conf.urls import patterns, include, url

import session_csrf
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

from potato_blog_ric import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^_ah/', include('djangae.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addblog/', views.createblog),
    url(r'^update-article/$', views.update_article),
    url(r'^delete-article/(?P<article_id>\w+)/$', views.delete_article),
    url(r'^upload-image/$', views.upload_image, name = 'upload'),
    url(r'^delete-image/(?P<article_id>\w+)/images/(?P<image_id>\w+)/$', views.delete_image),
    url(r'^logout/', views.logout_view),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

urlpatterns += staticfiles_urlpatterns()