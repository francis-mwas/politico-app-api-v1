""" Global Imports """
from flask import Flask, Blueprint
from flask_restful import Api
from instance.config import app_config

""" Importing Blueprints """
from .admin import admin_blueprint as admn_blp

""" local module imports """
from .admin.admin import Party, GetSpecificParty, CreateOffice




""" creating an application instance """
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
   
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    """ Registering application blueprint for admin views"""
    admin = Api(admn_blp)
    app.register_blueprint(admn_blp, url_prefix='/api/v1')
   

    

    """ creating admin enpoints"""
    admin.add_resource(Party,'/parties')
    admin.add_resource(GetSpecificParty, '/parties/<int:id>')
    admin.add_resource(CreateOffice, '/offices')
    


    
    return app
