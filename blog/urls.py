from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.blog_list, name='blog_list'),
    path(r'<int:article_id>/', views.blog_detail, name='blog_detail'),
]
