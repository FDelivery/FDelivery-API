from .Auth.UserAuth import UserRegister, UserLogin
from .DeliveryLogic.deliveries import Deliveries
from .Users import Users


def initialize_routes(api):
    # users routs
    api.add_resource(Users, '/api/v1/users/<string:user_id>')
    api.add_resource(UserRegister, '/api/v1/users/auth/register/')
    api.add_resource(UserLogin, '/api/v1/users/auth/login/')

    api.add_resource(Deliveries, '/api/deliveriesLogic/deliveries/')
    # api.add_resource