from init import db, ma, bcrypt, jwt
from flask import Flask
from controllers.cards_controller import cards_bp
from controllers.auth_controller import auth_bp
import os


  # Allows the models to connect

  # Create app will be picked up by flask automatically
def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(err):  # This is what covers if any 404 errors acur and will display the message in return
      return {'Error': str(err)}, 404 # str(err) lets the user see the error

    app.config ['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') # The os.environ gets the database from .env
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(cards_bp)
    app.register_blueprint(auth_bp)

    return app

