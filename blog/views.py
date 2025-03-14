from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Home View (Shows Only Published Posts)
def home(request):
    """Displays all published posts on the homepage."""
    posts = Post.objects.filter(status=1).order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

# Post Detail View (Includes Comments)
def post_detail(request, slug):
    """Displays a single post and its comments."""
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = post.comments.filter(approved=True).order_by("-created_at")

    # Handle POST request for adding comments
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

# Create Post View (Automatically Published)
@login_required
def create_post(request):
    """Allows users to create a new post."""
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = 1
            post.save()
            messages.success(request, "Your post has been created successfully!")
            return redirect('home')
        else:
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

# Edit Post View (Uses Unified Edit Form)
class EditPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'status']
    template_name = 'blog/edit_form.html'

    def test_func(self):
        """Ensure only the post author can edit."""
        post = self.get_object()
        return self.request.user == post.author

    def get_context_data(self, **kwargs):
        """Passes dynamic context to template"""
        context = super().get_context_data(**kwargs)
        context['object_type'] = "Post"
        context['cancel_url'] = self.object.get_absolute_url()
        return context

# Delete Post View (Only the Author Can Delete)
class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')

    def test_func(self):
        """Ensure only the post author can delete."""
        post = self.get_object()
        return self.request.user == post.author

    def get(self, request, *args, **kwargs):
        """Override to prevent rendering of the confirmation page."""
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Override to handle post request directly without a confirmation page."""
        post = self.get_object()
        post.delete()
        messages.success(request, "Your post has been deleted.")
        return redirect(self.success_url)

# Edit Comment View (Allows users to edit their own comments)
@login_required
def edit_comment(request, comment_id):
    """Allows users to edit their own comments."""
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure the user is the author of the comment
    if request.user != comment.author:
        messages.error(request, "You cannot edit someone else's comment.")
        return redirect('home')

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Your comment has been updated!")
            return redirect('post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_form.html', {
        'form': form,
        'object_type': "Comment",
        'cancel_url': comment.post.get_absolute_url(),
    })

# Delete Comment View (Allows users to delete their own comments)
@login_required
def delete_comment(request, comment_id):
    """Allows users to delete their own comments."""
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure the user is the author of the comment
    if request.user != comment.author:
        messages.error(request, "You cannot delete someone else's comment.")
        return redirect('home')

    post_slug = comment.post.slug
    comment.delete()
    messages.success(request, "Your comment has been deleted.")
    return redirect('post_detail', slug=post_slug)
