from flask import request
from flask_restful import Resource, reqparse
from datetime import timedelta
from flask_jwt_extended import create_access_token
from database.models.User import BusinessUser, CourierUser, User


class Register(Resource):
    def post(self):
        # TODO : need to check that all parameters are correctly given
        user: User
        body = request.get_json()
        role = body.get('role')

        if role == 'Admin':
            user = User(**body)
        elif role == 'Courier':
            user = CourierUser(**body)
        elif role == 'Business':
            user = BusinessUser(**body)

        user.hash_password()
        user.save()
        return str(user.id), 200


class Login(Resource):
    def post(self):
        email = request.json.get('email')  # get email from post
        password = request.json.get('password')  # get password from post
        print(email, password)
        user = User.objects.get(email=email)  # retrieve user object from DB
        authorized = user.check_password(password=password)
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        expires = timedelta(days=7)
        access_token = create_access_token(user, expires_delta=expires)
        return {'token': access_token}, 200
