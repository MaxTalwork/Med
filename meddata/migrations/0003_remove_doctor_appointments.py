# Generated by Django 5.1.2 on 2024-10-17 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("meddata", "0002_appointment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctor",
            name="appointments",
        ),
    ]
