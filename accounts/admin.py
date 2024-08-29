from django.contrib import admin

from accounts.models import User

# Register your models here.
admin.site.register(User)

admin.site.site_header = 'Social Network Admin'
