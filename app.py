from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt
from resources.jwt_manger import initialize_jwt
from routes import initialize_routes


# TODO: Generate Swagger
# TODO: Validate with flask-marshmallow see if you can generate swagger from it


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')

api = Api(app)
bcrypt = Bcrypt(app)


initialize_jwt(app)
initialize_db(app)


initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
