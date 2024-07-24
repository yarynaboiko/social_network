from django.db import models
from accounts.models import User


class Group(models.Model):
    name = models.CharField(max_length=250, verbose_name='Назва групи')
    description = models.TextField(max_length=500, verbose_name='Опис групи')
    image = models.ImageField(upload_to='group_images/', verbose_name='Зображення групи')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Власник групи', related_name='user_groups')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення групи')


class GroupMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_groups', verbose_name='Учасник')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='members', verbose_name='Група')
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата приєднання до групи')
    is_admin = models.BooleanField(default=False, verbose_name='Адміністратор')
