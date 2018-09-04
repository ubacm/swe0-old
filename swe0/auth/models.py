from flask_login import UserMixin

from swe0 import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)  # Note: Slack's limit is 80 chars.
    is_admin = db.Column(db.Boolean, nullable=False, server_default='0')

    def __repr__(self):
        return '<User {}: {}>'.format(self.id, self.email)
