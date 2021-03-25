from flask import Flask, request, Response
from database.db import initialize_db
from resources.businessUser import BusinessUserSignUpApi
from flask_restful import Api
from resources.routes import initialize_routes
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/api'
}

initialize_db(app)
initialize_routes(api)

# @app.route('/api/deliveries/<int:index>', methods=['GET'])
# def get_movie(index):
#     return jsonify(movies[index])


# @app.route('api/deliveries/<id>', methods=['PUT'])
# def update_movie(index):
#     body = request.get_json()
#     Delivery.objects.get(id=id).update(**body)
#     return 'Updated Delivery', 200

if __name__ == '__main__':
    app.run(debug=True)
