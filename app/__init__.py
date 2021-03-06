from flask import Flask
# from app.helpers.app_context import AppContext as AC
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

from .config import config_by_name

load_dotenv('.env')

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_name):
    """
    create_app   creates an instance of the flask app

    Args:
        config_object (string): config file

    """
    app = Flask(__name__)

    cors = CORS(app, support_credentials=True)
    # Load config profile
    app.config.from_object(config_by_name[config_name])

    # initiate plugins
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    return app