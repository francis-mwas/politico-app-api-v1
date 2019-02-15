import unittest
import json
from app import create_app
from manage import Tables


class BaseTest(unittest.TestCase):
    def setUp(self):

        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            Tables().drop_table()
            Tables().migrate()
            Tables().create_admin()

    def create_account(self):
        """testing user sign up."""

        user_data = {
            "firstname": "francis",
            "lastname": "mwangi",
            "othername": "fram",
            "email": "fram@gmail.com",
            "phoneNumber": "0717-445-862",
            "passportUrl": "http://localhost.com/img1.png",
            "isAdmin": 1,
            "password": "mwas12345"
        }
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        return response

    def user_login(self):
        """testing user login."""
        login_data = {
            "email": "fram@gmail.com",
            "password": "mwas12345"
        }
        response = self.client.post(
            "api/v2/auth/signin",
            data=json.dumps(login_data),
            headers={"content-type": "application/json"}
        )
        return response


    def generate_token(self):
        """test tokem generation after successful login."""

        self.create_account()

        response = self.user_login()

        token = json.loads(response.data).get("access_token", None)

        return token

    def create_party(self):
        "create a party method."

        access_token = self.generate_admin_token()
        party_data = {
            "name":"qwetyui",
            "hqAddress": "Nairobi",
            "logoUrl": "http://images.com/img1.png",
        }
        response = self.client.post(
            "api/v2/admin/parties",
            data=json.dumps(party_data),
            headers={'Content-type': 'application/json',
                     "Authorization": f"Bearer {access_token}"}

        )
        return response

    def create_office(self):
        """function to create office."""
        access_token = self.generate_admin_token()
        create_office_data = {
            "name":"sadfg",
            "Type": "federal"
        }
        response = self.client.post(
            "api/v2/admin/offices",
            data=json.dumps(create_office_data),
            headers = {'Content-type': 'application/json',
             "Authorization": f"Bearer {access_token}" }
        )
        return response

    def admin_login(self):
        data = {
            "email":"admin@gmail.com",
            "password":"12345"
        }

        response = self.client.post(
            "api/v2/auth/signin",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        return response

    def generate_admin_token(self):
        """test tokem generation after successful login."""

        response = self.admin_login()

        token = json.loads(response.data).get("access_token", None)

        return token
        

