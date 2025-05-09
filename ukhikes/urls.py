from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from blog.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("profile/", include("profiles.urls")),
    path("blog/", include("blog.urls")),
    path("", home, name="home"),
    path("testimonials/", include("testimonials.urls")),
    # Redirect /accounts/profile/ to /profile/
    path("accounts/profile/", lambda request: redirect('profile')),
]

# Serve static files only when DEBUG=True (local development)
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
