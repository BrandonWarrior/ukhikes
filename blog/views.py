from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Home View (Show Only Published Posts)
def home(request):
    """Displays all published posts on the homepage."""
    posts = Post.objects.filter(status=1).order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

# Post Detail View (Now Uses Slugs)
def post_detail(request, slug):
    """Displays a single post."""
    post = get_object_or_404(Post, slug=slug, status=1)
    return render(request, 'blog/post_detail.html', {'post': post})

# Register View
def register(request):
    """Handles user registration."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home') 
    else:
        form = UserCreationForm()
    
    return render(request, 'blog/register.html', {'form': form})

# Login View
def user_login(request):
    """Handles user login."""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'blog/login.html', {'form': form})

# Logout View
@login_required
def user_logout(request):
    """Logs the user out."""
    logout(request)
    messages.info(request, "You have logged out successfully!")
    return redirect('home')

# Create Post View
@login_required
def create_post(request):
    """Allows users to create a new post."""
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Your post has been created successfully!")
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})
