from django.contrib import admin
from django.urls import path, include
from blog.views import home  # ✅ Import the home view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("profile/", include("profiles.urls")),
    path("blog/", include("blog.urls")),
    path("", home, name="home"),  # ✅ Define home correctly
]
