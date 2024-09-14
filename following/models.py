from accounts.models import User
from django.db import models


class Friend(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_friend')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_friend')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.from_user} {self.to_user}'

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзі'
        unique_together = ('from_user', 'to_user')
        ordering = ['created_at']


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_request')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_request')
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.from_user} {self.to_user}'

    class Meta:
        verbose_name = 'Запит на дружбу'
        verbose_name_plural = 'Запити на дружбу'
        unique_together = ('from_user', 'to_user')
        ordering = ['created_at']


class Subscriber(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_subscribe')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_subscribe')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Підписник'
        verbose_name_plural = 'Підписники'
        unique_together = ('from_user', 'to_user')
        ordering = ['created_at']

    def __str__(self):
        return f'{self.from_user} {self.to_user}'
