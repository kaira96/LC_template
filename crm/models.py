from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField('ФИО', max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=20)
    choice_courses = (
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('UX/UI', 'UX/UI'),
        ('Flutter', 'Flutter'),
        ('SMM', 'SMM'),
        ('Kids', 'Kids'),
    )
    course = models.CharField('Курс', max_length=225, choices=choice_courses, blank=True)
    choice_tariff = (
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Standart+', 'Standart+'),
    )
    tariff = models.CharField('Тариф', max_length=255, choices=choice_tariff, blank=True)
    payment = models.PositiveIntegerField('Оплата', default=0, blank=True)
    data = models.DateTimeField('Дата', blank=True)
    finished = models.DateTimeField('Выпуск', blank=True)
    certificate = models.FileField('Сертификат', upload_to='certificate/%Y/%m/%d/',
                                   blank=True)
    accept = models.BooleanField('Принят', default=False)

    def __str__(self):
        return f'{self.name} - {self.phone_number}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['-data']