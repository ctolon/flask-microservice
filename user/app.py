import base64
from pathlib import Path

from flask import Flask, g
from flask_migrate import Migrate
from flask_login import LoginManager
from flask.sessions import SecureCookieSessionInterface
from dotenv import dotenv_values

import models
from routes import blueprint as book_blueprint

config = dotenv_values(".env")
parent_dir = Path(__file__).parent
database_path = parent_dir / 'database'
db_name = "user"

def init_app(app: Flask):
    models.db.app = app
    models.db.init_app(app)

app = Flask(__name__)
app.config['SECRET_KEY'] = config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{database_path}/{db_name}.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_app(app)

app.register_blueprint(book_blueprint)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter_by(id=user_id).first()

@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.args.get('api_key')
    if api_key:
        user = models.User.query.filter_by(api_key=api_key).first()
        if user:
            return user
        
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        user = models.User.query.filter_by(api_key=api_key).first()
        if user:
            return user
        
    return None

class CustomSessionInterface(SecureCookieSessionInterface):
    """Prevent creating session from API requests."""
    
    def save_session(self, *args, **kwargs):
        if g.get('login_via_request'):
            return
        return super(CustomSessionInterface, self).save_session(*args,
                                                                **kwargs)

migrate = Migrate(app, models.db)

if __name__ == '__main__':
    
    app.run(
        host=config['HOST'],
        port=config['PORT'],
        debug=None
        )