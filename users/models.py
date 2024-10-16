from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    surname = models.CharField(
        max_length=100, verbose_name="фамилия", blank=True, null=True
    )
    name = models.CharField(max_length=100, verbose_name="имя", blank=True, null=True)
    patronymic = models.CharField(
        max_length=100, verbose_name="отчество", blank=True, null=True
    )
    avatar = models.ImageField(
        upload_to="users/avatars/", blank=True, null=True, verbose_name="Avatar"
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name="phone",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )
    is_staff = models.BooleanField(verbose_name="Сотрудник", default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"
