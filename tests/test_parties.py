import unittest
import json

from app import create_app

class PoliticalParties(unittest.TestCase):

    def setUp(self):
        """application testing configurations."""

        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Teardown function."""
        self.app_context.pop()
        

    def create_account(self):
        """user sign up function."""

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
        """user login function."""
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
        """test tokem generation after successful login."""
        
        self.create_account()

        response = self.signin()

        token = json.loads(response.data).get("access_token", None)
      
        return token


    
    def create_party(self, name):
        "create a party."
        access_token = self.generate_token()
        party_data = {
            "name":name,
            "hqAddress": "Nairobi",
            "logoUrl": "http://images.com/img1.png",
        }
        response = self.client.post(
            "api/v1/admin/parties",
            data=json.dumps(party_data),
            headers = {'Content-type': 'application/json',
            "Authorization": f"Bearer {access_token}"}

        )
        return response

   
    def test_party_creation(self):
        """test party creation."""
        response = self.create_party('odm')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)[
                         "Message"], "Party reqistered successfully")


    def test_invalid_party_name(self):
        """test invalid party name while creating the party."""
        access_token = self.generate_token()

        create_invalid_party_name = {
            "name":"123",
            "hqAddress":"Niarobi",
            "logoUrl":"localhost/images/img1.png"
        }

        res=self.client.post(
            "api/v1/admin/parties",
            data=json.dumps(create_invalid_party_name),
            headers={"content-type":"application/json",
            "Authorization": f"Bearer {access_token}"}
        )

        self.assertEqual(res.status_code, 400)
        self.assertEqual(json.loads(res.data)[
                         "Message"], "Please enter valid name")
 
        
    
    def test_invalid_party_hqaddress(self):
        """test invalid party hqaddress while creating the party."""
        access_token = self.generate_token()
        create_invalid_party_hqaddres = {
            "name":"jubilee",
            "hqAddress":"1234567890",
            "logoUrl":"img1.png"
        }
        res=self.client.post(
            "api/v1/admin/parties",
            data=json.dumps(create_invalid_party_hqaddres),
            headers={"content-type":"application/json",
             "Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(res.status_code, 400)
        self.assertEqual(json.loads(res.data)[
                         "Message"], "Please enter valid headquarter name")
        
                
    def test_invali_logo_url(self):
        """test invalid logo url."""
        access_token = self.generate_token()
        invalid_logo_url = {
             "name":"jubilee",
            "hqAddress":"Niarobi",
            "logoUrl":"111111"
        }
        res = self.client.post(
            "api/v1/admin/parties",
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
        self.create_party('Kanu')
        response_data = self.client.get(
            "api/v1/admin/parties/2",
            headers ={"content-type": "application/json",
            "Authorization": f"Bearer {access_token}"}
        )
 
        self.assertEqual(response_data.status_code, 200)
        

    def test_fetch_all_parties(self):
        """test fetching all political parties."""
        access_token = self.generate_token()
        response_data = self.client.get(
            "api/v1/admin/parties",
             headers={"content-type":"application/json",
             "Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(response_data.status_code, 200)

    def test_party_does_not_exist(self):
        """testing party does not exist."""
        access_token = self.generate_token()
        response = self.client.get(
            "api/v1/admin/parties/200",
            headers = {"content-type": "application/json",
            "Authorization": f"Bearer {access_token}"}
        )
        self.assertEqual(response.status_code, 404)

    def test_edit_party(self):
        """test editing a specific party."""
        access_token = self.generate_token()
        self.create_party('Kanu')
        update_data = {
            "name":"kilimanjaro party",
            "hqAddress": "Nairobi",
            "logoUrl": "http://images.com/img1.png",
        }
        
        response=self.client.patch(
            "api/v1/admin/parties/2",
            data=json.dumps(update_data),
            headers={"content-type":"application/json",
             "Authorization": f"Bearer {access_token}" }
        )
  
        self.assertEqual(response.status_code, 200)

    
   
    

    
    
