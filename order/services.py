from flask import Response, jsonify, request, make_response
import requests
from models import db, Order, OrderItem

USER_API_URL = "http://user-service:5000/api/user/get"

def get_user(api_key: str):
    headers = {
        'Authorization': api_key
    }

    response = requests.get(USER_API_URL, headers=headers)
    if response.status_code != 200:
        return {'message': 'Not Authorized'}

    user = response.json()
    return user


def checkout():
    api_key = request.headers.get('Authorization')
    if not api_key:
        return make_response(jsonify({'message': 'Not logged in'}), 401)
    response = get_user(api_key)
    if not response.get('result'):
        return make_response(jsonify({'message': 'Not logged in'}), 401)
    
    user = response.get('result')

    open_order = Order.query.filter_by(user_id=user["id"], is_open=1).first()

    if open_order:
        open_order.is_open = False
        db.session.add(open_order)
        db.session.commit()
        response = { "message": "Order checked out successfully", "result": open_order.serialize() }
        return make_response(jsonify(response), 200)
    else:
        response = { "message": "Open order not found" }
        return make_response(jsonify(response), 404)
    

def get_open_order():
    api_key = request.headers.get('Authorization')
    if not api_key:
        return make_response(jsonify({'message': 'Not logged in'}), 401)
    response = get_user(api_key)
    if not response.get('result'):
        return make_response(jsonify({'message': 'Not logged in'}), 401)
    
    user = response.get('result')
    
    open_order = Order.query.filter_by(user_id=user["id"], is_open=1).first()
    
    if open_order:
        response = { "message": "Open order found", "result": open_order.serialize() }
        return make_response(jsonify(response), 200)
    else:
        response = { "message": "Open order not found" }
        return make_response(jsonify(response), 404)

def all_orders():
    all_order = Order.query.all()
    result = [order.serialize() for order in all_order]
    response = { "message": "List of all orders", "result": result }
    return make_response(jsonify(response), 200)

def add_order_item():
    api_key = request.headers.get('Authorization')
    if not api_key:
        return make_response(jsonify({'message': 'Not logged in'}), 401)
    response = get_user(api_key)
    if not response.get('result'):
        return make_response(jsonify({'message': 'Not logged in'}), 401)
    
    user = response.get('result')
    book_id = int(request.form["book_id"])
    quantity = int(request.form["quantity"])
    user_id = user["id"]
    
    open_order = Order.query.filter_by(user_id=user_id, is_open=1).first()
    
    if not open_order:
        open_order = Order()
        open_order.is_open = True
        open_order.user_id = user_id
        
        order_item = OrderItem(book_id=book_id, quantity=quantity)
        open_order.order_items.append(order_item)
    else:
        found = False
        for item in open_order.order_items:
            if item.book_id == book_id:
                item.quantity += quantity
                found = True
                
        if not found:
            order_item = OrderItem(book_id=book_id, quantity=quantity)
            open_order.order_items.append(order_item)
            
    db.session.add(open_order)
    db.session.commit()
    
    response = { "message": "Order item added successfully", "result": open_order.serialize() }
    return make_response(jsonify(response), 200)