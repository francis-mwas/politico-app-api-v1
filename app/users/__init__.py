""" import blueprint from """
from flask import Blueprint
"""local imports"""
from .users import CreateVote, GetVotes

user_blueprint = Blueprint('user', __name__)
