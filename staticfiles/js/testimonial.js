/**
 * Testimonial Submission Script
 *
 * This script handles the submission of the testimonial form via AJAX.
 * When the form is submitted, it sends the data to the server, then
 * displays a styled alert in the baseMessages container based on the
 * response. If the submission is successful, the form is hidden.
 */
document.addEventListener('DOMContentLoaded', function() {
    const testimonialForm = document.getElementById('testimonialForm');
    const baseMessages = document.getElementById('baseMessages');

    if (testimonialForm) {
        testimonialForm.addEventListener('submit', function(e) {
            e.preventDefault();
            console.log('Testimonial form submitted');

            const formData = new FormData(testimonialForm);

            // Perform AJAX request
            fetch('/testimonials/testimonial/create/', {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                let alertHtml = '';
                if (data.success) {
                    alertHtml = `
                        <div class="alert alert-success alert-dismissible fade show" 
                             role="alert">
                            Your testimonial has been sent for approval!
                            <button type="button" class="btn-close" 
                                    data-bs-dismiss="alert" aria-label="Close">
                            </button>
                        </div>`;
                    testimonialForm.style.display = 'none';
                } else {
                    alertHtml = `
                        <div class="alert alert-danger alert-dismissible fade show" 
                             role="alert">
                            There was an error submitting your testimonial. 
                            Please try again.
                            <button type="button" class="btn-close" 
                                    data-bs-dismiss="alert" aria-label="Close">
                            </button>
                        </div>`;
                }
                if (baseMessages) {
                    baseMessages.innerHTML = alertHtml;
                } else {
                    alert(alertHtml);
                }
            })
            .catch(error => {
                const alertHtml = `
                        <div class="alert alert-danger alert-dismissible fade show" 
                             role="alert">
                            An error occurred. Please try again.
                            <button type="button" class="btn-close" 
                                    data-bs-dismiss="alert" aria-label="Close">
                            </button>
                        </div>`;
                if (baseMessages) {
                    baseMessages.innerHTML = alertHtml;
                } else {
                    alert(alertHtml);
                }
            });
        });
    } else {
        console.error('testimonialForm not found');
    }
});
