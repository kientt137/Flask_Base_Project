from ..Config import db
from ..Utils import Timer


class User(db.Model):
    __tablename__ = "user"

    id_user = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    username = db.Column(db.Text())
    email = db.Column(db.Text())
    password = db.Column(db.Text())
    pw_update_at = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())

    def __init__(self, **data):
        self.username = data["username"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = Timer.get_current_date_time()
