from django.urls import path
from .views import home, register, user_login, user_logout, post_detail, create_post

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),  # ✅ Use slug instead of post_id
    path('create/', create_post, name='create_post'),
]
