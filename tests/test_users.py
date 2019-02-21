import json
from .base_test import BaseTest


class PoliticalOffice(BaseTest):

    def test_signin(self):
        """Testing user sign in."""
        
        self.create_account()
        response = self.user_login()

        self.assertEqual(response.status_code, 200)

    def test_user_email_exists(self):
        """testing user sign up."""

        user_data = {
            "national_id": "29805523",
            "firstname": "francis",
            "lastname": "mwangi",
            "othername": "fram",
            "email": "fram@gmail.com",
            "phoneNumber": "0710-445-862",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": False,
            "password": "mwas12345"
        }

        self.create_account()
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

        self.assertEqual(json.loads(response.data)[
                         "Message"], "This user already exist")

    def test_user_does_not_exist_sign_up(self):
        """test non existence user signin."""

        login_data = {
            "email": "john@gmail.com",
            "password": "john12345"
        }
        self.create_account()

        response = self.client.post(
            "api/v2/auth/login",
            data=json.dumps(login_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data)[
                         "message"], "The user not found, please register")

    def test_invalid_email(self):
        """test invalid user email registration."""

        user_data = {
            "national_id": "29805523",
            "firstname": "francis",
            "lastname": "mwangi",
            "othername": "fram",
            "email": "@@#mm@.com",
            "phoneNumber": "0717-445-862",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": False,
            "password": "mwas12345"
        }
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

        self.assertEqual(json.loads(response.data)[
                         "Message"], "Enter valid "
                         "email address with only one @ and one dot")

    def test_invalid_firstname(self):
        """test invalid firstname."""

        user_data = {
            "national_id": "29805523",
            "firstname": "%43*****mmm",
            "lastname": "mwangi",
            "othername": "fram",
            "email": "fram@gmail.com",
            "phoneNumber": "0717-445-862",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": False,
            "password": "mwas12345"
        }
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

        self.assertEqual(json.loads(response.data)[
                         "Message"], "Please enter a valid "
                         "firstname, with atleast characters")

    def test_invalid_lastname(self):
        """testing invalid lastname."""

        user_data = {
            "national_id": "29805523",
            "firstname": "john",
            "lastname": "88989098",
            "othername": "fram",
            "email": "fram@gmail.com",
            "phoneNumber": "0717-445-862",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": False,
            "password": "mwas12345"
        }
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

        self.assertEqual(json.loads(response.data)[
                         "Message"], "Firstname should be "
                         " atleast 3 characters and characters only")

    def test_invalid_othernames(self):
        """testing if othernames are valid."""

        user_data = {
            "national_id": "29805523",
            "firstname": "john",
            "lastname": "lastaname",
            "othername": "^hgf99",
            "email": "fram@gmail.com",
            "phoneNumber": "0717-445-862",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": False,
            "password": "mwas12345"
        }
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

        self.assertEqual(json.loads(response.data)[
                         "Message"], "Othername should "
                         "be atleast 3 characters and characters only")

    def test_invalid_phone_number(self):
        """test for invalid phone number."""

        user_data = {
            "national_id": "29805523",
            "firstname": "john",
            "lastname": "lastaname",
            "othername": "othernames",
            "email": "fram@gmail.com",
            "phoneNumber": "kk445-862ll",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": False,
            "password": "mwas12345"
        }
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

        self.assertEqual(json.loads(response.data)[
                         "Message"], "Phone number "
                         "should be atleast 10 characters")

    def test_invalid_url(self):
        """test for invalid passport url."""

        user_data = {
            "national_id": "29805523",
            "firstname": "john",
            "lastname": "lastaname",
            "othername": "othernames",
            "email": "fram@gmail.com",
            "phoneNumber": "0717-445-862",
            "passportUrl": "localhost.com/img1.png",
            "isAdmin": False,
            "password": "mwas12345"
        }
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

        self.assertEqual(json.loads(response.data)[
                         "Message"], "Enter valid "
                         "passport url ending with an image extension")

    def test_invalid_password(self):
        """test for invalid password."""

        user_data = {
            "national_id": "29805523",
            "firstname": "john","""  """
            "lastname": "lastaname",
            "othername": "othernames",
            "email": "fram@gmail.com",
            "phoneNumber": "0717-445-862",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": False,
            "password": "q5"
        }
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

        # self.assertEqual(json.loads(response.data)[
        #                  "Message"],"Password must be between 3 and 10 alphanumeric characters")


