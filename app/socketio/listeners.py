

from app.socketio import socketio
from flask_socketio import join_room, leave_room


@socketio.on('join')
def register_delivery_room(b_id, sid):
    join_room(b_id, sid=sid)
    print(b_id, "has joined the room")


@socketio.on('leave')
def register_delivery_room(b_id, sid):
    leave_room(b_id, sid=sid)
    print(b_id, "has left the room")
