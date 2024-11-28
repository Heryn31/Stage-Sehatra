from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User 

class UserAdmin(DefaultUserAdmin):
    # Customize the fields displayed in the admin list view
    list_display = ('id','username', 'email','is_online', 'is_active', 'is_staff')

# Register the User model with the default UserAdmin
admin.site.register(User, UserAdmin)
