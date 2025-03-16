"""
Registers custom admin interfaces for user and profile models.

CustomUserAdmin customizes Django's default UserAdmin to use email and
username.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    """
    Admin interface for the custom user model.
    """
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2"),
        }),
    )
    list_display = ("email", "username", "is_staff", "date_joined")
    search_fields = ("email", "username")
    ordering = ("email",)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
