from django.urls import path
from . import views

urlpatterns = [
    # Register and login paths
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    
    # Logout path 
    path('logout/', views.logout_view, name="logout"),
    
    # Profile-related paths
    path('', views.profile, name="profile"),
    path('edit/', views.edit_profile, name="edit_profile"),
    path('delete/', views.delete_account, name='delete_account'),

]
