from flask import request
from flask_restful import Resource, reqparse
from datetime import timedelta
from flask_jwt_extended import create_access_token
from database.models.User import BusinessUser, CourierUser, User


def register_admin(req: request):
    body = req.get_json()
    user = User(**body)
    user.hash_password()
    user.save()
    return {'id': str(user.id)}, 200


def register_business(req: request):
    body = req.get_json()
    user = BusinessUser(**body)
    user.hash_password()
    user.save()
    return {'id': str(user.id)}, 200


def register_courier(req: request):
    body = req.get_json()
    user = CourierUser(**body)
    user.hash_password()
    user.save()
    return {'id': str(user.id)}, 200


class Register(Resource):
    def post(self):
        # TODO : need to check that all parameters are correctly given
        print(request.data)
        role = request.json.get('role')
        print(role)
        if role == 'Admin':
            return register_admin(request)
        elif role == 'Courier':
            return register_courier(request)
        elif role == 'Business':
            return register_business(request)


class Login(Resource):
    def post(self):
        body = request.get_json()
        user = BusinessUser.objects.get()
        authorized = user.check_password(body.get())
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        expires = timedelta(days=7)
        access_token = create_access_token(user, expires_delta=expires)
        return {'token': access_token}, 200
