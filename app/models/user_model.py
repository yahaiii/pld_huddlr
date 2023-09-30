from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class User(db.Model):
    """User model for storing user data."""

    __tablename__ = 'users'

    # User fields
    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(255), unique=True, nullable=False)
    PasswordHash = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), unique=True, nullable=False)
    FirstName = db.Column(db.String(255))
    LastName = db.Column(db.String(255))
    ProfileImageURL = db.Column(db.String(255))
    RegistrationDate = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, username, email, password, first_name=None, last_name=None, profile_image_url=None):
        """
        Initialize a new user.

        Args:
            username (str): The user's username.
            email (str): The user's email address.
            password (str): The user's password.
            first_name (str, optional): The user's first name.
            last_name (str, optional): The user's last name.
            profile_image_url (str, optional): URL to the user's profile image.
        """
        self.Username = username
        self.Email = email
        self.set_password(password)
        self.FirstName = first_name
        self.LastName = last_name
        self.ProfileImageURL = profile_image_url

    def set_password(self, password):
        """
        Hash and set the user's password.

        Args:
            password (str): The user's password.
        """
        self.PasswordHash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check if the provided password matches the stored hash.

        Args:
            password (str): The password to check.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return check_password_hash(self.PasswordHash, password)
