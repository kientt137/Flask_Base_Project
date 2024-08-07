from flask_restx import Resource
from src.Config.Helper import get_time_zone
from src.Config import logger
from src.Helper.Wrapper import jwt_verify


class Alive(Resource):
    def get(self):
        return "alive", 200


class TimezoneAPI(Resource):
    @jwt_verify()
    def get(self):
        logger.debug("TimezoneAPI calling")
        return get_time_zone(), 200
