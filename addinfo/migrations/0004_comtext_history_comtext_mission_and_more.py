# Generated by Django 5.1.2 on 2024-10-16 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("addinfo", "0003_comtext_is_active_comtext_map_comtext_mapurl_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="comtext",
            name="history",
            field=models.TextField(blank=True, null=True, verbose_name="История"),
        ),
        migrations.AddField(
            model_name="comtext",
            name="mission",
            field=models.TextField(
                blank=True, null=True, verbose_name="Миссия и ценности"
            ),
        ),
        migrations.AlterField(
            model_name="comtext",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание компании. Основной текст"
            ),
        ),
    ]
