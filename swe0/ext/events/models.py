from swe0 import db


class Event(db.Model):
    __tablename__ = 'events_event'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.DateTime(timezone=True))
    end_time = db.Column(db.DateTime(timezone=True))
    check_in_enabled = db.Column(db.Boolean, server_default='0')
    check_in_code = db.Column(db.String(10), server_default='', nullable=False)
    check_in_rewards = db.Column(db.Integer, server_default='1')


class CheckIn(db.Model):
    __tablename__ = 'events_check_in'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True))
