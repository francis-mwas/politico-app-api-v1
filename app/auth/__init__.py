""" import blueprint from """
from flask import Blueprint
"""local imports"""
from .auth import UserSignUp

admin_blueprint = Blueprint('auth', __name__)

