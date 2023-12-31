from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Initialize Flask app
app = Flask(__name__)

# TODO
# remember to take out hardcoded config

# Load app configurations from config file
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql8649936:Fp3Ba9DYYl@sql8.freemysqlhosting.net:3306/sql8649936'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Import models
from .models.user_model import User
from .models.meeting_model import Meeting
from .models.notification_model import Notification
from .models.availability_model import Availability
from .models.meeting_invitees_model import MeetingInvitees
from .models.topic_model import Topic


# Import routes 
# from app.routes import user_routes

# Register the blueprint
# app.register_blueprint(user_routes)

# Import other necessary modules or setup here

# Create database tables (if needed)
with app.app_context():
    db.create_all()


