from flask import Blueprint, Response
import services as order_service

blueprint = Blueprint('order_api_routes', __name__, url_prefix='/api/order')

@blueprint.route('', methods=['GET'])
def get_open_order() -> Response:
    return order_service.get_open_order()

@blueprint.route('/all', methods=['GET'])
def all_orders() -> Response:
    return order_service.all_orders()

@blueprint.route('/add-item', methods=['POST'])
def add_order_item() -> Response:
    return order_service.add_order_item()

@blueprint.route('/checkout', methods=['POST'])
def checkout() -> Response:
    return order_service.checkout()