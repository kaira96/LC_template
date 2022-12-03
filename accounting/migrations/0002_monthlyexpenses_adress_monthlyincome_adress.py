# Generated by Django 4.1.3 on 2022-12-03 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounting", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="monthlyexpenses",
            name="adress",
            field=models.CharField(
                choices=[
                    ("Усенбаева 44", "Усенбаева 44"),
                    ("Ибраимова 96", "Ибраимова 96"),
                ],
                default=1,
                max_length=255,
                verbose_name="Адрес",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="monthlyincome",
            name="adress",
            field=models.CharField(
                choices=[
                    ("Усенбаева 44", "Усенбаева 44"),
                    ("Ибраимова 96", "Ибраимова 96"),
                ],
                default=1,
                max_length=255,
                verbose_name="Адрес",
            ),
            preserve_default=False,
        ),
    ]
