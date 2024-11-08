from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

# Define a custom UserAdmin class
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None,{'fields':('username','password')}),
        ('Personal info', {'fields':('first_name','last_name','date_of_birth')}),
        ('Permissions', {'fields':('is_active', 'is_staff' , 'is_superuser','groups','user_permissions')}),
        ('Important dates', {'fields':('last_login','date_joined')}),

    )
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
