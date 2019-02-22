import json
from .base_test import BaseTest

class TestUsersViews(BaseTest):
  
  
    def test_voting_candidate_not_registered(self):
        """test candidate voting while not registered."""

        access_token = self.generate_admin_token()
        vote_data= {
            "office_id": 1,
            "candidate_id":2,
            "party_id": 2
        }
        res=self.client.post(
            "api/v2/users/votes",
            data=json.dumps(vote_data),
            headers={"content-type":"application/json",
            "Authorization": f"Bearer {access_token}"}
        )

        self.assertEqual(res.status_code, 404)


    
    def test_voting_candidate_none_existed_office(self):
        """testing for none existing office."""

        access_token = self.generate_admin_token()
        vote_data= {
            "office_id": 6,
            "candidate_id":2,
            "party_id": 2
        }
        res=self.client.post(
            "api/v2/users/votes",
            data=json.dumps(vote_data),
            headers={"content-type":"application/json",
            "Authorization": f"Bearer {access_token}"}
        )

        self.assertEqual(res.status_code, 404)
      
    def test_voting_candidate_none_existing_party(self):
        """test voting for none existing party."""

        access_token = self.generate_admin_token()
        vote_data= {
            "office_id": 6,
            "candidate_id":2,
            "party_id": 10
        }
        res=self.client.post(
            "api/v2/users/votes",
            data=json.dumps(vote_data),
            headers={"content-type":"application/json",
            "Authorization": f"Bearer {access_token}"}
        )

        self.assertEqual(res.status_code, 404)
   