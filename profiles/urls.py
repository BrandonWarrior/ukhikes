from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('', views.profile, name="profile"),
    path('edit/', views.edit_profile, name="edit_profile"),
    path('delete/', views.delete_account, name="delete_account"),
]
