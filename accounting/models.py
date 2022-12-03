from django.db import models
from django.urls import reverse

# Create your models here.
class MonthlyIncome(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    summ = models.PositiveIntegerField('Сумма', default=0)
    choice_adress = (
        ('Усенбаева 44', 'Усенбаева 44'),
        ('Ибраимова 96', 'Ибраимова 96'),
    )
    adress = models.CharField('Адрес', max_length=255, choices=choice_adress)
    data = models.DateTimeField('Дата')

    def get_absolute_url(self):
        return reverse('monthly_income', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ежемесячное поступление'
        verbose_name_plural = 'Ежемесячные поступления'
        ordering = ['-data']

class MonthlyExpenses(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    summ = models.PositiveIntegerField('Сумма', default=0)
    choice_adress = (
        ('Усенбаева 44', 'Усенбаева 44'),
        ('Ибраимова 96', 'Ибраимова 96'),
    )
    adress = models.CharField('Адрес', max_length=255, choices=choice_adress)
    data = models.DateTimeField('Дата')

    def get_absolute_url(self):
        return reverse('monthly_expenses', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ежемесячный расход'
        verbose_name_plural = 'Ежемесячные расходы'
        ordering = ['-data']