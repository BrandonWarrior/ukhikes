from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)  # Add this line for image upload

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Returns the URL for the post detail page."""
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def get_absolute_url(self):
        """Returns the URL for the post that the comment belongs to."""
        return reverse('post_detail', kwargs={'slug': self.post.slug})

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
