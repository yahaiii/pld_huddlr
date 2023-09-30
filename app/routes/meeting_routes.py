from flask import Blueprint, render_template, request
from models.meeting_model import Meeting
import datetime

meeting_routes = Blueprint('meeting_routes', __name__)

@meeting_routes.route('/', methods=['GET'])
def index():
    meetings = Meeting.query.all()
    return render_template('meeting/index.html', meetings=meetings)

@meeting_routes.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('meeting/create.html')

    if request.method == 'POST':
        meeting_name = request.form['meeting_name']
        meeting_description = request.form['meeting_description']
        meeting_start_date_time = datetime.datetime.strptime(request.form['meeting_start_date_time'], '%Y-%m-%dT%H:%M:%S')
        meeting_end_date_time = datetime.datetime.strptime(request.form['meeting_end_date_time'], '%Y-%m-%dT%H:%M:%S')
        meeting_location = request.form['meeting_location']

        meeting = Meeting(MeetingName=meeting_name, MeetingDescription=meeting_description, MeetingStartDateTime=meeting_start_date_time, MeetingEndDateTime=meeting_end_date_time, MeetingLocation=meeting_location)

        db.session.add(meeting)
        db.session.commit()

        return redirect(url_for('meeting_routes.index'))

@meeting_routes.route('/<int:meeting_id>/edit', methods=['GET', 'POST'])
def edit(meeting_id):
    meeting = Meeting.query.get(meeting_id)

    if request.method == 'GET':
        return render_template('meeting/edit.html', meeting=meeting)

    if request.method == 'POST':
        meeting.MeetingName = request.form['meeting_name']
        meeting.MeetingDescription = request.form['meeting_description']
        meeting.MeetingStartDateTime = datetime.datetime.strptime(request.form['meeting_start_date_time'], '%Y-%m-%dT%H:%M:%S')
        meeting.MeetingEndDateTime = datetime.datetime.strptime(request.form['meeting_end_date_time'], '%Y-%m-%dT%H:%M:%S')
        meeting.MeetingLocation = request.form['meeting_location']

        db.session.commit()

        return redirect(url_for('meeting_routes.index'))

@meeting_routes.route('/<int:meeting_id>/delete', methods=['POST'])
def delete(meeting_id):
    meeting = Meeting.query.get(meeting_id)

    db.session.delete(meeting)
    db.session.commit()

    return redirect(url_for('meeting_routes.index'))
