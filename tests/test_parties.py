import unittest
import json

from app import create_app

class PoliticalParties(unittest.TestCase):

    def setUp(self):
        """ application testing configurations"""

        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """ setting teardown """
        self.app_context.pop()

    """test party creation """
    def test_party_creation(self):
        create_party_data = {
            "name":"odm",
            "hqAddress": "Nairobi",
            "logoUrl": "imgpng"
        }
        
        res= self.client.post(
            "api/v1/parties",
            data=json.dumps(create_party_data),
            headers={'content-type': 'application/json'}
        )
        return res
        
     
                

    """ test invalid party hqaddress while creating the party """
    def test_invalid_party_hqaddress(self):
        create_invalid_party_hqaddres = {
            "name":"jubilee",
            "hqAddress":"1234567890",
            "logoUrl":"img1.png"
        }
        res=self.client.post(
            "api/v1/parties",
            data=json.dumps(create_invalid_party_hqaddres),
            headers={"content-type":"application/json"}
        )
        self.assertEqual(res.status_code, 400)
        
                
    def test_invali_logo_url(self):
        invalid_logo_url = {
             "name":"jubilee",
            "hqAddress":"Niarobi",
            "logoUrl":"111111"
        }
        res = self.client.post(
            "api/v1/parties",
            data=json.dumps(invalid_logo_url),
            headers={"content-type":"application/json"}
        )
        self.assertEqual(res.status_code, 400)
       


    """ test invalid party name while creating the party """
    def test_invalid_party_data(self):
        create_invalid_party_name = {
            "name":"123",
            "hqAddress":"Niarobi",
            "logoUrl":"localhost/images/img1.png"
        }
        res=self.client.post(
            "api/v1/parties",
            data=json.dumps(create_invalid_party_name),
            headers={"content-type":"application/json"}
        )
        self.assertEqual(res.status_code, 400)
        
      


    

    
    
