"""
URL configuration for the UK Hikes project.

This file maps URL patterns to the relevant views in the blog, profiles, and
testimonials apps, as well as the administration and authentication URLs.
British spelling conventions have been applied.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("profile/", include("profiles.urls")),
    path("blog/", include("blog.urls")),
    path("", home, name="home"),
    path("testimonials/", include("testimonials.urls")),
]

"""
Allow Django to serve media files during development.
"""
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
