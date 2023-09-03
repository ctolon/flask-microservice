from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from dotenv import dotenv_values

import models
from routes import blueprint as order_blueprint

config = dotenv_values(".env")
parent_dir = Path(__file__).parent
database_path = parent_dir / 'database'
db_name = "order"

def init_app(app: Flask):
    models.db.app = app
    models.db.init_app(app)

app = Flask(__name__)
app.config['SECRET_KEY'] = config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{database_path}/{db_name}.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_app(app)

app.register_blueprint(order_blueprint)

migrate = Migrate(app, models.db)

if __name__ == '__main__':
    
    app.run(
        host=config['HOST'],
        port=config['PORT'],
        debug=None
        )