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
