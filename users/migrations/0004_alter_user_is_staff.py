# Generated by Django 5.1.2 on 2024-10-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_remove_user_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False, verbose_name="Сотрудник"),
        ),
    ]
