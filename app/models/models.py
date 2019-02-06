"""import datetime to help you get the current date and time"""
from datetime import datetime

parties = []
users = []

""" create class party that will hold party related data """
class Parties:
    party_id = 1

    def __init__(self,name=None, hqAddress=None, logoUrl=None):
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl
        self.id = Parties.party_id
        self.date_created = str(datetime.now().replace(microsecond=0, second=0))

        Parties.party_id +=1

        
    """ serialize party data so that we can be able to returnn json """
    def serialize(self):
        return dict(
            id = self.id,
            name = self.name,
            hqAddress = self.hqAddress,
            logoUrl = self.logoUrl,
            date_created = self.date_created
        )

    """ get party by nanme """
    def get_party_by_name(self, name):
        for party in parties:
            if party.name == name:
                return party
    
    """ get a specific party by id """
    def get_specifi_party_by_id(self):
        for party in parties:
            if party.id == id:
                return party
