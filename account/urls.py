from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'  # 一定要写这一行，否则html中会报错 'account' is not a registered namespace

urlpatterns = [
    # path(r'login/', views.user_login, name='user_login'),
    path('login/', auth_views.LoginView.as_view(template_name="account/login.html"), name='user_login'),  # 使用Django内置的登录方法
    path('logout/', auth_views.LogoutView.as_view(template_name="account/logout.html"), name='user_logout'),  # 使用Django内置的登出方法
    path('register/', views.user_register, name='user_register'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name="account/password_change_form.html", success_url="/account/password-change-done/"), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"), name='password_change_done'),

]
