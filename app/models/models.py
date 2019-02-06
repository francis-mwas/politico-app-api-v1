"""import datetime to help you get the current date and time"""
from datetime import datetime

parties = []
offices = []
users = []

""" create class party that will hold party related data """


class Parties:
    party_id = 1

    def __init__(self, name=None, hqAddress=None, logoUrl=None):
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl
        self.id = Parties.party_id
        self.date_created = str(
            datetime.now().replace(microsecond=0, second=0))

        Parties.party_id += 1

    """ serialize party data so that we can be able to returnn json """

    def serialize(self):
        return dict(
            id=self.id,
            name=self.name,
            hqAddress=self.hqAddress,
            logoUrl=self.logoUrl,
            date_created=self.date_created
        )

    """ get party by nanme """

    def get_party_by_name(self, name):
        for party in parties:
            if party.name == name:
                return party

    """ get a specific party by id """

    def get_specific_party_by_id(self, id):
        for party in parties:
            if party.id == id:
                return party


""" create new political office class"""


class CreatePoliticalOffice:
    office_id = 1

    def __init__(self, name=None, Type=None):
        self.name = name
        self.Type = Type
        self.date_created = str(
            datetime.now().replace(microsecond=0, second=0))
        self.office_id = CreatePoliticalOffice.office_id
        CreatePoliticalOffice.office_id += 1

    """serialize data so that it becomes json friendly """

    def serializer(self):
        return dict(
            office_id=self.office_id,
            name=self.name,
            Type=self.Type,
            date_created=self.date_created
        )
    """ fetch an office by name """

    def get_office_by_name(self, name):
        for office in offices:
            if office.name == name:
                return office
    """ fetch office by id """

    def get_office_by_id(self, office_id):
        for office in offices:
            if office.office_id == office_id:
                return office


""" creating class users """

class User:
    user_id = 1
    def __init__(self, firstname=None, lastname=None, othername=None,email=None, phoneNumber=None, passportUrl=None, isAdmin=None):
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phoneNumber
        self.passportUrl = passportUrl
        self.isAdmin = isAdmin
        self.createdDate = datetime.now().replace(second=0, microsecond=0)
        self.user_id = User.user_id
        User.user_id +=1

    """ get user by email """
    def get_user_by_email(self, email):
        for user in users:
            if user.email == email:
                return email




    
