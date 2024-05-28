from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from src.Config import db
from src.Config.Helper import get_time_zone


class Alive(Resource):
    def get(self):
        return "alive", 200

class TimezoneAPI(Resource):
    @jwt_required()
    def get(self):
        return get_time_zone(), 200
