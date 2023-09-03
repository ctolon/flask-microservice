from flask import jsonify, request, make_response
from models import db, Dummy

def dummy():
    return make_response(jsonify({ "message": "Dummy" }), 200)
    