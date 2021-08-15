from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_socketio import SocketIO
from flask import Flask

from database.db import initialize_db
from resources.jwt_manger import initialize_jwt

socketIO = SocketIO()


def create_app(debug=False):
    app = Flask(__name__)
    app.config.from_envvar('ENV_FILE_LOCATION')

    api = Api(app)
    bcrypt = Bcrypt(app)

    initialize_jwt(app)
    initialize_db(app)
    from routes import initialize_routes
    initialize_routes(api)
    socketIO.init_app(app)
    return app
