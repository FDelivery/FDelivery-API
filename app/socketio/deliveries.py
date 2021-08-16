from flask import session
from flask_socketio import emit

from app.socketio import socketio


@socketio.on('connect')
def charts_connect():
    print(session.get('sensor_name','sesion'),"Server says: A client has connected to charts")
    emit('my_response', {'data': 'Connected', 'count': 0})