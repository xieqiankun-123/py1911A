from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, min_length=3, label="输入用户名", help_text="用户名最短3位,最长50位")
    password = forms.CharField(max_length=20, min_length=3, widget=forms.PasswordInput, label="输入密码",
                               help_text="密码最短3位,最长50位")


class RegistForm(forms.ModelForm):
    password2 = forms.CharField(max_length=20, min_length=3, widget=forms.PasswordInput, label="重复密码",
                                help_text="密码最短3位,最长50位")

    class Meta:
        model = User
        fields = ["username", "password"]
        labels = {
            "username": "输入用户名",
            "password": "输入密码"
        }
        help_texts = {
            "username": "用户名最短3位,最长50位",
            "password": "密码最短3位,最长50位"
        }
        widgets = {
            "password":forms.PasswordInput

        }
