from flask_restful import Resource, abort, fields, marshal_with

from . import events_api
from .models import Event


event_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'location': fields.String,
    'start_time': fields.String,
    'end_time': fields.String,
}


@events_api.resource('')
class EventsResource(Resource):
    @staticmethod
    @marshal_with(event_fields)
    def get():
        return Event.query.all()


@events_api.resource('/<int:event_id>')
class EventResource(Resource):
    @staticmethod
    @marshal_with(event_fields)
    def get(event_id):
        event = Event.query.get(event_id)
        if event is None:
            abort(404, message='Event with ID {} was not found.'.format(event_id))
        return event
