from ..Config import db


class User(db.Model):
    __tablename__ = "user"

    id_user = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    username = db.Column(db.Text())
    email = db.Column(db.Text())
    password = db.Column(db.Text())

    def __init__(self, **data):
        self.username = data["username"]
        self.email = data["email"]
        self.password = data["password"]
