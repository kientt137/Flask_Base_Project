from flask import request, jsonify, current_app
from flask_restx import Resource

from src.Config.Types import SALT_LOGIN
from src.Config import db
from src.Config.Core import decrypt_aes, check_bc, encrypt_bc
from src.Models import User
from src.Schema import UserSchemaList
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
)
import re
from src.Utils.Wrapper import body_validate


class UserLoginController(Resource):
    @jwt_required()
    @body_validate("data")
    def patch(self):
        """
        Update user password
        - Check current user is user want to change password
        - Check old password is correct
        - Check new password is different with current password
        - Check new password is valid
        """
        body = request.get_json()
        """
            :data: the body json need to encrypted are
            {
                password,
                old_password
            }
        """
        current_user_id = get_jwt_identity()
        data_decrypt = decrypt_aes(body["data"], SALT_LOGIN)
        # data_decrypt = body["data"]
        query_user = User.query.filter(User.id_user == current_user_id)

        if query_user.count() == 0:
            return {
               "status": 400,
               "message": "The user data didn't exist.",
            }, 400

        if query_user.count() != 0:
            user: User = query_user.first()
            # check the password
            if check_bc(data_decrypt["old_password"], user.password):
                # current password is correct, validate the new password
                if data_decrypt["password"] == data_decrypt["old_password"]:
                    return {
                        "status": 400,
                        "message": "The new password must be different from the old password.",
                    }, 400
                is_valid, reason = validate_password(data_decrypt["password"])
                if not is_valid:
                    return {
                        "status": 400,
                        "message": reason
                    }, 400
                # save the new password
                hashpw = encrypt_bc(data_decrypt['password'])
                # remove unused field
                data_update = {
                    "password": hashpw
                }
                query_user.update(data_update)
                db.session.commit()

                return {
                    "status": 201,
                    "message": "Update password successfully",
                }, 201

            else:
                return {
                    "status": 400,
                    "message": "The current password is wrong, check it again.",
                }, 400

    @body_validate("data")
    def post(self):
        body = request.get_json()
        """
            :data: the body json need to encrypted are
            {
                username,
                password
            }
        """

        data_decrypt = decrypt_aes(body["data"], SALT_LOGIN)
        # data_decrypt = body["data"]
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


class UserRefreshTokenController(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return {"access_token": access_token}, 200


def validate_password(password):
    # Minimum length
    if len(password) < current_app.config["PASSWORD_MINIMUM_LENGTH"]:
        return False, f"Password must be at least {current_app.config['PASSWORD_MINIMUM_LENGTH']} characters long."

    # Contains at least one lowercase letter
    if current_app.config["PASSWORD_MUST_CONTAIN_LOWER_CASE"] and not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."

    # Contains at least one uppercase letter
    if current_app.config["PASSWORD_MUST_CONTAIN_UPPER_CASE"] and not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."

    # Contains at least one digit
    if current_app.config["PASSWORD_MUST_CONTAIN_DIGIT"] and not re.search(r'\d', password):
        return False, "Password must contain at least one digit."

    # Contains at least one special character
    if current_app.config["PASSWORD_MUST_CONTAIN_SPECIAL_CHARACTER"] and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."

    return True, "Password is valid."
