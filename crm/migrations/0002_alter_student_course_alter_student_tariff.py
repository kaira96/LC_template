# Generated by Django 4.1.3 on 2022-12-03 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="course",
            field=models.CharField(
                choices=[
                    ("Python", "Python"),
                    ("JavaScript", "JavaScript"),
                    ("UX/UI", "UX/UI"),
                    ("Flutter", "Flutter"),
                    ("SMM", "SMM"),
                    ("Kids", "Kids"),
                ],
                max_length=225,
                verbose_name="Курс",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="tariff",
            field=models.CharField(
                choices=[
                    ("Online", "Online"),
                    ("Offline", "Offline"),
                    ("Standart+", "Standart+"),
                ],
                max_length=255,
                verbose_name="Тариф",
            ),
        ),
    ]
