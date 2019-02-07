from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import datetime
"""local imports"""
from ..models.models import User, users
from validations import validations


class UserSignUp(Resource):
    """creating classs user signup"""
    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('firstname', type=str, required=True,
                        help='This field is required')
    parser.add_argument('lastname', type=str, required=True,
                        help='This field is required')
    parser.add_argument('othername', type=str, required=True,
                        help='This field is required')
    parser.add_argument('email', type=str, required=True,
                        help='This field is required')
    parser.add_argument('phoneNumber', type=str,
                        required=True, help='This field is required')
    parser.add_argument('passportUrl', type=str,
                        required=True, help='This field is required')
    parser.add_argument('isAdmin', type=str, required=True,
                        help='This field is required')
    parser.add_argument('password', type=str, required=True,
                        help='This is field is required')

   
    def post(self):
        """ create user account """
        user_data = UserSignUp().parser.parse_args()

        firstname = user_data['firstname']
        lastname = user_data['lastname']
        othername = user_data['othername']
        email = user_data['email']
        phoneNumber = user_data['phoneNumber']
        passportUrl = user_data['passportUrl']
        isAdmin = user_data['isAdmin']
        password = user_data['password']

        """validate user data before submitting """
        validate_user_data = validations.Validations()

        if not validate_user_data.validate_input_fields(firstname):
            return {"status": 400, "Message": "Please enter a valid "
            "firstname, with atleast characters"}, 400
        if not validate_user_data.validate_input_fields(lastname):
            return {"status": 400, "Message": "Firstname should be "
            " atleast 3 characters and characters only"}, 400
        if not validate_user_data.validate_input_fields(othername):
            return {"status": 400, "Message": "Othername should "
            "be atleast 3 characters and characters only"}, 400
        if not validate_user_data.validate_email(email):
            return {"status": 400, "Message": "Enter valid "
            "email address with only one @ and one dot"}, 400
        if not validate_user_data.validate_phone_number(phoneNumber):
            return {"status": 400, "Message": "Phone number " 
            "should be atleast 10 characters"}, 400
        if not validate_user_data.validate_is_admin:
            return {"message": "Is admin field should have a range of"
            "between 0 and 1"}, 400

        if not validate_user_data.validate_url(passportUrl):
            return {"status": 400, "Message": "Enter valid "
            "passport url ending with an image extension"}, 400
        if not validate_user_data.validate_password(password):
            return {"status": 400, "Message": "Password must "
            "be between 3 and 10 alphanumeric characters"}, 400

       
        """ check if user already exists """
        user_exist = User().get_user_by_email(email)
        if user_exist:
            return {"status": 400, "Message": "This user already exist"}, 400

        user = User(firstname, lastname, othername, email,
                    phoneNumber, passportUrl, bool(isAdmin), password)

        users.append(user)
        return {
            "status": 201,
            "Message": "Your account created successfully"
        }, 201
    """ get all users """
    def get(self):
        return {"status": 200, "users":[user.serialize() for user in users ]}, 200

class UserLogin(Resource):
    """ user login """
    parser =reqparse.RequestParser()

    parser.add_argument('email', type=str, required=True, 
        help="The email field ir required to login")
    parser.add_argument('password', type=str, required=True,
        help="Password field cannot be empty")
    

    def post(self):
        login_data = UserLogin.parser.parse_args()

        email = login_data['email']
        password = login_data['password']

        validate_user_login = validations.Validations()

        if not validate_user_login.validate_email(email):
            return {"status": 400, "Message": "Please enter a valid email address"}, 400
        if not validate_user_login.validate_password(password):
            return {"status": 400, "Message": "Password should start with alphanumeric"
            "character and have length between 3 to 10 characters"}, 400
        
        """ check is user already registered"""
        user_exist = User().get_user_by_email(email)
        # import pdb; pdb.set_trace()
        # print(user_exist.pwhash)
        if user_exist:
            return {"Message": "Welcome, you have successfully logged in", 
            "status":200},
        return {"status": 404, "message": "The user is not found on this server"},404

        
