from django.contrib.auth.forms import (UserCreationForm)

from django.forms import ModelForm
from meddata.forms import StyleFormMixin
from users.models import User


class UserRegForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserForm(StyleFormMixin, ModelForm):
    class Meta:
        model = User
        fields = ("surname", "name", "patronymic", "avatar", "phone_number")
