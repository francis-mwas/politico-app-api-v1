import unittest
import json

from app import create_app

class PoliticalOffice(unittest.TestCase):

    def setUp(self):
        """ application testing configurations"""

        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """ Teardown function"""
        self.app_context.pop()

    def create_account(self):
        """ user sign up function """

        user_data = {
            	"firstname": "francis",
                "lastname":"mwangi",
                "othername":"fram",
                "email":"mwas@gmail.com",
                "phoneNumber": "0717-445-862",
                "passportUrl": "http://localhost.com/img1.png",
                "isAdmin": 1,
                "password":"mwas12345"
        }
        response = self.client.post(
            "api/v1/auth/signup",
            data=json.dumps(user_data),
            headers={"content-type": "application/json"}
        )
        return response
    def signin(self):
        """ user login function """
        user_login_data = {
            "email": "mwas@gmail.com",
            "password": "mwas12345"
        }
        response = self.client.post(
            "api/v1/auth/signin",
            data=json.dumps(user_login_data),
            headers={"content-type": "application/json"}
        )
        return response

    def generate_token(self):
        """ test tokem generation after successful login """
        self.create_account()
        response = self.signin()
        token = json.loads(response.data).get("access_token", None)
        print(token)
        return token



    def create_office(self, name):
        """ function to create office """
        access_token = self.generate_token()
        create_office_data = {
            "name":name,
            "Type": "federal"
        }
        response = self.client.post(
            "api/v1/admin/offices",
            data=json.dumps(create_office_data),
            headers = {'Content-type': 'application/json',
             "Authorization": f"Bearer {access_token}" }
        )
        return response

    def test_office_creation(self):
        """ test office creation """
        response = self.create_office('Governor')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)[
                         "Message"], "New office created successfully")
    

    def test_office_creation_with_invalid_name(self):
        """test office creation with invalid data """
        access_token = self.generate_token()
        office_data = {
            "name":"222222#@",
            "Type": "federal"
        }
        response = self.client.post(
            "api/v1/admin/offices",
            data=json.dumps(office_data),
            headers={"content-type": "application/json",
             "Authorization": f"Bearer {access_token}" }
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)[
                         "Message"], "Please enter valid office name")

    def test_office_creation_with_invalid_type(self):
        """ test office creation with invalid type """
        access_token = self.generate_token()
        create_office = {
            "name":"Gubernatorial",
            "Type": "2222091"
        }
        response = self.client.post(
            "api/v1/admin/offices",
            data=json.dumps(create_office),
            headers={'content-type': 'application/json',
            "Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)[
                         "Message"], "Please enter valid office type")

    def test_fetching_a_single_office(self):
        """testing fetching a single office by id """

        access_token = self.generate_token()
        self.create_office('Office of the senator')

        response_data = self.client.get(
            "api/v1/admin/offices/2",
            headers ={'content-type': 'application/json',
            'Authorization': f'Bearer {access_token}' }
        )
        self.assertEqual(response_data.status_code, 200)
        
    
    
    def test_fetch_all_offices(self):
        """ test fetching all political offices """
        access_token = self.generate_token()
        response_data = self.client.get(
            "api/v1/admin/offices",
             headers={"content-type":"application/json",
             'Authorization': f'Bearer {access_token}'}
        )
        self.assertEqual(response_data.status_code, 200)

    def test_office_does_not_exist(self):
        """ testing office does not exist """
        access_token = self.generate_token()
        
        response = self.client.get(
            "api/v1/admin/office/200",
            headers = {"content-type": "application/json",
            "Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(response.status_code, 404)
        


    def test_edit_office(self):
        """ test editing a specific office """
        access_token = self.generate_token()
        self.create_office('Office governor')
        update_data = {
             "name":"Office of the president",
            "Type": "federal"
        }
        response=self.client.patch(
            "api/v1/admin/offices/2",
            data=json.dumps(update_data),
            headers={"content-type":"application/json",
            "Authorization": f"Bearer {access_token}"}
        )
      
        self.assertEqual(response.status_code, 200)
        

    