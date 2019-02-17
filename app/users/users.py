from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.models import  Votes, Candidates, User, CreatePoliticalOffice


class CreateVote(Resource):
    """create vote."""

    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('office_id', type=int, 
        required=True, help='Please fill in this field')
    parser.add_argument('candidate_id', type=int, 
        required=True, help='Please fill in this field')
    
    @jwt_required
    def post(self):
        """create post vote method."""

        votes_data = CreateVote.parser.parse_args()

        office_id = votes_data["office_id"]
        candidate_id = votes_data["candidate_id"]

        current_user = get_jwt_identity()
        candidate = Candidates().get_candidate_by_id(candidate_id)

        if not candidate:
            return {"Message": "User not registered as a candidate", "status":404}, 404


        office = CreatePoliticalOffice().get_office_by_id(office_id)

        if not office:
            return{"Message": "Office not found", "status": 404},404
        
        voted_user = Votes().get_already_voted_users(current_user["user_id"])
        if voted_user:
            return {"message": "You have already voted for this candidate", "status":400},400
        
 

        vote = Votes(current_user["user_id"], office_id, candidate_id)
        vote.add_vote()

        return {
            "status": 201,
            "Message": "Your vote has been added successfully"
        }, 201



