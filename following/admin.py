from django.contrib import admin

from following.models import Friend, Subscriber, FriendRequest

# Register your models here.
admin.site.register(Friend)
admin.site.register(FriendRequest)
admin.site.register(Subscriber)