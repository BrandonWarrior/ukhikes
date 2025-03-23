"""
Views for the testimonials app.

This module contains views to create, list, and
display details of testimonials.
The create_testimonial view handles testimonial
submission via AJAX and returns a JSON
response, testimonial_list renders a
list of approved testimonials, and testimonial_detail
displays a single testimonial.
"""

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm
from .models import Testimonial


@login_required
def create_testimonial(request):
    """
    Handle testimonial creation.

    On POST, validate the testimonial form, assign
    the current user as the author,
    save the testimonial, and return a JSON
    response indicating success or errors.
    On GET, render the testimonial submission
    template with the form.
    """
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.author = request.user
            testimonial.save()
            messages.success(
                request,
                "Your testimonial has been sent for approval!")
            # Return a JSON response indicating success.
            return JsonResponse({'success': True})
        else:
            # Return a JSON response with error details.
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = TestimonialForm()

    return render(
        request,
        'testimonials/create_testimonial.html', {'form': form})


def testimonial_list(request):
    """
    Display a list of approved testimonials.

    Only testimonials that have been approved are rendered,
    sorted in descending order of their creation date.
    """
    testimonials = Testimonial.objects.filter(approved=True).order_by(
        '-created_at')
    return render(request,
                  'testimonials/testimonial_list.html',
                  {'testimonials': testimonials})


def testimonial_detail(request, id):
    """
    Display the details of a single testimonial.

    Retrieves a testimonial by its ID and renders
    it using the testimonial_detail template.
    """
    testimonial = get_object_or_404(Testimonial, id=id)
    return render(request, 'testimonials/testimonial_detail.html',
                  {'testimonial': testimonial})
