from flask_socketio import SocketIO

socketio = SocketIO()


def create_socketio(app):
    from . import deliveries

    socketio.init_app(app)

    return app
