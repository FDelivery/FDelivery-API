from flask import session, request
from flask_socketio import emit

from app.socketio import socketio
from flask_socketio import join_room


@socketio.on('join')
def register_delivery_room(b_id):
    join_room(b_id)
