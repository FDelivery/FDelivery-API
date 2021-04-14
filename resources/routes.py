from .Auth.businessUserAuth import UserRegister, UserLogin
from .DeliveryLogic.deliveries import Deliveries


def initialize_routes(api):
    # users routs
    api.add_resource(UserRegister, '/api/users/auth/register/')
    api.add_resource(UserLogin, '/api/users/auth/login/')

    api.add_resource(Deliveries, '/api/deliveriesLogic/deliveries/')
