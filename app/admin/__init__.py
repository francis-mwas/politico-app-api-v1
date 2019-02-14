""" import blueprint from """
from flask import Blueprint
"""local imports"""
from .admin import Parties

admin_blueprint = Blueprint('admin', __name__)

