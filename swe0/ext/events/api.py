from functools import wraps

from flask_login import current_user
from flask_restful import Resource, abort, fields, marshal

from . import events_api
from .models import Event


EVENT_FIELDS = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'location': fields.String,
    'start_time': fields.String,
    'end_time': fields.String,
}

EVENT_FIELDS_PRIVILEGED = {
    **EVENT_FIELDS,
    'check_in_enabled': fields.Boolean,
    'check_in_code': fields.String,
    'check_in_rewards': fields.Integer,
}


def marshal_events(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if current_user.is_authenticated and current_user.is_admin:
            return marshal(response, EVENT_FIELDS_PRIVILEGED)
        else:
            return marshal(response, EVENT_FIELDS)
    return wrapper


@events_api.resource('')
class EventsResource(Resource):
    @staticmethod
    @marshal_events
    def get():
        return Event.query.all()


@events_api.resource('/<int:event_id>')
class EventResource(Resource):
    @staticmethod
    @marshal_events
    def get(event_id):
        event = Event.query.get(event_id)
        if event is None:
            abort(404, message='Event with ID {} was not found.'.format(event_id))
        return event
