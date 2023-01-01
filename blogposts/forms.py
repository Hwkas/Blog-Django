from django.forms import ModelForm, CharField, PasswordInput
from .models import *


class RegisterForm(ModelForm):
    password = CharField(widget=PasswordInput)
    class Meta:
        model = User
        fields = "__all__"


class CreatePostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = "__all__"