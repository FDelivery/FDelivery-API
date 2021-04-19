from flask import request
from flask_restful import Resource, reqparse
from datetime import timedelta
from flask_jwt_extended import create_access_token
from database.models.BusinessUser import BusinessUser


class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('firstName', type=str, help='Name cannot be converted', required=True)
        args = parser.parse_args()
        # TODO : need to check that all parameters are correctly given
        body = request.get_json()
        #
        address_body = body.get('address')
        # address = Address()

        user = BusinessUser(**body)
        # user.address = Address(**address_body)
        user.hash_password()
        user.save()
        user_id = user.id
        return {'id': str(user_id)}, 200


class UserLogin(Resource):
    def get(self):
        body = request.get_json()
        user = BusinessUser.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401

        expires = timedelta(days=7)
        access_token = create_access_token(identity=user.id, expires_delta=expires)
        return {'token': access_token}, 200
