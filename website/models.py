from django.db import models

class Lead(models.Model):
    name = models.CharField('ФИО', max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=20)
    data = models.DateTimeField('Дата', auto_now_add=True)
    accept = models.BooleanField('Принят', default=False)

    def __str__(self):
        return f'{self.name} - {self.phone_number}'

    class Meta:
        verbose_name = 'Лид'
        verbose_name_plural = 'Лиды'
        ordering = ['-data']

