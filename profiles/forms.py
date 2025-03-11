from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=150, label="Username")
    email = forms.EmailField(required=True, label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.email = self.cleaned_data.get('email')
        user.save()
        return user

class ProfileUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label="Username")

    class Meta:
        model = Profile
        fields = ['username', 'bio', 'profile_picture', 'location', 'experience_level', 'favorite_hikes', 'instagram_handle']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username

    def save(self, commit=True):
        profile = super(ProfileUpdateForm, self).save(commit=commit)
        new_username = self.cleaned_data['username']
        if new_username != self.instance.user.username:
            self.instance.user.username = new_username
            self.instance.user.save()
        return profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
