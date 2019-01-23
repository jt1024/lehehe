from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_list, name='blog_list'),
    url(r'(?P<article_id>\d)/$', views.blog_detail, name='blog_detail'),
]
