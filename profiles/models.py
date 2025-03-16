"""
Defines the Profile model associated with the User model.

Contains signals to automatically create and save a profile when a user
is created or saved.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

EXPERIENCE_CHOICES = [
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
]


class Profile(models.Model):
    """
    Model representing a user's profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(default="", blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True
    )
    location = models.CharField(max_length=100, blank=True, null=True)
    favorite_hikes = models.TextField(blank=True, null=True)
    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        blank=True,
        null=True)
    instagram_handle = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        """
        Returns the username associated with the profile.
        """
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Ensures that a profile is created for every new user.
    """
    if created and not Profile.objects.filter(user=instance).exists():
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Saves the profile when the user is saved.
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()
