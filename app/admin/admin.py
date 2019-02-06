""" Global iports """
from flask import Flask
from flask_restful import Resource, reqparse
""" local imports """
from ..models.models import parties,Parties, CreatePoliticalOffice, offices

""" create class Parties """
class Party(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('name', type=str, required=True, help='Please fill in this field')
    parser.add_argument('hqAddress', type=str, required=True, help='Please fill in this field')
    parser.add_argument('logoUrl', type=str, required=True, help='This field cant be empty')

    """create post party method"""
    def post(self):
         party_data = Party.parser.parse_args()

         name = party_data['name']
         hqAddress = party_data['hqAddress']
         logoUrl = party_data['logoUrl']

         """ check if party name is valid """
         if name.isdigit():
             return{
                 "status":400,
                 "Message": "Invalid party name, name must be characters only"
                 }, 400

         if hqAddress.isdigit():
             return {
                 "status":400,
                 "Message": "Invalid party hqAddress, it must be characters only"
                 }, 400

         """ check to see if the logo url is a string only"""
         if logoUrl.isdigit():
            return{
                "status":400,
                "Message": "Invalid logo url, it must be characters only"
                }, 400


         """ check if party already exists before creation """
         if Parties().get_party_by_name(name):
            return {
                "status": 400,
                "Message": "This party already exists"
                }, 400

         party = Parties(name,hqAddress,logoUrl)
         parties.append(party)
         if party:
                 return {
                     "status":201,
                     "Message": "Party reqistered successfully"
                     }, 201
         return {
             "status": "400",
             "Message": "Party not created"}, 400
             

    """fetch all political parties """
    def get(self):
        return{
            "status":200,
            "parties":[party.serialize() for party in parties]
        }
"""get a specific political party by using id """
class GetSpecificParty(Resource):
    def get(self, id):
        party = Parties().get_specifi_party_by_id(id)
        if not party:
            return {
                "status": 400,
                "Message": "That party does not exist"
                }, 400

        return {
            "party": party.serialize(),
            "status": 200
            }, 200

""" create office """
class CreateOffice(Resource):

    parser = reqparse.RequestParser(bundle_errors=True)

    parser.add_argument('name', type=str, required=True, help='Please fill in this field')
    parser.add_argument('Type', type=str, required=True, help='Please fill in this field')
    
    """ create post office method """
    def post(self):

        office_data = CreateOffice.parser.parse_args()

        name = office_data['name']
        Type = office_data['Type']

        """check if office name is valid """
        if name.isdigit():
             return{
                 "status":400,
                 "Message": "Invalid office name, name must be characters only"
                 }, 400
        if Type.isdigit():
             return{
                 "status":400,
                 "Message": "Invalid office type, type must be characters only"
                }, 400
        office = CreatePoliticalOffice(name, Type)
        offices.append(office)
        if office:
            return {
                     "status":201,
                     "Message": "New office created successfully"
                }, 201


