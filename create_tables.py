from app import db
from flask_migrate import Migrate

# Import your models
from models.user_model import User
from models.meeting_model import Meeting
from models.notification_model import Notification
from models.availability_model import Availability
from models.meeting_invitees_model import MeetingInvitees

# Initialize Flask-Migrate
migrate = Migrate()

def create_tables():
    # Create all tables
    db.create_all()

if __name__ == '__main__':
    create_tables()
