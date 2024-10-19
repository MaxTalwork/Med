import uuid

from django.db import models

NULLABLE = {"blank": True, "null": True}


class ComText(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название текста")
    description = models.TextField(
        verbose_name="Описание компании. Основной текст", **NULLABLE
    )
    history = models.TextField(verbose_name="История", **NULLABLE)
    mission = models.TextField(verbose_name="Миссия и ценности", **NULLABLE)
    surname = models.CharField(max_length=100, verbose_name="фамилия", **NULLABLE)
    contact_name = models.CharField(max_length=100, verbose_name="имя", **NULLABLE)
    patronymic = models.CharField(max_length=100, verbose_name="отчество", **NULLABLE)
    avatar = models.ImageField(
        upload_to="addinfo/avatars/", **NULLABLE, verbose_name="Avatar"
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name="phone",
        **NULLABLE,
        help_text="Введите номер телефона",
    )
    adress = models.TextField(verbose_name="Адрес", **NULLABLE)
    map = models.ImageField(upload_to="addinfo/maps/", **NULLABLE, verbose_name="Карта")
    mapurl = models.URLField(verbose_name="Ссылка на карту", **NULLABLE)
    email = models.EmailField(verbose_name="Адрес эл. почты", **NULLABLE)
    is_active = models.BooleanField(
        verbose_name="Действующая информация", default=False
    )
    is_main = models.BooleanField(verbose_name="Основная информация", default=False)

    class Meta:
        verbose_name = "Данные о компании"
        verbose_name_plural = "Данные о компании"
        ordering = ["name", "surname"]

    def __str__(self):
        return f"{self.name}"


class Feedback(models.Model):
    STATUSES = [
        ("New", "Новая"),
        ("InProgress", "В работе"),
        ("Complete", "Заверешена"),
    ]
    title = models.CharField(max_length=100, verbose_name="Тема обращения", **NULLABLE)
    description = models.TextField(verbose_name="Ваше обращение", **NULLABLE)
    surname = models.CharField(max_length=100, verbose_name="Ваша фамилия", **NULLABLE)
    contact_name = models.CharField(max_length=100, verbose_name="Ваше имя", **NULLABLE)
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Номер телефона",
        **NULLABLE,
        help_text="Введите номер телефона",
    )
    email = models.EmailField(verbose_name="Адрес эл. почты", **NULLABLE)
    feedback = models.TextField(verbose_name="Ваше обращение", **NULLABLE)
    status = models.CharField(choices=STATUSES, default="Новая", verbose_name="Статус")

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"

    def __str__(self):
        return f"{self.id} {self.title}"
