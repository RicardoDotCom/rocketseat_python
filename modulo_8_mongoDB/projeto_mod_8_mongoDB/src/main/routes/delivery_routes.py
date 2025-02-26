from flask import Blueprint, jsonify, request
from src.main.http_types.http_resquest import HttpResquest
from src.main.http_types.http_response import HttpResponse

delivery_routes_bp = Blueprint("delivery_routes", __name__)

@delivery_routes_bp.route("/delivery/order", methods=["POST"])
def registry_order():
    print(request.json)
    http_request = HttpResquest(body=request.json)


    return jsonify({ "ola": "mundo" }), 200