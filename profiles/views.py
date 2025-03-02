from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from .models import Profile

# Profile View
@login_required
def profile(request):
    """Displays the user's profile page."""
    return render(request, 'profiles/profile.html')

# Edit Profile View
@login_required
def edit_profile(request):
    """Allows users to edit their profile."""
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profiles/edit_profile.html', {'form': form})
