from audioop import reverse
from django.db import models

# Create your models here.
class Property(models.Model):
    title = models.CharField('Название', max_length=255)
    count = models.PositiveIntegerField('Количество', default=0)
    choice_adress = (
        ('Усенбаева 44', 'Усенбаева 44'),
        ('Ибраимова 96', 'Ибраимова 96'),
    )
    adress = models.CharField('Адрес', max_length=255, choices=choice_adress)
    data = models.DateTimeField('Дата покупки')
    price = models.PositiveIntegerField('Цена', default=0)
    image = models.FileField('Фото', upload_to='property/%Y/%m/%d/', blank=True)

    def get_absolute_url(self):
        return reverse('property', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Имущество'
        verbose_name_plural = 'Имуществ'
        ordering = ['-data']



