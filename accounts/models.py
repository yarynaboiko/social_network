from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = [
        ('man', 'Чоловік'),
        ('woman', 'Жінка'),
        ('other', 'Інше')
    ]
    phone = models.CharField(max_length=20, verbose_name='Номер телефону', blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, verbose_name='Стать', default='other')
    birthday = models.DateField(verbose_name='Дата народження', blank=True, null=True)

    def __str__(self):
        return f'{self.username} - {self.first_name} {self.last_name}'

    def get_friends_count(self):
        return self.to_friend.count() + self.from_friend.count()

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
