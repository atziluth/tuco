from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'identity')
    list_filter = ['identity']
    search_fields = ['username']