from ..Controller import *
from .Config import api


def Routes(api):
    api.add_resource(Alive, '/alive')
    api.add_resource(TimezoneAPI, '/timezone')
    api.add_resource(UserLoginController, '/login')
    api.add_resource(UserRefreshTokenController, '/refresh_token')
    api.add_resource(UserRegisterController, '/register')
Routes(api)
