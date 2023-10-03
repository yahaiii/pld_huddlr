from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms.user_form import RegistrationForm, LoginForm, ForgotPasswordForm
from ..models.user_model import User
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from sqlalchemy import text  # Import the 'text' function

# Create a Blueprint object
user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm() # Create an instance of the RegistrationForm

    if request.method == 'POST':
        if form.validate_on_submit():
            # Form submission logic
            username = form.username.data
            email = form.email.data
            password = form.password.data

            # Create a new user and add them to the database
            user = User(username=username, email=email, password=password)
            try:
                db.session.add(user)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(str(e))

            flash('Your account has been created successfully!', 'success')
            return redirect(url_for('user_routes.login')) # Redirect to the login page

    return render_template('register.html', form=form)

@user_routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            
            if user and user.check_password(password):
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))  # Redirect to a protected route

    return render_template('login.html', form=form)

@user_routes.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data

            # Check if the email exists in the database
            user = User.query.filter_by(Email=email).first()

            if user:
                # Generate a random temporary password
                temporary_password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

                # Set the temporary password for the user and save to the database
                user.set_password(temporary_password)
                db.session.commit()

                # Send an email to the user with the temporary password
                # You will need to implement email sending functionality here

                flash('An email with instructions to reset your password has been sent.', 'success')
                return redirect(url_for('user_routes.login'))  # Redirect to the login page after sending email
            else:
                flash('Email address not found in our records.', 'danger')

    return render_template('forgot_password.html', form=form)

@user_routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful!', 'success')
    return redirect(url_for('login'))

@user_routes.route('/profile')
@login_required
def profile():
    # Access the current user with current_user (provided by Flask-Login)
    user = User.query.get(current_user.id)
    return render_template('profile.html', user=user)

@user_routes.route('/check-db-connection')
def check_db_connection():
    try:
        # Attempt to perform a simple database operation
        db.session.query().from_statement(text('SELECT 1')).all()
        return "Database connection is working."
    except Exception as e:
        return f"Database connection error: {str(e)}"
