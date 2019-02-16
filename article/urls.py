from django.urls import path, re_path
from . import views

app_name = 'article'  # 一定要写这一行，否则html中会报错 'article' is not a registered namespace

urlpatterns = [
    path('article-column/', views.article_column, name="article_column"),
    path('rename-article-column/', views.rename_article_column, name="rename_article_column"),
    path('del-article-column/', views.del_article_column, name="del_article_column"),
    path('article-post/', views.article_post, name="article_post"),
    path('article-list/', views.article_list, name="article_list"),
    re_path('article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.article_detail, name="article_detail"),
]
