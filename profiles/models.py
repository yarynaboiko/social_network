from accounts.models import User
from django.db import models


class Profile(models.Model):
    PROFILE_TYPES = [
        ('private', 'Приватний'),
        ('public', 'Публічний')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=150, verbose_name="Ім'я")
    surname = models.CharField(max_length=150, verbose_name="Прізвище")
    image = models.ImageField(upload_to='profile_images/', verbose_name='Зображення профілю')
    cover = models.ImageField(upload_to='profile_images/', verbose_name='Обкладинка профілю', blank=True, null=True)
    city = models.CharField(max_length=150, verbose_name='Місто', blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name='Країна', blank=True, null=True)
    status = models.TextField(max_length=300, verbose_name='Статус', blank=True, null=True)
    type = models.CharField(max_length=50, choices=PROFILE_TYPES, default='public')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.surname} - {self.pk}'

