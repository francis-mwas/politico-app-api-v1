import json
from .base_test import BaseTest

class PoliticalOffice(BaseTest):

    def test_office_creation(self):
        """test office creation."""
        response = self.create_office()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)[
                         "Message"], "Office created successfully")

    def test_fetch_all_offices(self):
        """test fetching all political offices."""
        
        access_token = self.generate_token()
        self.create_office()
        response_data = self.client.get(
            "api/v1/admin/offices",

             headers={"content-type":"application/json",

             'Authorization': f'Bearer {access_token}'}
        )
        self.assertEqual(response_data.status_code, 200)

    def test_office_creation_with_invalid_name(self):
        """test office creation with invalid data."""
        access_token = self.generate_admin_token()
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
        """test office creation with invalid type."""
        access_token = self.generate_admin_token()
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
        """testing fetching a single office by id."""

        access_token = self.generate_token()
        self.create_office()
        response_data = self.client.get(
            "api/v1/admin/offices/1",
            headers ={'content-type': 'application/json',
            'Authorization': f'Bearer {access_token}' }
        )
        self.assertEqual(response_data.status_code, 200)
        
    def test_office_does_not_exist(self):
        """testing office does not exist."""
        access_token = self.generate_token()
        
        response = self.client.get(
            "api/v1/admin/office/200",
            headers = {"content-type": "application/json",
            "Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(response.status_code, 404)
        
    def test_edit_office(self):
        """test editing a specific office."""
        access_token = self.generate_admin_token()
        self.create_office()
        update_data = {
             "name":"Office of the president",
            "Type": "federal"
        }
        response=self.client.patch(
            "api/v1/admin/offices/1",
            data=json.dumps(update_data),
            headers={"content-type":"application/json",
            "Authorization": f"Bearer {access_token}"}
        )
      
        self.assertEqual(response.status_code, 200)
        
        

    