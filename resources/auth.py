import re

import mongoengine
from flask.wrappers import Response
from flask import request
from flask_restful import Resource
from datetime import timedelta
from flask_jwt_extended import create_access_token
from database.models.User import BusinessUser, CourierUser, User


class Register(Resource):
    def post(self):
        # TODO : need to check that all parameters are correctly given
        user: User
        body = request.get_json()
        role = body.get('role')

        if role == 'ADMIN':
            user = User(**body)
        elif role == 'COURIER':
            user = CourierUser(**body)
        elif role == 'BUSINESS':
            user = BusinessUser(**body)
        user.hash_password()
        try:
            user.save()
        except mongoengine.errors.NotUniqueError as exception:
            return str(exception), 400
            print
        return str(user.id), 200


class Login(Resource):
    def post(self):
        email = request.json.get('email')  # get email from post
        password = request.json.get('password')  # get password from post
        user = User.objects.get(email=email)  # retrieve user object from DB

        authorized = user.check_password(password=password)

        if authorized:
            expires = timedelta(days=7)
            access_token = create_access_token(user, expires_delta=expires)
            return str(access_token), 200
        # return str(user.id), 200

        return 'error: Email or password invalid', 401
