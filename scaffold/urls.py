from django.conf.urls import patterns, include, url

import session_csrf
session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

from potato_blog_ric import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^_ah/', include('djangae.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^addblog/', views.createblog),
    url(r'^update-article/$', views.update_article),
    url(r'^delete-article/(?P<article_id>\w+)/$', views.delete_article),
    url(r'^upload-image/$', views.upload_image, name = 'upload'),
    url(r'^delete-image/(?P<article_id>\w+)/images/(?P<image_id>\w+)/$', views.delete_image),
    url(r'^logout/', views.logout_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
