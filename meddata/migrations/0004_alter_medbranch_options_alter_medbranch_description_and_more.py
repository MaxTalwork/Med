# Generated by Django 5.1.2 on 2024-10-17 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meddata", "0003_remove_doctor_appointments"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="medbranch",
            options={
                "verbose_name": "Направление медицины",
                "verbose_name_plural": "Направления медицины",
            },
        ),
        migrations.AlterField(
            model_name="medbranch",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Направление медицины"
            ),
        ),
        migrations.AlterField(
            model_name="medbranch",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Направление медицины"),
        ),
    ]
