import functools
from flask import request, jsonify

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
