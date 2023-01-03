from django.forms import ModelForm, Form, CharField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django import forms
from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput)

class CreatePostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = "__all__"