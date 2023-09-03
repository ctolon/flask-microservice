from flask import Blueprint, Response
import services as book_service

blueprint = Blueprint('book_api_routes', __name__, url_prefix='/api/book')

@blueprint.route('/all', methods=['GET'])
def get_all_books() -> Response:
    return book_service.get_all_books()

@blueprint.route('/create', methods=['POST'])
def create_books() -> Response:
    return book_service.create_books()

@blueprint.route('/get/<slug>', methods=['GET'])
def book_details(slug: str):
    return book_service.book_details(slug)