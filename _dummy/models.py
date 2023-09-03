from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dummy(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    
    def __repr__(self):
        return f'<dummy {self.id}>'
    
    def serialize(self):
        return {
            'id': self.id,
        }