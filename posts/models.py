from django.db import models
from accounts.models import User
from groups.models import Group
from profiles.models import Profile


class Post(models.Model):
    media = models.FileField(upload_to='posts_media/', verbose_name='Медіа-файл', blank=True, null=True)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='user_posts')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')
    likes = models.ManyToManyField(User, verbose_name='Лайки', related_name='likes')
    shares = models.ManyToManyField(User, verbose_name='Поширення', related_name='shares')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, related_name='group_posts')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, related_name='profile_posts')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор коментаря', related_name='comments')
    text = models.TextField(verbose_name='Коментар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    comments_media = models.FileField(upload_to='comments_media/', verbose_name='Медіа-файл', blank=True, null=True)
