from django.contrib import admin
from django.contrib.admin import register

from user.models import User, UserProfile


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['username']


@register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'bio', 'website', 'is_verified']
    list_display_links = ['id', 'bio']
