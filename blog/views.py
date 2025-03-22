from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import Post, Comment
from .forms import PostForm, CommentForm


def home(request):
    """
    Displays paginated published posts on the index page.
    """
    posts = Post.objects.filter(status=1).order_by("-created_at")
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/index.html", {"page_obj": page_obj})


def post_detail(request, slug):
    """
    Displays the details of a single post and its comments.
    Processes new comment submissions.
    """
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = post.comments.filter(approved=True).order_by("-created_at")

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", slug=post.slug)
        else:
            messages.error(
                request,
                "Comment not posted. Enter a valid comment."
            )

    else:
        form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "form": form,
        }
    )


@login_required
def create_post(request):
    """
    Permits authenticated users to create a new blog post.
    After a successful submission, the post is automatically published
    and the user is redirected to the index page with a success message.
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = 1
            post.save()
            messages.success(
                request, "Your post has been created successfully!")
            return redirect("index")
        else:
            messages.error(
                request, "Post not uploaded. Check title and content.")
            return redirect("index")

    else:
        form = PostForm()

    return render(request, "blog/create_post.html", {"form": form})


class EditPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Permits a post author to edit their blog post.
    The post is automatically set to published (status=1) upon saving.
    """
    model = Post
    fields = ["title", "content", "image"]
    template_name = "blog/edit_form.html"

    def test_func(self):
        """
        Verifies that the current user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author

    def get_context_data(self, **kwargs):
        """
        Supplies additional context to the edit form template.
        """
        context = super().get_context_data(**kwargs)
        context["object_type"] = "Post"
        context["cancel_url"] = self.object.get_absolute_url()
        return context

    def form_valid(self, form):
        """
        Automatically sets the post status to published (1) before saving.
        """
        form.instance.status = 1
        response = super().form_valid(form)
        print("Updated Post:", self.object.title,
              self.object.content, self.object.status)
        return response

    def get_success_url(self):
        """
        Redirects to the post detail page after editing.
        """
        return reverse("post_detail", kwargs={"slug": self.object.slug})


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Permits a post author to delete their blog post.
    """
    model = Post
    success_url = reverse_lazy("index")

    def test_func(self):
        """
        Verifies that the current user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests by delegating to the POST method.
        """
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Deletes the post and redirects to the
        index page with a success message.
        """
        post = self.get_object()
        post.delete()
        messages.success(request, "Your post has been deleted.")
        return redirect(self.success_url)


@login_required
def edit_comment(request, comment_id):
    """
    Permits a user to edit their own comment.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        messages.error(request, "You cannot edit someone else's comment.")
        return redirect("index")

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Your comment has been updated!")
            return redirect("post_detail", slug=comment.post.slug)

    else:
        form = CommentForm(instance=comment)

    return render(
        request,
        "blog/edit_form.html",
        {
            "form": form,
            "object_type": "Comment",
            "cancel_url": comment.post.get_absolute_url(),
        }
    )


@login_required
def delete_comment(request, comment_id):
    """
    Permits a user to delete their own comment.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        messages.error(request, "You cannot delete someone else's comment.")
        return redirect("index")

    post_slug = comment.post.slug
    comment.delete()
    messages.success(request, "Your comment has been deleted.")
    return redirect("post_detail", slug=post_slug)
