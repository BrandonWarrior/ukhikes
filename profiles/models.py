from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Choices for experience level
EXPERIENCE_CHOICES = [
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True)  
    bio = models.TextField(default="", blank=True)
    
    # Use Django's ImageField and set a default local image
    profile_picture = models.ImageField(
        upload_to='profile_pics/',  # Directory where images are saved
        default='profile_pics/default.jpg',  # Default local image path
        blank=True
    )
    
    location = models.CharField(max_length=100, blank=True, null=True)
    favorite_hikes = models.TextField(blank=True, null=True)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, blank=True, null=True)
    instagram_handle = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username

# Automatically create a profile when a new user is registered
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Automatically save the profile when the user is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
