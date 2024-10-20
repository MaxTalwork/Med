# Generated by Django 5.1.2 on 2024-10-18 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "meddata",
            "0004_alter_medbranch_options_alter_medbranch_description_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="appointment",
            options={
                "ordering": ["med_service", "end_date"],
                "verbose_name": "Запись",
                "verbose_name_plural": "Записи",
            },
        ),
        migrations.AlterModelOptions(
            name="doctor",
            options={
                "ordering": ["surname", "name", "patronymic"],
                "verbose_name": "Врач",
                "verbose_name_plural": "Врачи",
            },
        ),
        migrations.AlterModelOptions(
            name="medservice",
            options={
                "ordering": ["med_branch", "name"],
                "verbose_name": "Услуга",
                "verbose_name_plural": "Услуги",
            },
        ),
    ]
