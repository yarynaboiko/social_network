from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = [
        ('man', 'Чоловік'),
        ('woman', 'Жінка'),
        ('other', 'Інше')
    ]
    phone = models.CharField(max_length=20, verbose_name='Номер телефону')
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, verbose_name='Стать')
    birthday = models.DateField(verbose_name='Дата народження')
