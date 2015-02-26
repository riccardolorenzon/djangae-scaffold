from django.conf.urls import *

from models import Post
import views

urlpatterns = patterns('',
    url(r'^add_post/$', views.add_post),
    url(r'^post/(?P<slug>[-\w]+)$',
        'blog.views.view_post',
        name='blog_post_detail'),
)