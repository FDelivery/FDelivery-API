from flask import request
from database.models.BusinessUser import BusinessUser
from flask_restful import Resource
from datetime import timedelta
from flask_jwt_extended import create_access_token

class BusinessUserSignUpApi(Resource):
    def post(self):
        # TODO : need to check that all parameters are correctly given 
        body = request.get_json()
        user = BusinessUser(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id' : str(id)} , 200
    
class BusinessUserSignInApi(Resource):
    def get(self):
        body = request.get_json()
        user = BusinessUser.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        
        expires = timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200 

# @businessUsers.route('/api/users', methods=['GET'])
# def get_users():
#     businessUsers = BusinessUser.objects().to_json()
#     if not businessUsers:
#         return  {'error': 'data not found'}, 404
#     else:
#         return Response(businessUsers, mimetype="application/json", status=200)

# @businessUsers.route('/api/users', methods=['POST'])
# def add_user():
#    body = request.get_json()
#    user = BusinessUser(**body).save()
#    return jsonify(user), 200       


