/**
 * Account Deletion Modal Script
*/

document.getElementById('delete-account-btn').addEventListener('click', function() {
    // Show the modal
    document.getElementById('confirmation-modal').style.display = 'block';
});

// Close the modal if the close button is clicked
document.getElementById('close-modal-btn').addEventListener('click', function() {
    document.getElementById('confirmation-modal').style.display = 'none';
});

// If the user confirms, submit the form to delete the account
document.getElementById('confirm-delete-btn').addEventListener('click', function() {
    document.getElementById('delete-account-form').submit();
});

// If the user cancels, close the modal
document.getElementById('cancel-delete-btn').addEventListener('click', function() {
    document.getElementById('confirmation-modal').style.display = 'none';
});
