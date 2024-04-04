from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'password', 'email', 'name', 'created_at')
    list_display = ('id', 'name', 'email', 'created_at', 'is_staff')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('id', 'name', 'created_at')}),
        # ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )

class UserProfileInline(admin.StackedInline):
    model = User
    can_delete = False
    verbose_name_plural = 'UserProfile'

admin.site.register(User, UserAdmin)