from allauth.account.forms import SignupForm
from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    """Form to allow users to update their profile with additional fields."""
    
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'location', 'experience_level', 'favorite_hikes', 'instagram_handle']

class CustomSignupForm(SignupForm):
    """Custom signup form to include first & last name during registration."""
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()

        # Ensure only one Profile is created per user
        Profile.objects.get_or_create(user=user)

        return user
