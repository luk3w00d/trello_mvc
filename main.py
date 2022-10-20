from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
  # Create app will be picked up by flask automatically
def create_app():
    app = Flask(__name__)
                                    # The os.environ gets the database from .env
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    db = SQLAlchemy(app)

    return app

