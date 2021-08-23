from app import create_api
from app.database.db import initialize_db
from app.socketio import create_socketio, socketio
from app.utils.jwt_manger import initialize_jwt

# TODO: marshmallow validation of IO
# TODO: Generate Swagger


# Initialise restful api
app = create_api()

# Initialise flask-socketio
create_socketio(app)

# Initialise flask_mongoengine
initialize_db(app)

# Initialise flask_jwt_extended
initialize_jwt(app)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
