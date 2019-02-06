from flask_restful import Resource, reqparse

from ..models.models import User, users


"""creating classs user signup"""

class UserSignUp(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('firstname', type=str, required=True, help='This field is required')
    parser.add_argument('lastname', type=str, required=True, help='This field is required')
    parser.add_argument('othername', type=str, required=True, help='This field is required')
    parser.add_argument('email', type=str, required=True, help='this field is required')
    parser.add_argument('phoneNumber', type=str, required=True, help='This field is required')
    parser.add_argument('passportUrl', type=str, required=True, help='This field is required')
    parser.add_argument('isAdmin', type=str, required=True, help='this field is required')

    """ create user account """
    def post(self):
        user_data = UserSignUp().parser.parse_args()

        firstname = user_data['firstname']
        lastname = user_data['lastname']
        othername = user_data['othername']
        email = user_data['email']
        phoneNumber = user_data['phoneNumber']
        passportUrl  = user_data['passportUrl']
        isAdmin = user_data['isAdmin']


        user = User(firstname, lastname, othername, email,phoneNumber,passportUrl,bool(isAdmin))

        users.append(user)
        return {
            "status": 201,
            "Message": "Your account created successfully"
        }, 201



