from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class MedBranch(models.Model):
    name = models.CharField(max_length=100, verbose_name="Направление медицины")
    description = models.TextField(verbose_name="Направление медицины", **NULLABLE)

    class Meta:
        verbose_name = "Направление медицины"
        verbose_name_plural = "Направления медицины"

    def __str__(self):
        return f"{self.name}"


class MedService(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование услуги")
    description = models.TextField(
        verbose_name="Описание услуги", blank=True, null=True
    )
    med_branch = models.ForeignKey(MedBranch, on_delete=models.SET_NULL, **NULLABLE)
    price = models.IntegerField(verbose_name="Цена услуги")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ["med_branch", "name"]

    def __str__(self):
        return f"{self.name}"


class Doctor(models.Model):
    surname = models.CharField(max_length=100, verbose_name="фамилия")
    name = models.CharField(max_length=100, verbose_name="имя")
    patronymic = models.CharField(max_length=100, verbose_name="отчество", **NULLABLE)
    biography = models.TextField(verbose_name="биография", **NULLABLE)
    med_branch = models.ForeignKey(MedBranch, on_delete=models.SET_NULL, **NULLABLE)
    # appointments = models.TextField(verbose_name="записи на приём", **NULLABLE)
    image = models.ImageField(
        upload_to="doctors/foto",
        **NULLABLE,
        verbose_name="Фотография врача",
    )

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"
        ordering = ["surname", "name", "patronymic"]

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"


class Appointment(models.Model):
    med_service = models.ForeignKey(MedService, on_delete=models.SET_NULL, **NULLABLE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, **NULLABLE)
    med_branch = models.ForeignKey(MedBranch, on_delete=models.SET_NULL, **NULLABLE)
    end_date = models.DateTimeField(
        verbose_name="Дата",
        blank=True,
        null=True,
    )
    client = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)
    result = models.TextField(verbose_name="Результат", **NULLABLE)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["med_service", "end_date"]

    def __str__(self):
        return f"{self.med_service}, {self.doctor}, {self.med_branch}, {self.client}"
