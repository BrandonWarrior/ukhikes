from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Register View
def register(request):
    """Handles user registration."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = UserCreationForm()
    
    return render(request, "profiles/signup.html", {"form": form})

# Login View
def login_view(request):
    """Handles user login."""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()
    
    return render(request, "profiles/login.html", {"form": form})

# Logout View
def logout_view(request):
    """Logs out the user and redirects to home."""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")

# Profile View
@login_required
def profile(request):
    """Displays the user's profile page."""
    return render(request, 'profiles/profile.html')

# Edit Profile View
@login_required
def edit_profile(request):
    """Allows users to edit their profile."""
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profiles/edit_profile.html', {'form': form})
