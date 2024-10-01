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

    def __str__(self):
        return f'{self.author}  {self.created_at} - {self.content}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор коментаря', related_name='comments')
    text = models.TextField(verbose_name='Коментар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    comments_media = models.FileField(upload_to='comments_media/', verbose_name='Медіа-файл', blank=True, null=True)

    def __str__(self):
        return f'{self.from_user}  {self.created_at} - {self.text}'

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['created_at']