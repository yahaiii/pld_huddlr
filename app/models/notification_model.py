from app import db
import datetime

class Notification(db.Model):
    """Model for storing notification details."""

    NotificationID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    RecipientID = db.Column(db.Integer, db.ForeignKey('users.UserID'))
    Message = db.Column(db.String(255), nullable=False)
    IsRead = db.Column(db.Boolean, default=False)
    CreatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # Define a relationship with the User model
    user = db.relationship('User', foreign_keys=[RecipientID], backref='notifications_received')

    def __repr__(self):
        return f'<Notification {self.NotificationID}>'
