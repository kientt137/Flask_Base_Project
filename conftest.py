import pytest
from sqlalchemy import create_engine
from flask_migrate import upgrade, migrate, stamp
from sqlalchemy_utils import database_exists, create_database
from src.Config import app, db


@pytest.fixture
def flask_app():
    # Database Config
    app.config['TESTING'] = True

    # Create the database if it doesn't exist
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)

    with app.app_context():
        yield app


@pytest.fixture
def client(flask_app):
    return flask_app.test_client()


@pytest.fixture
def init_database(flask_app):
    with flask_app.app_context():
        db.create_all()
        stamp(revision="head")
        migrate()
        upgrade()
        yield db
        db.session.remove()
        db.drop_all()
