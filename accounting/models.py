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


    def total(self):
        return sum([item.summ for item in MonthlyIncome.objects.all()])

    def save(self, *args, **kwargs):
        all_income = AllIncome.objects.filter(pk=1).get()
        total = self.total() + int(str(all_income.save()))



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

    def total(self):
        return sum([item.summ for item in MonthlyExpenses.objects.all()])

    def get_absolute_url(self):
        return reverse('monthly_expenses', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ежемесячный расход'
        verbose_name_plural = 'Ежемесячные расходы'
        ordering = ['-data']


class AllIncome(models.Model):
    summ = models.PositiveIntegerField('Итого', default=0)
    data = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return str(self.summ)

    class Meta:
        verbose_name = 'Итого Поступлений'
        verbose_name_plural = 'Итого Поступлений'
        ordering = ['-data']


class AllExpenses(models.Model):
    summ = models.PositiveIntegerField('Итого', default=0)
    data = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return str(self.summ)

    class Meta:
        verbose_name = 'Итого Расходов'
        verbose_name_plural = 'Итого Расходов'
        ordering = ['-data']