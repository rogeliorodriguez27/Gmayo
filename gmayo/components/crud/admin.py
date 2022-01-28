from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from components.accounts.models import CustomUser

admin.site.register(CustomUser, UserAdmin)