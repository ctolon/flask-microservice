from flask import Blueprint, Response
import services as dummy_service

blueprint = Blueprint('dummy_api_routes', __name__, url_prefix='/api/dummy')

@blueprint.route('', methods=['GET'])
def dummy() -> Response:
    return dummy_service.dummy()