// forgot_password.js - Add form validation for the forgot password page

document.addEventListener('DOMContentLoaded', function () {
    const forgotPasswordForm = document.getElementById('forgot-password-form');
    const emailField = document.getElementById('email');

    forgotPasswordForm.addEventListener('submit', function (e) {
        if (!isValidEmail(emailField.value)) {
            e.preventDefault();
            alert('Please enter a valid email address.');
        }
    });

    function isValidEmail(email) {
        // Add your email validation logic here
        // Example: return /\S+@\S+\.\S+/.test(email);
    }
});
