from flask import request, jsonify
from flask_restx import Resource

from src.Config.Types import SALT_LOGIN
from src.Config.Core import decrypt_aes, check_bc, encrypt_bc
from src.Models import User
from src.Schema import UserSchemaList
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)


class UserLoginController(Resource):
    def post(self):
        """
        Login auth
        """
        body = request.get_json()
        """
                :data: the body json need to encrypted are
                {
                    username,
                    password
                }
                """
        validate_string = ["data"]
        if all(key in body for key in validate_string):
            data_decrypt = decrypt_aes(body["data"], SALT_LOGIN)
            query_user = User.query.filter(User.username == data_decrypt["username"])

            if query_user.count() == 0:
                return {
                    "status": 400,
                    "message": "The user data didn't exist.",
                }, 400

            if query_user.count() != 0:
                user: User = query_user.first()
                # check the password
                if check_bc(data_decrypt["password"], user.password):
                    access_token = create_access_token(identity=user.id_user)
                    refresh_token = create_refresh_token(identity=user.id_user)
                    return {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    }, 200
                else:
                    return {
                        "status": 401,
                        "message": "The email or password is wrong, check it again.",
                    }, 401
        else:
            return {
                "status": 400,
                "message": "Missing required field in body request.",
            }, 400


class UserRefreshTokenController(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return {"access_token": access_token}, 200
