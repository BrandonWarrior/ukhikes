from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Home View (Show Only Published Posts)
def home(request):
    """Displays all published posts on the homepage."""
    posts = Post.objects.filter(status=1).order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

# Post Detail View (Includes Comments & Likes)
def post_detail(request, slug):
    """Displays a single post and its comments."""
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = post.comments.filter(approved=True).order_by("-created_at")

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been submitted and is awaiting approval!")
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

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

# Delete Comment View
@login_required
def delete_comment(request, comment_id):
    """Allows users to delete their own comments."""
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    post_slug = comment.post.slug
    comment.delete()
    messages.success(request, "Your comment has been deleted.")
    return redirect('post_detail', slug=post_slug)

# ✅ Like Post View 
@login_required
def like_post(request, post_id):
    """Handles liking a post."""
    post = get_object_or_404(Post, id=post_id)
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return JsonResponse({"liked": liked, "total_likes": post.total_likes()})

# ✅ Like Comment View 
@login_required
def like_comment(request, comment_id):
    """Handles liking a comment."""
    comment = get_object_or_404(Comment, id=comment_id)
    liked = False

    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
        liked = False
    else:
        comment.likes.add(request.user)
        liked = True

    return JsonResponse({"liked": liked, "total_likes": comment.total_likes()})
