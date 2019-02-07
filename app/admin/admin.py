""" Global iports """
from flask import Flask
from flask_restful import Resource, reqparse
""" local imports """
from ..models.models import parties,Parties, CreatePoliticalOffice, offices

from validations import validations


class Party(Resource):
    """ create class Parties """
    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('name', type=str, required=True,
         help='Please fill in this field')
    parser.add_argument('hqAddress', type=str, required=True,
         help='Please fill in this field')
    parser.add_argument('logoUrl', type=str, required=True,
         help='This field cant be empty')

    
    def post(self):
        """create post party method"""
        party_data = Party.parser.parse_args()

        name = party_data['name']
        hqAddress = party_data['hqAddress']
        logoUrl = party_data['logoUrl']

        validate_data = validations.Validations()

        """check to see if the input strings are valid"""
        if not validate_data.validate_input_fields(name):
            return {"status":400,"Message": "Please enter valid name"}, 400
        if not validate_data.validate_input_fields(hqAddress):
            return {"status":400,"Message": "Please enter valid headquarter name"}, 400
        if not validate_data.validate_url(logoUrl):
            return {"status":400, "Message": "Please enter a valid logo url"}, 400
         
        """ check of party exist """

        if Parties().get_party_by_name(name):
            return {"status": 400, "Message": "This party already exist"}, 400
        
            

         
        party = Parties(name,hqAddress,logoUrl)
        parties.append(party)
        if party:
            return {
                    "status":201,"Message": "Party reqistered successfully",
                    "party":party.serialize()
            }, 201
        return {"status": "400","Message": "Party not created"}, 400
             

  
    def get(self):
        """fetch all political parties """
        return{"status":200,"parties":[party.serialize() for party in parties]}


class GetSpecificParty(Resource):
    """get a specific political party by using id """
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, 
    help='Please fill in this field')
    parser.add_argument('hqAddress', type=str, required=True,
     help='Please fill in this field')
    parser.add_argument('logoUrl', type=str, required=True,
     help='This field cant be empty')
    
    
    def get(self, id):
        """ get a specific party by id """
        party = Parties().get_specific_party_by_id(id)
        if party:
            return {"party": party.serialize(),"status": 200}, 200

        return {"status": 404,"Message": "That party does not exist"}, 404
            

       

   
    def delete(self,id):
        """ delete a specific party """

        party = Parties().get_specific_party_by_id(id)

        if not party:
            return {"status": 404,"message": "this party does not exist"},404
        else:
            parties.remove(party)
            return {"status": 200,"Message": "party deleted successfully"}

   
    def patch(self, id):
        """ update specif party details """
        update_party =GetSpecificParty.parser.parse_args()
        name = update_party['name']
        hqAddress = update_party['hqAddress']
        logoUrl = update_party['logoUrl']

        validate_data = validations.Validations()

        """check to see if the input strings are valid"""
        if not validate_data.validate_input_fields(name):
            return {"status":400,"Message": "Please enter valid name"}, 400
        if not validate_data.validate_input_fields(hqAddress):
            return {"status":400,"Message": "Please enter valid "
            "headquarter name"}, 400
        if not validate_data.validate_url(logoUrl):
            return {"status":400, "Message": "Please enter a "
            "valid logo url"}, 400
     
        party = Parties().get_specific_party_by_id(id)
        if not party:
            return {
                "status": 404,
                "Message": "This party does not exist"
            }, 404
        else:
            party.name = name
            party.hqAddress = hqAddress
            party.logoUrl = logoUrl
            return {
                "message": "Party details updated successfully",
                "status": 200,
                "Party": party.serialize()
            }, 200
     





class CreateOffice(Resource):
    """ create office """
    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('name', type=str, 
        required=True, help='Please fill in this field')
    parser.add_argument('Type', type=str, 
        required=True, help='Please fill in this field')
    
    
    def post(self):
        """ create post office method """

        office_data = CreateOffice.parser.parse_args()

        name = office_data['name']
        Type = office_data['Type']

        """ validate office data before submiiting """
        validate_office_data = validations.Validations()


        if not validate_office_data.validate_input_fields(name):
            return {"status":400,"Message": "Please enter " 
            "valid office name"}, 400
        if not validate_office_data.validate_input_fields(Type):
            return {"status":400,"Message": 
            "Please enter valid office type"}, 400

        office_exist = CreatePoliticalOffice().get_office_by_name(name)
        if office_exist:
            return {"Status": 400, "Message": "Office name "
            "already exist"},400

        office = CreatePoliticalOffice(name, Type)
        offices.append(office)
        if office:
            return {"status":201,"Message": "New office "
            "created successfully", "Office": office.serializer()}, 201

    """ fetch all offices """
    def get(self):
        return {
            
            "status": 200,
            "Offices": [office.serializer() for office in offices]
        }
        
        
class GetSpecificOffice(Resource):
    """ get a specific political office by id """

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, 
    help='Please fill in this field')
    parser.add_argument('Type', type=str, required=True,
     help='Please fill in this field')
    
    def get(self, office_id):
  
        office = CreatePoliticalOffice().get_office_by_id(office_id)
        
        if office:
            return {"status": 200,"Office": office.serializer()}, 200
          
        else:
            return {"Status":400, "Message": "This office does not exist"}, 400
   
    def delete(self,office_id):
        """ delete a specific office """

        office = CreatePoliticalOffice().get_office_by_id(office_id)

        if not office:
            return {"status": 404,"message": "this party does not exist"},404
        else:
            offices.remove(office)
            return {"status": 200,"Message": "office deleted successfully"}

   
    def patch(self, office_id):
        """ update specif office details """
        update_office = GetSpecificOffice.parser.parse_args()
        name = update_office['name']
        Type = update_office['Type']
        

        validate_office_data = validations.Validations()
        """check to see if the input strings are valid"""
        if not validate_office_data.validate_input_fields(name):
            return {"status":400,"Message": "Please enter " 
            "valid office name"}, 400
        if not validate_office_data.validate_input_fields(Type):
            return {"status":400,"Message": 
            "Please enter valid office type"}, 400
     
        office = CreatePoliticalOffice().get_office_by_id(office_id)
        if not office:
            return {
                "status": 404,
                "Message": "Office does not exist"
            }, 404
        else:
            office.name = name
            office.Type = Type
            return {
                "message": "Office details updated successfully",
                "status": 200,
                "Party": office.serializer()
            }, 200
     
             
        
            

        


