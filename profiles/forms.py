from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    """Form to allow users to update their profile with additional fields, including username."""
    
    username = forms.CharField(max_length=150, required=True, label="Username")

    class Meta:
        model = Profile
        fields = ['username', 'bio', 'profile_picture', 'location', 'experience_level', 'favorite_hikes', 'instagram_handle']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        # Pre-fill the username field with the current user's username
        self.fields['username'].initial = self.instance.user.username

    def save(self, commit=True):
        # Save the Profile data
        profile = super().save(commit=commit)

        # Update the username if it has been changed
        new_username = self.cleaned_data['username']
        if new_username != self.instance.user.username:
            self.instance.user.username = new_username
            self.instance.user.save()

        return profile
