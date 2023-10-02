// Login.js - Add form validation for the login page

document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login-form');
    const passwordField = document.getElementById('password');
    const passwordError = document.getElementById('password-error');

    loginForm.addEventListener('submit', function (e) {
        if (!isStrongPassword(passwordField.value)) {
            e.preventDefault();
            passwordError.textContent = 'Password must be at least 8 characters long';
        } else {
            passwordError.textContent = '';
        }
    });

    function isStrongPassword(password) {
        // Add your password strength checking logic here
        // Example: return password.length >= 8;
    }
});
