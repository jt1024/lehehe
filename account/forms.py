from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# 注意：注册表单继承的是 forms.ModelForm ，区别于登录表单的 forms.Form
# 如果要将表单中的数据写入数据库表或修改某些记录的值，就让表单类继承 forms.ModelForm
# 如果提交表单之后，不会对数据库进行修改，则继承 forms.Form
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="ConfirmPassword", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("两次输入的密码不匹配")
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "address", "aboutme")


# 注意：UserForm 的 fields 中不包括 username ，因为 username 一旦确定就不能随便修改，在用户详细信息中不允许修改这个字段。
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
