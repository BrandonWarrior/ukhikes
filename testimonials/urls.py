"""
URL configuration for the testimonials app.

This file maps URL patterns to the corresponding views for creating,
listing, and viewing details of testimonials.
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'testimonial/create/',
        views.create_testimonial,
        name='create_testimonial'
    ),
    path(
        'list/',
        views.testimonial_list,
        name='testimonial_list'
    ),
    path(
        'testimonial/<int:id>/',
        views.testimonial_detail,
        name='testimonial_detail'
    ),
]
