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
    course = models.CharField('Курс', max_length=225, choices=choice_courses)
    choice_tariff = (
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Standart+', 'Standart+'),
    )
    tariff = models.CharField('Тариф', max_length=255, choices=choice_tariff)
    payment = models.PositiveIntegerField('Оплата', default=0)
    data = models.DateTimeField('Дата', auto_now_add=True)
    finished = models.DateTimeField('Выпуск')
    certificate = models.FileField('Сертификат', upload_to='certificate/%Y/%m/%d/')
    accept = models.BooleanField('Принят', default=False)

    def __str__(self):
        return f'{self.name} - {self.phone_number}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['-data']