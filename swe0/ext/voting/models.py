from swe0 import db
from swe0.auth.models import User
from swe0.ext.events.models import Event
from swe0.utils import foreign_key


categorization = db.Table(
    'voting_categorization',
    db.Column('category_id', db.Integer, db.ForeignKey('voting_category.id'), primary_key=True),
    db.Column('entry_id', db.Integer, db.ForeignKey('voting_entry.id'), primary_key=True),
)


class Category(db.Model):
    __tablename__ = 'voting_category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    event_id = db.Column(db.Integer, foreign_key(db, Event))
    is_accepting_entries = db.Column(db.Boolean, server_default='0')
    is_accepting_votes = db.Column(db.Boolean, server_default='0')

    event = db.relationship(
        Event, backref=db.backref('voting_categories', uselist=False))


class Entry(db.Model):
    __tablename__ = 'voting_entry'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    categories = db.relationship(Category, secondary=categorization, lazy='subquery', backref=db.backref('entries', lazy=True))
    _team_emails = db.Column('team_emails', db.String(200), nullable=False)

    @property
    def team_emails(self):
        return self._team_emails.split(', ')

    @team_emails.setter
    def team_emails(self, emails):
        if isinstance(emails, str):
            emails = (email.strip() for email in emails.split(','))
        self._team_emails = ', '.join(sorted(filter(None, emails)))


class Vote(db.Model):
    __tablename__ = 'voting_vote'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, foreign_key(db, User))
    category_id = db.Column(db.Integer, foreign_key(db, Category))
    entry_id = db.Column(db.Integer, foreign_key(db, Entry))

    user = db.relationship(User, backref='votes')
    category = db.relationship(Category, backref='votes')
    entry = db.relationship(Entry, backref='votes')
