"""
Views for the testimonials app.

This module contains views to create and display testimonials. The
create_testimonial view handles submission via POST and returns a JSON
response for AJAX requests, while testimonial_list renders a list of
approved testimonials.
"""

from django.shortcuts import render
from django.contrib import messages
from .forms import TestimonialForm
from .models import Testimonial
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def create_testimonial(request):
    """
    Handle testimonial creation.

    On POST, validate the testimonial form, set the author, save the
    testimonial, and return a JSON response indicating success or errors.
    On GET, render the testimonial submission template with the form.
    """
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.author = request.user
            testimonial.save()
            messages.success(
                request,
                "Your testimonial has been sent for approval!"
            )
            # Return a JSON response indicating success.
            return JsonResponse({'success': True})
        else:
            # Return a JSON response with error details.
            return JsonResponse({
                'success': False,
                'errors': form.errors,
            })
    else:
        form = TestimonialForm()

    return render(
        request,
        'testimonials/create_testimonial.html',
        {'form': form}
    )


def testimonial_list(request):
    """
    Display the list of approved testimonials.

    Only testimonials that have been approved are rendered, sorted in
    descending order of their creation date.
    """
    testimonials = Testimonial.objects.filter(
        approved=True
    ).order_by('-created_at')
    return render(
        request,
        'testimonials/testimonial_list.html',
        {'testimonials': testimonials}
    )
