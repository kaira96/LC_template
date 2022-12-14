# Generated by Django 4.1.3 on 2022-12-06 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounting", "0002_monthlyexpenses_adress_monthlyincome_adress"),
    ]

    operations = [
        migrations.CreateModel(
            name="AllExpenses",
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
                ("summ", models.PositiveIntegerField(default=0, verbose_name="Итого")),
                ("data", models.DateTimeField(auto_now_add=True, verbose_name="Дата")),
            ],
            options={
                "verbose_name": "Итого Расходов",
                "verbose_name_plural": "Итого Расходов",
                "ordering": ["-data"],
            },
        ),
        migrations.CreateModel(
            name="AllIncome",
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
                ("summ", models.PositiveIntegerField(default=0, verbose_name="Итого")),
                ("data", models.DateTimeField(auto_now_add=True, verbose_name="Дата")),
            ],
            options={
                "verbose_name": "Итого Поступлений",
                "verbose_name_plural": "Итого Поступлений",
                "ordering": ["-data"],
            },
        ),
        migrations.AlterField(
            model_name="monthlyexpenses",
            name="data",
            field=models.DateTimeField(verbose_name="Дата"),
        ),
        migrations.AlterField(
            model_name="monthlyincome",
            name="data",
            field=models.DateTimeField(verbose_name="Дата"),
        ),
    ]
