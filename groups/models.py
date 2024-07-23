from django.db import models
from accounts.models import User


class Group(models.Model):
    name = models.CharField(max_length=250, verbose_name='Назва групи')
    description = models.TextField(max_length=500, verbose_name='Опис групи')
    image = models.ImageField(upload_to='group_images/', verbose_name='Зображення групи')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    image = models.ImageField(upload_to='posts_images/', verbose_name='Зображення поста')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації поста')


class Like(models.Model):
    like = models.ManyToManyField(User, verbose_name='Лайк на пост')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_post = models.ForeignKey(Post, on_delete=models.SET_NULL)


class Comment(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор коментаря')
    comment = models.TextField(verbose_name='Коментар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')

