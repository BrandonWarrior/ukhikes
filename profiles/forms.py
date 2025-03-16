"""
Defines forms for user registration, profile updates, and login
within the profiles app.

CustomSignupForm is used by allauth for registration.
"""

from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile


class CustomSignupForm(SignupForm):
    """
    Form for user registration with additional fields.
    """
    username = forms.CharField(max_length=150, label="Username")
    email = forms.EmailField(required=True, label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, request):
        """
        Saves the user and returns the user instance.
        """
        user = super(CustomSignupForm, self).save(request)
        user.email = self.cleaned_data.get('email')
        user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating a user's profile.
    """
    username = forms.CharField(max_length=150, required=True, label="Username")

    class Meta:
        model = Profile
        fields = [
            'username',
            'bio',
            'profile_picture',
            'location',
            'experience_level',
            'favorite_hikes',
            'instagram_handle']

    def __init__(self, *args, **kwargs):
        """
        Initialises the form and sets the username initial value from the
        associated user.
        """
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username

    def save(self, commit=True):
        """
        Saves the profile and updates the related user's username if changed.
        """
        profile = super(ProfileUpdateForm, self).save(commit=commit)
        new_username = self.cleaned_data['username']
        if new_username != self.instance.user.username:
            self.instance.user.username = new_username
            self.instance.user.save()
        return profile


class LoginForm(AuthenticationForm):
    """
    Form for authenticating a user.
    """
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
