from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from profiles.models import Profile

# Extend User model to show profiles in admin panel


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profiles"


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)


# Unregister the default User model and register our customized one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register Profile separately


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "profile_picture")
