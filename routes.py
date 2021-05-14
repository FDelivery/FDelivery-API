from resources.UserAuth import Register, Login
from resources.deliveries import Deliveries
from resources.UsersList import UsersList, Users


def initialize_routes(api):
    api.add_resource(Users, '/api/v1/users/<string:user_id>')
    # users routs
    api.add_resource(UsersList, '/api/v1/users/')
    # api.add_resource(Users, '/api/v1/users/')
    # api.add_resource(Users, '/api/v1/users')

    api.add_resource(Register, '/api/v1/auth/register/')
    api.add_resource(Login, '/api/v1/auth/login/')

    api.add_resource(Deliveries, '/api/v1/deliveriesLogic/deliveries/')
    # api.add_resource
    # api.add_resource(Deliveries, '/api/courierLogic/delivers/')
    # api.add_resource(SpecificDeliver, '/api/courierLogic/deliver/<id>')
    # api.add_resource(couriers, '/api/courierLogic/couriers/')
