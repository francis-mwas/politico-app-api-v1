from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.models import Votes, Candidates, User, CreatePoliticalOffice, Parties
from validations import validations


class CreateVote(Resource):
    """create vote."""

    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('office_id', type=int,
                        required=True, help='Please fill in this field and must be an interger')
    parser.add_argument('candidate_id', type=int,
                        required=True, help='Please fill in this field')
    parser.add_argument('party_id', type=int, required=True,
                        help='please fill this field')

    @jwt_required
    def post(self):
        """create post vote method."""

        votes_data = CreateVote.parser.parse_args()

        office_id = votes_data["office_id"]
        candidate_id = votes_data["candidate_id"]
        party_id = votes_data['party_id']
        current_user = get_jwt_identity()

        candidate = Candidates().get_candidate_by_id(candidate_id)
        if not isinstance(office_id, int):
            return{"Message": "Must be an integer"},400
        if not isinstance(candidate_id, int):
            return{"Message": "Must be an integer"},400

        if not isinstance(party_id, int):
            return{"Message": "Must be an integer"},400



        if not candidate:
            return {"Message": "User not registered as a candidate", "status": 404}, 404

        office = CreatePoliticalOffice().get_office_by_id(office_id)

        if not office:
            return{"Message": "Office not found", "status": 404}, 404

        party = Parties().get_specific_party_by_id(party_id)
        if not party:
            return {"Status": 404, "Message": "Party not found"}, 404

        voted_user = Votes().get_already_voted_users(
            current_user["user_id"], office_id)       
        if voted_user:
            return {"message": "You have already voted for this office", "status": 400}, 400
        
       
        vote = Votes(current_user["user_id"],
                     office_id, candidate_id, party_id)
        vote.add_vote()

        return {
            "status": 201,
            "Message": "Your vote has been added successfully"
        }, 201


class GetVotes(Resource):

    @jwt_required
    def get(self, office_id, candidate_id):
        """ get votes"""

        if not isinstance(office_id, int):
            return {"status": 400, "Message": "office id must be an integer"}
        

        if not isinstance(candidate_id, int):
            return {"status": 400, "Message": "candidate id must be an integer"}
        

        votes = Votes().get_votes_for_a_specific_candidate(office_id, candidate_id)

        if votes:
            results = len(votes)
            return {
                "Votes":results, 
                "candidate_id":candidate_id,
                "office_id":office_id
            }
        else:
            return {"status": 404, "message": "There are no candidates available at the moment"}, 404


class GetAllCandidates(Resource):

    @jwt_required
    def get(self):
        """fetch all candidates parties."""
        candidates = Candidates().get_all_candidates()

        if candidates:
            return{"status": 200, "candidates": [candidate.serialize() for candidate in candidates]}, 200
        else:
            return {"status": 404, "message": "There are no candidates available at the moment"}, 404


class GetOfficeResults(Resource):

    @jwt_required
    def get(self, office_id):
        """fetch all office results """
        votes = Votes().get_votes_for_a_specific_office(office_id)

        return votes

       