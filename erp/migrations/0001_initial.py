# Generated by Django 4.1.3 on 2022-12-03 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "count",
                    models.PositiveIntegerField(default=0, verbose_name="Количество"),
                ),
                ("adress", models.CharField(max_length=255, verbose_name="Адрес")),
                ("data", models.DateTimeField(verbose_name="Дата покупки")),
                ("price", models.PositiveIntegerField(default=0, verbose_name="Цена")),
                (
                    "image",
                    models.FileField(
                        blank=True, upload_to="property/%Y/%m/%d/", verbose_name="Фото"
                    ),
                ),
            ],
            options={
                "verbose_name": "Имущество",
                "verbose_name_plural": "Имуществ",
                "ordering": ["-data"],
            },
        ),
    ]