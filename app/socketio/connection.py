from app.socketio import socketio


@socketio.on('connect')
def connected():
    print("user connected")


@socketio.on('disconnect')
def disconnect():
    print("user disconnected")