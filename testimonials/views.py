from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TestimonialForm
from .models import Testimonial
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def create_testimonial(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.author = request.user
            testimonial.save()
            messages.success(request, "Your testimonial has been sent for approval!")
            # This part will send a JSON response with success
            return JsonResponse({'success': True})
        else:
            # Return an error message if the form is invalid
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = TestimonialForm()

    return render(request, 'testimonials/create_testimonial.html', {'form': form})


def testimonial_list(request):
    """Display the list of testimonials."""
    testimonials = Testimonial.objects.filter(approved=True).order_by('-created_at')  # Only approved testimonials
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})
