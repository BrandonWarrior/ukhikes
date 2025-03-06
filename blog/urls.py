from django.urls import path
from .views import (
    home, post_detail, create_post, 
    EditPostView, DeletePostView,  
    edit_comment, delete_comment
)

urlpatterns = [
    path('', home, name='home'),
    path('post/create/', create_post, name='create_post'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', EditPostView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
