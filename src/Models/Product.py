from ..Config import db
from ..Helper import Timer


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    sku_code = db.Column(db.Text(), unique=True, nullable=False)
    name = db.Column(db.Text(), nullable=False)
    category = db.Column(db.Text(), nullable=False)
    qty_in_store = db.Column(db.BigInteger(), nullable=False)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())

    def __init__(self, **data):
        self.sku_code = data["sku_code"]
        self.name = data["name"]
        self.category = data["category"]
        self.qty_in_store = data.get("qty_in_store", 0)
        self.created_at = Timer.get_current_date_time()
