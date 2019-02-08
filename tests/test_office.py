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
        """ Teardown """
        self.app_context.pop()



    def create_office(self):
        """ function to create office """
        create_office_data = {
            "name":"Office of the president",
            "Type": "federal"
        }
        response = self.client.post(
            "api/v1/admin/offices",
            data=json.dumps(create_office_data),
            headers = {'Content-type': 'application/json'}
        )
        return response
    # def test_office_creation(self):
    #     """ test office creation """
    #     response = self.create_office()
    #     print(response.data)
        
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(json.loads(response.data)[
    #                      "Message"], "New office created successfully")
    

    def test_office_creation_with_invalid_name(self):
        """test office creation with invalid data """
        office_data = {
            "name":"222222#@",
            "Type": "federal"
        }
        response = self.client.post(
            "api/v1/admin/offices",
            data=json.dumps(office_data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)[
                         "Message"], "Please enter valid office name")

    def test_office_creation_with_invalid_type(self):
        """ test office creation with invalid type """
        create_office = {
            "name":"Gubernatorial",
            "Type": "2222091"
        }
        response = self.client.post(
            "api/v1/admin/offices",
            data=json.dumps(create_office),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)[
                         "Message"], "Please enter valid office type")

    def test_fetching_a_single_office(self):
        """testing fetching a single office by id """
        self.create_office()
        response_data = self.client.get(
            "api/v1/admin/offices/2",
            headers ={"content-type": "application/json"}
        )
        # print(response_data)
        self.assertEqual(response_data.status_code, 200)
        
    
    
    def test_fetch_all_offices(self):
        """ test fetching all political offices """
        response_data = self.client.get(
            "api/v1/admin/offices",
             headers={"content-type":"application/json"}
        )
        self.assertEqual(response_data.status_code, 200)

    def test_office_does_not_exist(self):
        """ testing office does not exist """
        
        response = self.client.get(
            "api/v1/admin/office/200",
            headers = {"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 404)
        


    def test_edit_office(self):
        """ test editing a specific office """
        self.create_office()
        update_data = {
             "name":"Office of the president",
            "Type": "federal"
        }
      
        response=self.client.patch(
            "api/v1/admin/offices/2",
            data=json.dumps(update_data),
            headers={"content-type":"application/json"}
        )
        self.assertEqual(response.status_code, 200)
        

    