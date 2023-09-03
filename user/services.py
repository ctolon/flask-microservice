from flask import jsonify, request, make_response
from flask_login import login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

def get_all_users():
    all_user = User.query.all()
    result = [user.serialize() for user in all_user]
    response = {
        'message': 'List of all users',
        'result': result
    }
    return jsonify(response)

def create_user():
    try:
        user = User()
        user.username = request.form["username"]
        user.password = generate_password_hash(request.form["password"], method='sha256')
        
        db.session.add(user)
        db.session.commit()
        
        response = { "message": "User created successfully", "result": user.serialize() }
        return make_response(jsonify(response), 200)
    except Exception as e:
        print(str(e))
        response = { "message": "User not created successfully", "result": False }
        return make_response(jsonify(response), 401)

def login():
    
    username = request.form["username"]
    password = request.form["password"]
    
    user = User.query.filter_by(username=username).first()
    
    if not user:
        response ={ "message": "User not found" }
        return make_response(jsonify(response), 401)
    
    if get_current_user().get_json()["result"] is not None:
        response ={ "message": "User already logged in" }
        return make_response(jsonify(response), 401)
    
    if check_password_hash(user.password, password):
        user.update_api_key()
        db.session.commit()
        login_user(user)
        response = { "message": "User logged in successfully", "api_key":  user.api_key }
        return make_response(jsonify(response), 200)
        
    response ={ "message": "Access denied" }
    return make_response(jsonify(response), 401)

def logout():
    if current_user.is_authenticated:
        logout_user()
        return make_response(jsonify({ "message": "User logged out successfully" }), 200)
    
    return make_response(jsonify({ "message": "No user not logged in" }), 401)

def user_exists(username: str):
    user = User.query.filter_by(username=username).first()
    if user:
        return make_response(jsonify({"result": True, "message": "User exists"}), 200)
    return make_response(jsonify({"result": False, "message": "User not exists"}), 404)

def get_current_user():
    if current_user.is_authenticated:
        return make_response(jsonify({"result": current_user.serialize()}), 200)
    return make_response(jsonify({"result": None}), 404)
    
    