from pathlib import Path

from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from dotenv import dotenv_values

from routes import blueprint as frontend_blueprint

config = dotenv_values(".env")
parent_dir = Path(__file__).parent

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = config['SECRET_KEY']
app.config['WTF_CSRF_SECRET_KEY'] = 'yLnLKAJ3UuK8cEqmNucvLAuusjY'
app.config['UPLOAD_FOLDER'] = 'static/images'
app.register_blueprint(frontend_blueprint)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_message = "Please login."
login_manager.login_view = 'frontend.login'

bootstrap = Bootstrap(app)

@login_manager.user_loader
def load_user(user_id):
    return None

if __name__ == '__main__':
    
    app.run(
        host=config['HOST'],
        port=config['FRONTENDAPP_PORT'],
        debug=None
        )