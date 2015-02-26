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
    url(r'^blog/', include('potato_blog_ric.urls'))
)
