from flask_restful import Resource, abort, fields, marshal, marshal_with

from . import rewards_api
from .models import Transaction


transaction_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'timestamp': fields.String,
    'amount': fields.Integer,
    'comment': fields.String,
}


@rewards_api.resource('/emails/<email>')
class RewardsByEmailResource(Resource):
    @staticmethod
    def get(email):
        transactions = Transaction.query.filter_by(email=email).all()
        return {
            'balance': sum(transaction.amount for transaction in transactions),
            'transactions': marshal(transactions, transaction_fields),
        }


@rewards_api.resource('/transactions/<transaction_id>')
class RewardsByTransactionResource(Resource):
    @staticmethod
    @marshal_with(transaction_fields)
    def get(transaction_id):
        transaction = Transaction.query.get(transaction_id)
        if transaction is None:
            abort(404, message='Transaction with ID {} was not found.'.format(transaction_id))
        return transaction
