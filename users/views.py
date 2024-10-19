import random
import secrets
import string

from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render, resolve_url
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from config import settings
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegForm, UserForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"перейдите по ссылке для завершения регистрации {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


def reset_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = get_object_or_404(User, email=email)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(10))
        user.set_password(password)
        user.save()
        send_mail(
            subject="Сброс пароля",
            message=f" Ваш новый пароль {password}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return redirect(reverse("users:login"))
    return render(request, "users/reset_password.html")


class UserLogoutView(LogoutView):
    """make logout available via GET"""

    http_method_names = ["get", "post", "options"]

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def my_logout_then_login(request, login_url=None):
    """
    Log out the user if they are logged in. Then redirect to the login page.
    """
    login_url = resolve_url(settings.LOGOUT_REDIRECT_URL)
    return UserLogoutView.as_view(next_page=login_url)(request)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy("meddata:doctor_list")


class UserDetailView(DetailView):
    model = User

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.save()
        return self.object
