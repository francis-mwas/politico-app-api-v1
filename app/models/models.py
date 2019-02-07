"""import datetime to help you get the current date and time"""
from datetime import datetime

parties = []
offices = []
users = []


class Parties:
    """ create class party that will hold party related data """
    party_id = 1

    def __init__(self, name=None, hqAddress=None, logoUrl=None):
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl
        self.id = Parties.party_id
        self.date_created = str(
            datetime.now().replace(microsecond=0, second=0))

        Parties.party_id += 1

    def serialize(self):
        """ serialize party data so that we can be able to returnn json """
        return dict(
            id=self.id,
            name=self.name,
            hqAddress=self.hqAddress,
            logoUrl=self.logoUrl,
            date_created=self.date_created
        )

    def get_party_by_name(self, name):
        """ get party by nanme """
        for party in parties:
            if party.name == name:
                return party

    def get_specific_party_by_id(self, id):
        """ get a specific party by id """
        for party in parties:
            if party.id == id:
                return party


class CreatePoliticalOffice:
    """ create new political office class"""
    office_id = 1

    def __init__(self, name=None, Type=None):
        self.name = name
        self.Type = Type
        self.date_created = str(
            datetime.now().replace(microsecond=0, second=0))
        self.office_id = CreatePoliticalOffice.office_id
        CreatePoliticalOffice.office_id += 1

    def serializer(self):
        """conver into a dictionary"""
        return dict(
            office_id=self.office_id,
            name=self.name,
            Type=self.Type,
            date_created=self.date_created
        )

    def get_office_by_name(self, name):
        """ fetch an office by name """
        for office in offices:
            if office.name == name:
                return office

    def get_office_by_id(self, office_id):
        """ fetch office by id """
        for office in offices:
            if office.office_id == office_id:
                return office


class User:
    """ creating class users """
    user_id = 1

    def __init__(self, firstname=None, lastname=None, othername=None,
     email=None, phoneNumber=None, passportUrl=None, 
     isAdmin=None, password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phoneNumber
        self.passportUrl = passportUrl
        self.isAdmin = isAdmin
        self.password = password
        self.createdDate = str(datetime.now().replace(second=0, microsecond=0))
        self.user_id = User.user_id
        User.user_id += 1

    def serialize(self):
        """ convert user data into a dictionary """
        return dict(
            firstname=self.firstname,
            lastname=self.lastname,
            othername=self.othername,
            email=self.email,
            phoneNumber=self.phoneNumber,
            passportUrl=self.passportUrl,
            isAdmin=self.isAdmin,
            password=self.password,
            createdDate=self.createdDate,
            user_id=self.user_id,

        )

    def get_user_by_email(self, email):
        """ get user by email """
        for user in users:
            if user.email == email:
                return email
