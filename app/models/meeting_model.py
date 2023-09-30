from app import db

class Meeting(db.Model):
    """Model for storing meeting details."""

    MeetingID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    MeetingName = db.Column(db.String(255), nullable=False)
    MeetingDescription = db.Column(db.String(255))
    MeetingStartDateTime = db.Column(db.DateTime, nullable=False)
    MeetingEndDateTime = db.Column(db.DateTime, nullable=False)
    MeetingLocation = db.Column(db.String(255))

    # Define a relationship with MeetingInvitees model
    meeting_invitees = db.relationship('MeetingInvitees', back_populates='meeting')

    def __repr__(self):
        return f'<Meeting {self.MeetingID}>'
