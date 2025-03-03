document.addEventListener('DOMContentLoaded', function() {
    const testimonialForm = document.getElementById('testimonialForm');
    const testimonialMessage = document.getElementById('testimonialMessage');
    
    testimonialForm.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent the form from submitting normally
        
        const formData = new FormData(testimonialForm);
        
        // Perform AJAX request
        fetch('/testimonials/testimonial/create/', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Hide the form
                testimonialForm.style.display = 'none';
                
                // Show the success message and "Return to Home" button
                testimonialMessage.style.display = 'block';
            } else {
                // Show error message if submission fails
                testimonialMessage.classList.add('testimonial-error-message');
                testimonialMessage.classList.remove('testimonial-success-message');
                testimonialMessage.style.display = 'block';
                testimonialMessage.textContent = 'There was an error submitting your testimonial. Please try again.';
            }
        })
        .catch(error => {
            testimonialMessage.classList.add('testimonial-error-message');
            testimonialMessage.classList.remove('testimonial-success-message');
            testimonialMessage.style.display = 'block';
            testimonialMessage.textContent = 'An error occurred. Please try again.';
        });
    });
});
