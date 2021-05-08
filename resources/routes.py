from .Auth.UserAuth import Register, Login
from .DeliveryLogic.deliveries import Deliveries
from .Users import Users
from .courierLogic.couriers import *


def initialize_routes(api):
    # users routs
    api.add_resource(Users, '/api/v1/users/<string:user_id>')
    # api.add_resource(Users, '/api/v1/users/')
    # api.add_resource(Users, '/api/v1/users')

    api.add_resource(Register, '/api/v1/users/auth/register/')
    api.add_resource(Login, '/api/v1/users/auth/login/')

    api.add_resource(Deliveries, '/api/deliveriesLogic/deliveries/')
    # api.add_resource
    # api.add_resource(Deliveries, '/api/courierLogic/delivers/')
    # api.add_resource(SpecificDeliver, '/api/courierLogic/deliver/<id>')
    # api.add_resource(couriers, '/api/courierLogic/couriers/')
