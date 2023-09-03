from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Order(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    is_open = db.Column(db.Boolean, default=False)
    order_items = db.relationship('OrderItem', backref='orderItem')
    
    def __repr__(self):
        return f'<order {self.id}>'
    
    def serialize(self):
        return {
            'user_id': self.user_id,
            'is_open': self.is_open,
            'order_items': [x.serialize() for x in self.order_items]
        }
        
class OrderItem(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    book_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    
    def __init__(self, book_id: int, quantity: int):
        self.book_id = book_id
        self.quantity = quantity
    

    
    def __repr__(self):
        return f'<order {self.id}>'
    
    def serialize(self):
        return {
            'book': self.book_id,
            'quantity': self.quantity,
        }