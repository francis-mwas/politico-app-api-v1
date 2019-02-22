"""Global Imports."""

from flask import Flask, Blueprint, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from instance.config import app_config

"""Importing Blueprints."""

from .admin import admin_blueprint as admn_blp
from .auth import admin_blueprint as auth_blp
from .users import user_blueprint as user_blp

"""local module imports."""

from .admin.admin import Party, GetSpecificParty, CreateOffice, GetSpecificOffice, GetPartyByName, GetOfficeByName, RegisterCandidate, GetAllUsers
from .auth.auth import UserSignUp, UserLogin
from .users.users import CreateVote, GetVotes, GetAllCandidates, GetOfficeResults

jwt = JWTManager()


def create_app(config_name):
    """creating an application instance."""

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    jwt.init_app(app)

    """Registering application blueprint for views."""

    admin = Api(admn_blp)
    app.register_blueprint(admn_blp, url_prefix='/api/v2/admin')
    auth = Api(auth_blp)
    app.register_blueprint(auth_blp, url_prefix='/api/v2/auth')
    user = Api(user_blp)
    app.register_blueprint(user_blp,url_prefix='/api/v2/users')


    """creating admin enpoints."""
    admin.add_resource(Party, '/parties')
    admin.add_resource(GetAllUsers, '/users')
    admin.add_resource(GetSpecificParty, '/parties/<int:id>')
    admin.add_resource(GetPartyByName, '/parties/<string:name>')
    admin.add_resource(CreateOffice, '/offices')
    admin.add_resource(GetSpecificOffice, '/offices/<int:office_id>')
    admin.add_resource(GetOfficeByName, '/offices/<string:name>')
    admin.add_resource(RegisterCandidate, '/office/<int:office_id>/register')

    """Auth endpoints"""
    auth.add_resource(UserSignUp, '/signup')
    auth.add_resource(UserLogin, '/login')

    """user endpoints"""
    user.add_resource(CreateVote, '/votes')
    user.add_resource(GetVotes, '/office/<int:office_id>/<int:candidate_id>/result')
    user.add_resource(GetAllCandidates, '/candidates')
    user.add_resource(GetOfficeResults, '/offices/<int:office_id>')

    
    @app.errorhandler(400)
    def handle_bad_request(e):
        return jsonify({
            "status": "400",
            "Message": "bad request"
         }), 400
    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify({
            "status": "404",
            "message": "The url you requested does not exist, please enter a valid url"
            "for example: https://politico-app-api-v1.herokuapp.com/api/v1/admin/parties"
        }), 404
    
    return app
    
