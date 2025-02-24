from django.urls import path
from .views import home, register, user_login, user_logout, post_detail, create_post, edit_comment, delete_comment

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('create/', create_post, name='create_post'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
