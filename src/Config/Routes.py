from ..Controller import *
from .Config import api


def Routes():
    api.add_resource(Alive, '/alive')
    api.add_resource(TimezoneAPI, '/timezone')
    api.add_namespace(product_ns, path="/api/products")
    api.add_namespace(user_ns, path="/api/users")


Routes()
