from flask import Blueprint, redirect, render_template, request, url_for
from models.notification_model import Notification
from config.database import db

notification_routes = Blueprint('notification_routes', __name__)

@notification_routes.route('/', methods=['GET'])
def index():
    notifications = Notification.query.all()
    return render_template('notification/index.html', notifications=notifications)

@notification_routes.route('/<int:notification_id>/mark-as-read', methods=['POST'])
def mark_as_read(notification_id):
    notification = Notification.query.get(notification_id)
    notification.IsRead = True
    db.session.commit()

    return redirect(url_for('notification_routes.index'))
