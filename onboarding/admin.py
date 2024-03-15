from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('account_id', 'password', 'email', 'username', 'created_at')
    list_display = ('account_id', 'username', 'email', 'created_at', 'is_staff')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('account_id', 'username', 'created_at')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )

admin.site.register(User, UserAdmin)