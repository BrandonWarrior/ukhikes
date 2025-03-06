from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileUpdateForm
from blog.models import Post, Comment

# Register View
def register(request):
    """
    Handles user registration, saves the user, and logs them in.
    Redirects to the profile page after successful registration.
    """
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
    """
    Handles user login, authenticates, and redirects to the profile page.
    """
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
    """
    Logs out the user and redirects to home with a success message.
    """
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")

# Profile View
@login_required
def profile(request):
    """
    Displays the user's profile page, showing their details and posts.
    """
    # Fetch the logged-in user's posts
    user_posts = Post.objects.filter(author=request.user).order_by('-created_at')

    # Render the profile page with user posts
    return render(request, 'profiles/profile.html', {'user_posts': user_posts})

# Edit Profile View
@login_required
def edit_profile(request):
    """
    Allows users to edit their profile, including the username, profile picture, and bio.
    """
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profiles/edit_profile.html', {'form': form})


# Delete Account View
@login_required
def delete_account(request):
    """
    Confirms and deletes the user's account. Redirects to the home page upon deletion.
    This also handles the deletion of related posts and comments.
    """
    if request.method == "POST":
        # Proceed with deletion if the user confirms
        posts = Post.objects.filter(author=request.user)
        comments = Comment.objects.filter(author=request.user)

        # Delete related posts and comments
        posts.delete()
        comments.delete()

        # Delete the user's profile and account
        user = request.user
        user.delete()

        messages.success(request, "Your account has been successfully deleted.")
        return redirect("home")
    
    # If it's a GET request, show an error or redirect, but the form submission will handle the deletion
    return redirect("profile")
