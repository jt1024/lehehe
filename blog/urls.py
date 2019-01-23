from django.urls import path
from . import views

app_name = 'blog'  # 一定要写这一行，否则html中的 href="{% url 'blog:blog_title' %}" 会报错 'blog' is not a registered namespace

urlpatterns = [
    path(r'', views.blog_list, name='blog_list'),
    path(r'<int:article_id>/', views.blog_detail, name='blog_detail'),
]
