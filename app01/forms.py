from django import forms
from captcha.fields import CaptchaField
import time


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={
        'class': 'form-control btn-login', 'placeholder': "请输入用户名", 'name': 'username'
    }))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={
        'class': 'form-control btn-login', 'placeholder': "请输入密码", 'name': 'password'
    }))
    # captcha = CaptchaField(label='验证码', widget=forms.TextInput(attrs={
    #     #     'class': 'form-control btn-login', 'placeholder': "请输入验证码",
    # }))
    captcha = CaptchaField(label='验证码',)


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={
        'class': 'form-control btn-login', 'placeholder': "请输入用户名", 'name': 'username'
    }))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={
        'class': 'form-control btn-login', 'placeholder': "请输入密码", 'name': 'password1'
    }))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={
        'class': 'form-control btn-login', 'placeholder': "确认密码", 'name': 'password2'
    }))
    nickname = forms.CharField(label="昵称", max_length=128, widget=forms.TextInput(attrs={
        'class': 'form-control btn-login', 'placeholder': "请输入昵称", 'name': 'nickname'
    }))
    email = forms.EmailField(label="邮箱", max_length=256, widget=forms.EmailInput(attrs={
        'class': 'form-control btn-login', 'placeholder': "请输入密码", 'name': 'email'
    }))
    gender = forms.ChoiceField(label="性别", choices=gender)
    phone = forms.CharField(label="手机号", max_length=128, widget=forms.TextInput(attrs={
        'class': 'form-control btn-login', 'placeholder': "请输入手机号", 'name': 'phone'
    }))
    # create_date = forms.DateField(label="创建时间", widget=forms.DateInput)
    captcha = CaptchaField(label='验证码', )
