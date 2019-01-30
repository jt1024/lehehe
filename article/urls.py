from django.urls import path
from . import views

app_name = 'article'  # 一定要写这一行，否则html中会报错 'article' is not a registered namespace

urlpatterns = [
    path('article-column/', views.article_column, name="article_column"),
]
