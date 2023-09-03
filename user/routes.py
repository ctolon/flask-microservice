from flask import Blueprint, Response
import services as user_service

blueprint = Blueprint('user_api_routes', __name__, url_prefix='/api/user')

@blueprint.route('/all', methods=['GET'])
def get_all_users() -> Response:
    return user_service.get_all_users()

@blueprint.route('/create', methods=['POST'])
def create_user() -> Response:
    return user_service.create_user()

@blueprint.route('/login', methods=['POST'])
def login():
    return user_service.login()

@blueprint.route('/logout', methods=['POST'])
def logout():
    return user_service.logout()

@blueprint.route('/exists/<username>', methods=['GET'])
def user_exists(username: str):
    return user_service.user_exists(username)

@blueprint.route('/get', methods=['GET'])
def get_current_user():
    return user_service.get_current_user()