from django.urls import path
from . import views

app_name = 'account'  # 一定要写这一行，否则html中会报错 'account' is not a registered namespace

urlpatterns = [
    path(r'login/', views.user_login, name='user_login'),
]
