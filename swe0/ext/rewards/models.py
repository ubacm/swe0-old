from sqlalchemy.sql import func

from swe0 import db


class Transaction(db.Model):
    __tablename__ = 'rewards_transaction'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    amount = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=False)
