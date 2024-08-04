from flask import request
from flask_restx import Resource, Namespace, fields
from src.Config import db
from src.Models import Product
from src.Schema.ProductSchema import ProductSchema
from src.Helper import Timer

product_ns = Namespace('products', description='Product Operations')

product_post_model = product_ns.model('ProductPost', {
    'sku_code': fields.String(required=True, title="SKU Code", description="The SKU code for the product"),
    'name': fields.String(required=True, title="Product Name", description="The product name"),
    'category': fields.String(required=True, title="Product Category", description="The category of product"),
    'qty_in_store': fields.Integer(required=False, title="Quantity in store", description="Quantity of product in store")
})

product_patch_model = product_ns.model('ProductPatch', {
    'sku_code': fields.String(required=True, title="SKU Code", description="The SKU code for the product"),
    'qty_in_store': fields.Integer(required=True, title="Quantity in store", description="Quantity of product in store")
})


@product_ns.route("")
class ProductsController(Resource):
    @product_ns.expect(product_post_model)
    def post(self):
        """
        Create new product
        """
        body = request.get_json()
        new_product = Product(**body)
        try:
            db.session.add(new_product)
            db.session.commit()
            return {
                "status_code": 200,
                "message": "Data inserted"
            }, 200
        except Exception as e:
            db.session.rollback()
            return {
                "status_code": 400,
                "message": str(e)
            }, 400

    @product_ns.expect(product_patch_model)
    def patch(self):
        """
        update quantity in store fore product
        """
        body = request.get_json()
        product = Product.query.filter(Product.sku_code == body["sku_code"]).first()
        if product:
            product.qty_in_store = body["qty_in_store"]
            product.updated_at = Timer.get_current_date_time()
            db.session.commit()
            return {
                "status_code": 200,
                "message": "Data updated"
            }, 200
        else:
            return {
                "status_code": 404,
                "message": "Product is not found"
            }, 404

    @product_ns.param('page', 'Page number', required=True, type=int, default=1)
    @product_ns.param('per_page', 'Items per page', required=True, type=int, default=10)
    def get(self):
        """
        Get all product
        """
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        query = Product.query
        pagination = query.paginate(page=page, per_page=per_page)
        schema = ProductSchema(many=True)
        list_product = schema.dump(pagination)
        if len(list_product) > 0:
            return {
                "status_code": 200,
                "message": "Success",
                "data": list_product
            }, 200
        else:
            return {
                "status_code": 404,
                "message": "No product",
                "data": None
            }, 404


@product_ns.route("/<id>")
@product_ns.param('id', 'Id of product')
class ProductController(Resource):
    def get(self, id):
        query = Product.query.filter(Product.id == id).first()
        if query:
            schema = ProductSchema()
            product = schema.dump(query)
            return {
                "status_code": 200,
                "message": "Success",
                "data": product
            }, 200
        else:
            return {
                "status_code": 404,
                "message": "No product",
                "data": None
            }, 404
