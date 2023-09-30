from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class User(db.Model):
    """User model for storing user data."""

    __tablename__ = 'users'

    UserID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(255), unique=True, nullable=False)
    PasswordHash = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), unique=True, nullable=False)
    FirstName = db.Column(db.String(255))
    LastName = db.Column(db.String(255))
    ProfileImageURL = db.Column(db.String(255))
    RegistrationDate = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, username, email, password, first_name=None, last_name=None, profile_image_url=None):
        self.Username = username
        self.Email = email
        self.set_password(password)
        self.FirstName = first_name
        self.LastName = last_name
        self.ProfileImageURL = profile_image_url

    def set_password(self, password):
        """Hash and set the user's password."""
        self.PasswordHash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.PasswordHash, password)
