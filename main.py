from db import db, ma
from flask import Flask
from controllers.cards_controller import cards_bp
import os


  # Allows the models to connect

  # Create app will be picked up by flask automatically
def create_app():
    app = Flask(__name__)
    
    app.config ['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') # The os.environ gets the database from .env
    
    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(cards_bp)

    return app

