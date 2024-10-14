from django.db import models


class MedService(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование услуги")
    description = models.TextField(verbose_name="Описание услуги", blank=True, null=True)
    med_branch = models.TextField(verbose_name="Направление мед.услуги", blank=True, null=True)
    doctors = models.TextField(verbose_name="Список врачей", blank=True, null=True)
    price = models.IntegerField(verbose_name="Цена услуги")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return f'{self.name}'


class Doctor(models.Model):
    surname = models.CharField(max_length=100, verbose_name="фамилия")
    name = models.CharField(max_length=100, verbose_name="имя")
    patronymic = models.CharField(max_length=100, verbose_name="отчество")
    biography = models.TextField(verbose_name="биография", blank=True, null=True)
    med_branch = models.TextField(verbose_name="Направление мед", blank=True, null=True)
    appointments = models.TextField(verbose_name="записи на приём", blank=True, null=True)
    image = models.ImageField(
        upload_to="doctors/foto",
        blank=True,
        null=True,
        verbose_name="Фотография врача",
    )

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'
