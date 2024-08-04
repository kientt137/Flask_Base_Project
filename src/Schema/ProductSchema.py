from ..Config import ma
from ..Models import Product


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_fk = True
        exclude = ('created_at', 'updated_at')
