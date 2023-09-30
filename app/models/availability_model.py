from app import db
import datetime

class Availability(db.Model):
    """Availability model for storing user availability data."""

    __tablename__ = 'availability'

    AvailabilityID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), nullable=False)
    StartDateTime = db.Column(db.DateTime, nullable=False)
    EndDateTime = db.Column(db.DateTime, nullable=False)

    # Define a relationship with the User model
    user = db.relationship('User', backref='availabilities')

    def __init__(self, user, start_datetime, end_datetime):
        self.user = user
        self.StartDateTime = start_datetime
        self.EndDateTime = end_datetime

    def __repr__(self):
        return f'<Availability {self.AvailabilityID}>'
