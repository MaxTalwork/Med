from django.contrib.auth.views import LoginView
from django.urls import path
from django.views.decorators.cache import cache_page

from users.apps import UsersConfig
from users.views import (UserCreateView, UserDetailView, UserLogoutView,
                         UserUpdateView, email_verification,
                         my_logout_then_login, reset_password)

app_name = UsersConfig.name
urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", my_logout_then_login, name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path("reset_password/", reset_password, name="reset_password"),
    path("user/<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
    path("user/<int:pk>/", cache_page(60)(UserDetailView.as_view()), name="user"),
]
