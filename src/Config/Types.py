import os
from flask.cli import load_dotenv

load_dotenv()

# App Config
SECRET_KEY = os.getenv('APP_SECRET_KEY')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
SALT_LOGIN = os.getenv('SALT_LOGIN')

# Database Config
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{dbUserName}:{dbPassword}@{dbHost}/{dbName}".format(
    dbUserName=os.getenv('POSTGRES_USER'),
    dbPassword=os.getenv('POSTGRES_PASSWORD'),
    dbHost=os.getenv('DBHOST'),
    dbName=os.getenv('POSTGRES_DB')
)

# redis url
REDIS_CACHE_URL = os.getenv('REDIS_CACHE_URL')

ENV = os.getenv('ENV')
SERVICE_NAME = os.getenv('SERVICE_NAME')
