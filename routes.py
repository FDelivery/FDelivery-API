from resources.UserAuth import Register, Login
from resources.DeliveryLogic.deliveries import Deliveries
from resources.Users import Users


def initialize_routes(api):
    # users routs
    api.add_resource(Users, '/api/v1/users/')
    # api.add_resource(Users, '/api/v1/users/')
    # api.add_resource(Users, '/api/v1/users')

    api.add_resource(Register, '/api/v1/auth/register/')
    api.add_resource(Login, '/api/v1/auth/login/')

    api.add_resource(Deliveries, '/api/deliveriesLogic/deliveries/')
    # api.add_resource
    # api.add_resource(Deliveries, '/api/courierLogic/delivers/')
    # api.add_resource(SpecificDeliver, '/api/courierLogic/deliver/<id>')
    # api.add_resource(couriers, '/api/courierLogic/couriers/')
