from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin): # admin model for user
    list_display = ["username", "email", "is_staff"] # display fields

admin.site.register(User, UserAdmin)
# Register your models here.
