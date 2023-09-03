from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Book(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return f'<book {self.id} {self.name}>'
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'price': self.price,
            'image': self.image
        }