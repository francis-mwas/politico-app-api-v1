from functools import wraps
from flask_jwt_extended import get_jwt_identity
from ..models.models import User

def admin_access(fn):
    """ Protect admin endpoints from normal users"""
    @wraps(fn)
    def wrapper_function(*args, **kwargs):
        user = User().get_user_by_email(get_jwt_identity()["email"])
        if user.isAdmin !=True:
            return {'message': 'You must be an admin to acces this endpoint'}, 401
        return fn(*args, **kwargs)
    return wrapper_function
    
    