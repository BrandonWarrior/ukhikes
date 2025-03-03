from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Share your experience...', 
                'class': 'form-control testimonial-content'  # Added class for custom styling
            }),
            'rating': forms.Select(attrs={'class': 'form-control testimonial-rating'}),  # Custom class for rating field
        }
