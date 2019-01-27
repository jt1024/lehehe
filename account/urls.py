from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'  # 一定要写这一行，否则html中会报错 'account' is not a registered namespace

urlpatterns = [
    # path(r'login/', views.user_login, name='user_login'),
    path(r'login/', auth_views.LoginView.as_view(template_name="account/login.html"), name='user_login'),  # 使用Django内置的登录方法
    path(r'logout/', auth_views.LogoutView.as_view(template_name="account/logout.html"), name='user_logout'),  # 使用Django内置的登出方法
    path(r'register/', views.user_register, name='user_register'),
]
