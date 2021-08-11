from resources.auth import Register, Login
from resources.deliveries import DeliveriesList, Deliveries
from resources.users import UsersList, Users, User


def initialize_routes(api):
    # users routs
    api.add_resource(Users, '/api/v1/users/<string:user_id>')
    api.add_resource(UsersList, '/api/v1/users/')

    # Auth routs
    api.add_resource(Register, '/api/v1/auth/register/')
    api.add_resource(Login, '/api/v1/auth/login/')

    # delivery routs
    api.add_resource(Deliveries, '/api/v1/deliveriesRef/<string:delivery_id>/')
    api.add_resource(DeliveriesList, '/api/v1/deliveriesRef/')


    # api.add_resource
    # api.add_resource(Deliveries, '/api/courierLogic/delivers/')
    # api.add_resource(SpecificDeliver, '/api/courierLogic/deliver/<id>')
    # api.add_resource(couriers, '/api/courierLogic/couriers/')
