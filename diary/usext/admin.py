from django.contrib import admin
from .models import UserExtends

@admin.register(UserExtends)
class UserExtendsAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'vip')