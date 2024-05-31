from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from src.Config import db
from src.Config.Helper import get_time_zone
from src.Config import logger
from src.Utils.Wrapper import jwt_verify


class Alive(Resource):
    def get(self):
        return "alive", 200

class TimezoneAPI(Resource):
    @jwt_verify()
    def get(self):
        logger.debug("TimezoneAPI calling")
        return get_time_zone(), 200
