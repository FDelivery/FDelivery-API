from resources.businessUser import BusinessUserSignUpApi, BusinessUserSignInApi

def initialize_routes(api):
    api.add_resource(BusinessUserSignUpApi, '/api/business/signup')
    api.add_resource(BusinessUserSignInApi, '/api/business/signin')
