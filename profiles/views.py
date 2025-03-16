"""
Contains views for user registration, login, logout and profile management.
"""

from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import ProfileUpdateForm
from blog.models import Post, Comment


def register(request):
    """
    Handles user registration. Saves the user and logs them in, then
    redirects to the profile page.
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


def login_view(request):
    """
    Handles user login and redirects to the profile page upon successful
    authentication.
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


def logout_view(request):
    """
    Logs out the user and redirects to the home page with a success message.
    """
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")


@login_required
def profile(request):
    """
    Displays the user's profile page with their posts, paginated.
    """
    user_posts = (
        Post.objects.filter(author=request.user)
        .order_by('-created_at')
    )
    paginator = Paginator(user_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'profiles/profile.html', {'page_obj': page_obj})


@login_required
def edit_profile(request):
    """
    Permits users to edit their profile details.
    """
    if request.method == "POST":
        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profiles/edit_profile.html', {'form': form})


@login_required
def delete_account(request):
    """
    Confirms and deletes the user's account along with their related posts
    and comments.
    """
    if request.method == "POST":
        posts = Post.objects.filter(author=request.user)
        comments = Comment.objects.filter(author=request.user)
        posts.delete()
        comments.delete()
        user = request.user
        user.delete()
        messages.success(
            request,
            "Account deleted successfully."
        )
        return redirect("home")
    return redirect("profile")
