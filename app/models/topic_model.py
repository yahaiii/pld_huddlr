from app import db  # Import the SQLAlchemy instance from your Flask app
import datetime

class Topic(db.Model):
    """Topic model for storing information about topics."""

    __tablename__ = 'topics'

    TopicID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    TopicTitle = db.Column(db.String(255), nullable=False)
    TopicDescription = db.Column(db.String(1000))
    CreatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # Add any additional fields or relationships here

    def __init__(self, title, description=None):
        self.TopicTitle = title
        self.TopicDescription = description

    def __repr__(self):
        return f'<Topic {self.TopicTitle}>'
