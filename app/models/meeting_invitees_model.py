from app import db

class MeetingInvitees(db.Model):
    """Model for storing meeting attendees."""

    MeetingID = db.Column(db.Integer, db.ForeignKey('meeting.MeetingID'), primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), primary_key=True)
    
    # Acceptance status field
    AcceptanceStatus = db.Column(db.String(20), default='pending')  # 'accepted', 'declined', or 'pending'

    # Define relationships with Meeting and User models
    meeting = db.relationship('Meeting', back_populates='meeting_invitees')
    user = db.relationship('User', back_populates='meetings_invited_to')

    def __init__(self, meeting, user, acceptance_status='pending'):
        self.meeting = meeting
        self.user = user
        self.AcceptanceStatus = acceptance_status

    def __repr__(self):
        return f'<MeetingInvitees {self.MeetingID}, {self.UserID}>'
