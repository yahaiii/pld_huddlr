from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms.user_form import UserForm
from flask_login import current_user, login_user, logout_user, login_required
from ..models.user_model import User
from app import db

# Create a Blueprint object
user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('user_routes.login'))

    return render_template('register.html', form=form)

@user_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Redirect to a protected route

    return render_template('login.html')

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
