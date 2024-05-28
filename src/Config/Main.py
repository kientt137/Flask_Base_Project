from flask import Flask, jsonify, render_template
from .Types import *
from datetime import timedelta


app                                          = Flask(__name__, template_folder='../Templates', static_folder='../Static')
app.config['SECRET_KEY']                     = SECRET_KEY
app.config["JWT_SECRET_KEY"]                 = JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"]       = timedelta(days=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"]      = timedelta(days=30)
app.config['CORS_HEADERS']                   = 'Content-Type'
app.config['CACHE_TYPE']                     = "redis"
app.config['CACHE_DEFAULT_TIMEOUT']          = 86400
app.config['CACHE_REDIS_URL']                = REDIS_CACHE_URL
app.config['SQLALCHEMY_DATABASE_URI']        = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 404 handling
@app.errorhandler(404)
def page_not_found(e):
    data = {
        "status": 404,
        "message": 'Not Found.'
    }

    return jsonify(data), 404
