import random
import string

from django.contrib.auth import password_validation
from django.contrib.auth.forms import (PasswordResetForm, SetPasswordForm,
                                       UserCreationForm)
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from config.settings import EMAIL_HOST_USER
from meddata.forms import StyleFormMixin
from users.models import User


class UserRegForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
