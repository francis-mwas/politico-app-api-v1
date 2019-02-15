import json
from .base_test import BaseTest

class PoliticalParties(BaseTest):

    def test_party_creation(self):
        """test party creation."""

        response = self.create_party()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)[
                         "Message"], "Party reqistered successfully")


    def test_invalid_party_name(self):
        """test invalid party name while creating the party."""

        access_token = self.generate_admin_token()
        create_invalid_party_name = {
            "name":"123",
            "hqAddress":"Niarobi",
            "logoUrl":"localhost/images/img1.png"
        }
        res=self.client.post(
            "api/v2/admin/parties",
            data=json.dumps(create_invalid_party_name),
            headers={"content-type":"application/json",
            "Authorization": f"Bearer {access_token}"}
        )

        self.assertEqual(res.status_code, 400)
        self.assertEqual(json.loads(res.data)[
                         "Message"], "Please enter valid name")
 
        
    
    def test_invalid_party_hqaddress(self):
        """test invalid party hqaddress while creating the party."""

        access_token = self.generate_admin_token()
        create_invalid_party_hqaddres = {
            "name":"jubilee",
            "hqAddress":"1234567890",
            "logoUrl":"img1.png"
        }
        res=self.client.post(
            "api/v2/admin/parties",
            data=json.dumps(create_invalid_party_hqaddres),
            headers={"content-type":"application/json",
             "Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(res.status_code, 400)
        self.assertEqual(json.loads(res.data)[
                         "Message"], "Please enter valid headquarter name")
        
                
    def test_invali_logo_url(self):

        """test invalid logo url."""
        access_token = self.generate_admin_token()
        invalid_logo_url = {
                "name":"jubilee",
                "hqAddress":"Niarobi",
                "logoUrl":"111111"
        }
        res = self.client.post(
            "api/v2/admin/parties",
            data=json.dumps(invalid_logo_url),
            headers={"content-type":"application/json",
            "Authorization": f"Bearer {access_token}"}
            )
        self.assertEqual(res.status_code, 400)
        self.assertEqual(json.loads(res.data)[
                         "Message"], "Please enter a valid logo url")

    def test_fetching_a_single_party(self):
        """testing fetching a single party by id."""

        access_token = self.generate_token()
        self.create_party()
        response_data = self.client.get(
            "api/v2/admin/parties/1",
            headers ={"content-type": "application/json",
            "Authorization": f"Bearer {access_token}"}
        )
 
        self.assertEqual(response_data.status_code, 200)
        
    def test_fetch_all_parties(self):
        """test fetching all political parties."""

        self.create_party()
        access_token = self.generate_token()
        response_data = self.client.get(
            "api/v2/admin/parties",
             headers={"content-type":"application/json",
             "Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(response_data.status_code, 200)

    def test_party_does_not_exist(self):
        """testing party does not exist."""

        access_token = self.generate_token()
        response = self.client.get(
            "api/v2/admin/parties/200",
            headers = {"content-type": "application/json",
            "Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(response.status_code, 404)

    def test_edit_party(self):
        """test editing a specific party."""

        access_token = self.generate_admin_token()
        self.create_party()
        update_data = {
            "name":"kilimanjaro party",
            "hqAddress": "Nairobi",
            "logoUrl": "http://images.com/img1.png",
        }
        response=self.client.patch(
            "api/v2/admin/parties/1",
            data=json.dumps(update_data),
            headers={"content-type":"application/json",
             "Authorization": f"Bearer {access_token}" }
        )
  
        self.assertEqual(response.status_code, 200)
        


    
   
    

    
    
