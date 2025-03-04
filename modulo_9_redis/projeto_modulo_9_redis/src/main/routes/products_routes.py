from flask import Blueprint, jsonify

product_routes_bp = Blueprint("product_routes", __name__)

@product_routes_bp.route("/products", methods=["POST"])
def insert_product():
    return jsonify({"msg": "produto cadastrado"}), 200

@product_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name):
    return jsonify({"msg": f"produto {product_name}" }), 200
