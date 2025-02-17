from django.contrib import admin
from django.urls import path, include
from blog.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("profile/", include("profiles.urls")),
    path("blog/", include("blog.urls")),
    path("", home, name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)