from flask import jsonify, request, make_response
from models import db, Book

def create_books():
    try:
        book = Book()
        book.name = request.form["name"]
        book.slug = request.form["slug"]
        book.image = request.form["image"]
        book.price = request.form["price"]

        db.session.add(book)
        db.session.commit()
        
        response = { "message": "Book created successfully", "result": book.serialize() }
        return make_response(jsonify(response), 200)
    except Exception as e:
        print(str(e))
        response = { "message": "Book not created successfully", "result": False }
        return make_response(jsonify(response), 401)
    
def get_all_books():
    all_books = Book.query.all()
    result =  [book.serialize() for book in all_books]
    response = { "result": result }
    return make_response(jsonify(response), 200)

def book_details(slug):
    book = Book.query.filter_by(slug=slug).first()
    if book:
        response = { "result": book.serialize() }
        return make_response(jsonify(response), 200)
    response = { "result": False }
    return make_response(jsonify(response), 401)
    