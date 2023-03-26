from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import User


@register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'id', 'email', 'is_superuser', 'is_staff', 'is_active'
    )
    list_filter = (
        'is_staff', 'is_superuser', 'is_active', 'groups__name'
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-date_joined',)
