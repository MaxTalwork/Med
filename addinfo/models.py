from django.db import models

NULLABLE = {"blank": True, "null": True}


class ComText(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название текста")
    description = models.TextField(verbose_name="Описание компании. Основной текст", **NULLABLE)
    history = models.TextField(verbose_name="История", **NULLABLE)
    mission = models.TextField(verbose_name="Миссия и ценности", **NULLABLE)
    surname = models.CharField(
        max_length=100, verbose_name="фамилия", **NULLABLE
    )
    contact_name = models.CharField(max_length=100, verbose_name="имя", **NULLABLE)
    patronymic = models.CharField(
        max_length=100, verbose_name="отчество", **NULLABLE
    )
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
    map = models.ImageField(
        upload_to="addinfo/maps/", **NULLABLE, verbose_name="Карта"
    )
    mapurl = models.URLField(verbose_name="Ссылка на карту", **NULLABLE)
    email = models.EmailField(verbose_name="Адрес эл. почты", **NULLABLE)
    is_active = models.BooleanField(verbose_name="Действующая информация", default=False)

    class Meta:
        verbose_name = "Данные о компании"
        verbose_name_plural = "Данные о компании"

    def __str__(self):
        return f"{self.name}"
