from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(required=False)
    city = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')