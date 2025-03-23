"""
Models for the testimonials app.
"""

from django.db import models
from django.contrib.auth.models import User


class Testimonial(models.Model):
    """
    Model representing a user testimonial.

    Attributes:
        author: Foreign key to the User who submitted the testimonial.
        content: The text content of the testimonial.
        rating: A numeric rating from 1 to 5.
        created_at: Timestamp when the testimonial was created.
        approved: Boolean indicating if the testimonial is approved.
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="testimonials"
    )
    content = models.TextField()
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        default=5
    )
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the Testimonial.
        """
        return (
            f"Testimonial by {self.author.username} - "
            f"{self.rating}/5"
        )
