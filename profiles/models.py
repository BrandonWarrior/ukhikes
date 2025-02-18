from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True)  
    bio = models.TextField(default="", blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/',  # Remove "media/" from upload_to path
        default='profile_pics/default-avatar.jpg'  # Correct default image path
    )

    def __str__(self):
        return self.user.username

# Signal to automatically create a profile when a user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
