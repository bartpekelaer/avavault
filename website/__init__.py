import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
secret_key = os.getenv('AVAVAULT')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
