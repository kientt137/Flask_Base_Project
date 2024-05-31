import functools
from flask import request, jsonify
from flask_jwt_extended import get_jwt, verify_jwt_in_request, get_jwt_identity
from jwt import ExpiredSignatureError

from src.Models import User


def body_validate(*required_keys):
    """
    Validate the body request must include required keys
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            body = request.get_json()
            missing_keys = [key for key in required_keys if key not in body]
            if missing_keys:
                return {
                    "status": 400,
                    "message": "Missing required field in body request.",
                }, 400
            return func(*args, **kwargs)
        return wrapper
    return decorator


def jwt_verify(refresh=False):
    # validate the jwt
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request(refresh=refresh)
            user_id = get_jwt_identity()
            claims = get_jwt()

            user = User.query.filter(User.id_user == user_id).first()

            if not user:
                return {
                    "status": 400,
                    "message": "The user data didn't exist.",
                }, 400
            print(user.pw_update_at.timestamp(), claims['iat'], flush=True)
            if user.pw_update_at is not None:
                if user.pw_update_at.timestamp() > claims['iat']:
                    # If the password was updated after the token was issued, raise an exception
                    raise ExpiredSignatureError()
            return func(*args, **kwargs)
        return wrapper

    return decorator
