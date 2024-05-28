from flask_migrate import Migrate

from .Main import app

from flask_restx import Api
from flask_cors import CORS
from flask_caching import Cache
from flask_compress import Compress
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended.exceptions import NoAuthorizationError, WrongTokenError
from flask import jsonify
from jwt import InvalidSignatureError, ExpiredSignatureError
from src.Lib.CompressReponse import GzipCompress

# Compress(app)
GzipCompress(app)
api    = Api(app)
cors   = CORS(app, resources={r"/*": {"origins": "*"}}) # for cors in flask
caches = Cache(app)
db     = SQLAlchemy(app)
# add migrate
migrate = Migrate(app, db)
# flask db init flask db migrate -m "Initial migration." flask db upgrade
ma     = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


@api.errorhandler
def default_error_handler(error):
    status_code = getattr(error, 'status_code', 500)
    if isinstance(error, InvalidSignatureError) or isinstance(error, WrongTokenError):
        return {"message": "Signature verification failed.", "error": "invalid_token"}, 401
    elif isinstance(error, NoAuthorizationError):
        return {"message": "Request does not contain an access token.", "error": "authorization_required"}, 401
    elif isinstance(error, ExpiredSignatureError):
        return {"message": "The token has expired.", "error": "token_expired"}, 401
    # else:
    return {"message": str(error)}, status_code
