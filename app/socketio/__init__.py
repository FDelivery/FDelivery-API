from flask_socketio import SocketIO

socketio = SocketIO()


def create_socketio(app):
    from . import listeners
    from . import connection
    socketio.init_app(app)

    return app
