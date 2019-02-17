""" Global iports."""
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
"""local imports."""
from ..models.models import  Parties, CreatePoliticalOffice,Candidates, User,GetUsers
from .is_admin import admin_access

from validations import validations

class Party(Resource):
    """ create class Parties."""

    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('name', type=str, required=True,
         help='Please fill in this field')
    parser.add_argument('hqAddress', type=str, required=True,
         help='Please fill in this field')
    parser.add_argument('logoUrl', type=str, required=True,
         help='This field cant be empty')

    @jwt_required
    @admin_access
    def post(self):
        """create post party method."""

        party_data = Party.parser.parse_args()

        name = party_data['name']
        hqAddress = party_data['hqAddress']
        logoUrl = party_data['logoUrl']

        validate_data = validations.Validations()

        """check to see if the input strings are valid."""
        if not validate_data.validate_input_fields(name):
            return {"status":400,"Message": "Please enter valid name"}, 400
        if not validate_data.validate_input_fields(hqAddress):
            return {"status":400,"Message": "Please enter valid headquarter name"}, 400
        if not validate_data.validate_url(logoUrl):
            return {"status":400, "Message": "Please enter a valid logo url"}, 400
       

        if Parties().get_party_by_name(name):
            """check of party exist."""

            return {"status": 400, "Message": "This party already exist"}, 400
         
        party = Parties(name,hqAddress,logoUrl)
        party.create_party()
        
        if party:
            return {
                    "status": 201, "Message": "Party reqistered successfully"
            }, 201
        return {"status": "400","Message": "Party not created"}, 400
             

    @jwt_required
    def get(self):
        """fetch all political parties."""

        parties = Parties().get_all_parties()
        if parties:
            return{"status":200,"parties":[party.serialize() for party in parties]},200
        else:
            return {"status": 404, "message": "There are no parties available at the moment"},404
    

class GetSpecificParty(Resource):
    """get a specific political party by using id."""

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, 
    help='Please fill in this field')
    parser.add_argument('hqAddress', type=str, required=True,
     help='Please fill in this field')
    parser.add_argument('logoUrl', type=str, required=True,
     help='This field cant be empty')
    
    @jwt_required
    def get(self, id):
        """ get a specific party by id."""

        party = Parties().get_specific_party_by_id(id)
        if party:
            return {"party": party.serialize(),"status": 200}, 200

        return {"status": 404,"Message": "That party does not exist"}, 404
            
    @jwt_required
    @admin_access
    def delete(self,id):
        """ delete a specific party."""

        party = Parties().get_specific_party_by_id(id)
        print(party)

        if not party:
            return {"status": 404,"message": "this party does not exist"},404
        else:
            Parties().delete_party(id)
            return {"status": 200,"Message": "party deleted successfully"}

    @jwt_required
    @admin_access
    def patch(self, id):
        """ update specif party details."""

        update_party =GetSpecificParty.parser.parse_args()
        name = update_party['name']
        hqAddress = update_party['hqAddress']
        logoUrl = update_party['logoUrl']

        validate_data = validations.Validations()

        """check to see if the input strings are valid."""
        if not validate_data.validate_input_fields(name):
            return {"status":400,"Message": "Please enter valid name"}, 400
        if not validate_data.validate_input_fields(hqAddress):
            return {"status":400,"Message": "Please enter valid "
            "headquarter name"}, 400
        if not validate_data.validate_url(logoUrl):
            return {"status":400, "Message": "Please enter a "
            "valid logo url"}, 400
     
        if Parties().get_specific_party_by_id(id):
            party = Parties(name, hqAddress, logoUrl)
            party.update_party(id)
            return{"Message": "party details updated", "status": 200}, 200
        return {"Message": "party does not exist", "status": 404}, 404    


class GetPartyByName(Resource):

    def get(self, name):
        """get a party by name."""

        party = Parties().get_party_by_name(name)
        print(party)
        if party:
            return {"Message": party.serialize(), "status": 200},200
        return{"Message": "party name does not exists"},400


class CreateOffice(Resource):
    """create office."""

    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('name', type=str, 
        required=True, help='Please fill in this field')
    parser.add_argument('Type', type=str, 
        required=True, help='Please fill in this field')
    
    @jwt_required
    @admin_access
    def post(self):
        """create post office method."""

        office_data = CreateOffice.parser.parse_args()

        name = office_data['name']
        Type = office_data['Type']

        """validate office data before submiiting."""
        validate_office_data = validations.Validations()


        if not validate_office_data.validate_input_fields(name):
            return {"status":400,"Message": "Please enter " 
            "valid office name"}, 400
        if not validate_office_data.validate_input_fields(Type):
            return {"status":400,"Message": 
            "Please enter valid office type"}, 400

        office = CreatePoliticalOffice().get_office_by_type(Type)
        if office:
            return {"Status": 400, "Message": "Office name "
            "already exist"},400

        office = CreatePoliticalOffice(Type,name)
        office.create_office()
        return {
            "status": 201,
            "Message": "Office created successfully"
        }, 201

    @jwt_required
    def get(self):
        """fetch all offices."""
    
        offices =CreatePoliticalOffice().fetch_all_offices()
        if offices:
            return {
                    "status": 200,
                    "Offices": [office.serializer() for office in offices]
            }
        return {"Message": "There are no offices available", "status": 404},404


class GetSpecificOffice(Resource):
    """get a specific political office by id."""

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, 
    help='Please fill in this field')
    parser.add_argument('Type', type=str, required=True,
     help='Please fill in this field')
    
    @jwt_required
    def get(self, office_id):
        """fetch a specific office data."""
  
        office = CreatePoliticalOffice().get_office_by_id(office_id)
        
        if office:
            return {"status": 200,"Office": office.serializer()}, 200
          
        else:
            return {"Status":400, "Message": "This office does not exist"}, 400

    @jwt_required
    @admin_access
    def delete(self,office_id):
        """delete a specific office."""

        office = CreatePoliticalOffice().get_office_by_id(office_id)

        if not office:
            return {"status": 404,"message": "this office does not exist"},404
        else:
            CreatePoliticalOffice().delete_office(office_id)
            return {"status": 200,"Message": "office deleted successfully"}

    @jwt_required
    @admin_access
    def patch(self, office_id):
        """ update a specif office details."""

        update_office = GetSpecificOffice.parser.parse_args()
        name = update_office['name']
        Type = update_office['Type']
        

        validate_office_data = validations.Validations()
        """check to see if the input strings are valid."""

        if not validate_office_data.validate_input_fields(name):
            return {"status":400,"Message": "Please enter." 
            "valid office name"}, 400
        if not validate_office_data.validate_input_fields(Type):
            return {"status":400,"Message": 
            "Please enter valid office type"}, 400
     
        if CreatePoliticalOffice().get_office_by_id(office_id):

            office =CreatePoliticalOffice(Type,name)
            office.update_office(office_id)
            return{"Message": "party details updated", "status": 200}, 200
        return {
                "status": 404,
                "Message": "Office does not exist"
            }, 404 

class GetOfficeByName(Resource):
    
    def get(self, name):
        """get office by name."""

        office = CreatePoliticalOffice().get_office_by_type(name)
        if office:
            return {"Office": office.serializer(), "status": 200}
        return {"Message": "This is office does not exist", "status":404},404

class RegisterCandidate(Resource):

    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('party_id', type=int, 
         required=True, help='Please fill in this field')
    parser.add_argument('candidate_id', type=int, 
          required=True, help='Please fill in this field')
        
    @jwt_required
    @admin_access
    def post(self, office_id):
        """create post party method."""

        data = RegisterCandidate.parser.parse_args()
        party_id = data['party_id']
        candidate_id = data['candidate_id']
    
        # validate_data = validations.Validations()

        # """check to see if the input strings are valid."""
        # if not validate_data.validate_ids(office_id):
        #         return {"status":400,"Message": "office id must be a number"}, 400
        # if not validate_data.validate_ids(party_id):
        #         return {"status":400,"Message": "party id must be a number"}, 400
        # if not validate_data.validate_ids(candidate_id):
        #         return {"status":400, "Message": "user id must be a number"}, 400

        user = User().get_user_by_id(candidate_id)

        if not user:
            return {"Status": 404, "Message":" user not found"}, 404

        party = Parties().get_specific_party_by_id(party_id)

        if not party:
            return {"Status": 404, "Message":" party does not exist"}, 404

        candidate = Candidates().get_candidate_by_id(candidate_id)

        if candidate:
            return {"Status": 400, "Message": "candidate already registered"},400

        candidate = Candidates(office_id,party_id, user.user_id)
        candidate.register_candidates()
        return {
            "status": 201,
            "Message": "Candidate registered successfully"
        }, 201



class GetAllUsers(Resource):

    @jwt_required
    @admin_access
    def get(self):
        """fetch all users."""
    
        users =GetUsers().fetch_all_users()
        if users:
            return {
                    "status": 200,
                    "Users": [user.serialize() for user in users]
            }
        return {"Message": "There are no users available", "status": 404},404



        


