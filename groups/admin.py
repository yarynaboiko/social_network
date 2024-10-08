from django.contrib import admin

from groups.models import Group, GroupMember

# Register your models here.
admin.site.register(Group)
admin.site.register(GroupMember)