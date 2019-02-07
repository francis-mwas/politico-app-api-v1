""" Global Imports """
from flask import Flask, Blueprint, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from instance.config import app_config

""" Importing Blueprints """
from .admin import admin_blueprint as admn_blp
from .auth import admin_blueprint as auth_blp

""" local module imports """
from .admin.admin import Party, GetSpecificParty, CreateOffice, GetSpecificOffice
from .auth.auth import UserSignUp, UserLogin

jwt = JWTManager()


""" creating an application instance """
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
   
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

 
    jwt.init_app(app)

    """ Registering application blueprint for views"""
    admin = Api(admn_blp)
    app.register_blueprint(admn_blp, url_prefix='/api/v1')
    auth = Api(auth_blp)
    app.register_blueprint(auth_blp, url_prefix='/api/v1')

    """ creating admin enpoints"""
    admin.add_resource(Party,'/parties')
    admin.add_resource(GetSpecificParty, '/parties/<int:id>')
    admin.add_resource(CreateOffice, '/offices')
    admin.add_resource(GetSpecificOffice, '/offices/<int:office_id>')

    auth.add_resource(UserSignUp, '/signup')
    auth.add_resource(UserLogin, '/signin')
    
    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify({
            "status": "error",
            "message": "Resource not found"
        }), 404

    return app
