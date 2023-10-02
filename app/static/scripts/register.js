// Register.js - Add form validation for the registration page

document.addEventListener('DOMContentLoaded', function () {
    // Get form elements
    const form = document.getElementById("registration-form");
    const usernameInput = document.getElementById("username");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirm_password");

    // Get error message elements
    const emailError = document.getElementById("email-error");
    const passwordError = document.getElementById("password-error");
    const confirmPasswordError = document.getElementById("confirm-password-error");

    // Regular expression for email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Event listener for email validation
    emailInput.addEventListener("input", () => {
        const email = emailInput.value;
        if (!emailRegex.test(email)) {
            emailError.textContent = "Invalid email address";
        } else {
            emailError.textContent = "";
        }
    });

    // Event listener for password strength validation
    passwordInput.addEventListener("input", () => {
        const password = passwordInput.value;
        if (password.length < 8) {
            passwordError.textContent = "Password must be at least 8 characters";
        } else {
            passwordError.textContent = "";
        }
    });

    // Event listener for password confirmation
    confirmPasswordInput.addEventListener("input", () => {
        const password = passwordInput.value;
        const confirmPassword = confirmPasswordInput.value;
        if (password !== confirmPassword) {
            confirmPasswordError.textContent = "Passwords do not match";
        } else {
            confirmPasswordError.textContent = "";
        }
    });

    // Event listener to prevent form submission if there are validation errors
    form.addEventListener("submit", (event) => {
        if (
            !emailRegex.test(emailInput.value) ||
            passwordInput.value.length < 8 ||
            passwordInput.value !== confirmPasswordInput.value
        ) {
            event.preventDefault(); // Prevent form submission
        }
    });

});
