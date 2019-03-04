from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'image'  # 一定要写这一行，否则html中会报错 'image' is not a registered namespace

urlpatterns = [
    path('list-images/', views.list_images, name="list_images"),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('del-image/', views.del_image, name='del_image'),
    path('images/', views.falls_images, name="falls_images"),
]
