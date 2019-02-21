"""import datetime to help you get the current date and time."""
from datetime import datetime
from werkzeug.security import generate_password_hash
import psycopg2
import os
from flask import current_app



class DatabaseConnection:
    def __init__(self):
        self.host = current_app.config["DB_HOST"]
        self.port = current_app.config['DB_PORT']
        self.name = current_app.config["DB_NAME"]
        self.username = current_app.config["DB_USERNAME"]
        self.password = current_app.config["DB_PASSWORD"]

        if os.get_env('DATABASE_URL'):
            self.conn=psycopg2.connect(os.get_env('DATABASE_URL'))
        else:

            self.conn = psycopg2.connect(
                host=self.host,
                database=self.name,
                password=self.password,
                user=self.username
            )
        self.cursor = self.conn.cursor()


class Parties(DatabaseConnection):
    """ create class party that will hold party related data."""

    def __init__(self, name=None, hqAddress=None, logoUrl=None):

        super().__init__()
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl
        self.date_created = datetime.now().replace(microsecond=0, second=0)
        self.id = None

    def create_tables(self):

        self.cursor.execute(
            """
        CREATE TABLE parties (
            id serial PRIMARY KEY,
            name VARCHAR NOT NULL,
            hqAddress VARCHAR NOT NULL,
            logoUrl VARCHAR NOT NULL,
            date_created TIMESTAMP
        );
        """
        )
        self.conn.commit()

    def drop_table(self):
        """ function to drop table parties."""

        self.cursor.execute(
            """
                DROP TABLE IF EXISTS parties
                """
        )
        self.conn.commit()

    def create_party(self):
        """insert party data into a database."""

        self.cursor.execute(

            '''INSERT INTO parties(name, hqAddress,
             logoUrl, date_created) VALUES(%s, %s, %s, %s)''',

            (self.name, self.hqAddress, self.logoUrl, self.date_created)
        )
        self.conn.commit()
        self.cursor.close()

    def serialize(self):
        """ serialize party data so that we can be able to returnn json."""
        return dict(
            id=self.id,
            name=self.name,
            hqAddress=self.hqAddress,
            logoUrl=self.logoUrl,
            date_created=str(self.date_created)
        )

    def get_party_by_name(self, name):
        """get party by nanme."""

        self.cursor.execute(
            "SELECT * FROM parties WHERE name=%s", (name,)
        )
        party = self.cursor.fetchone()
        self.conn.commit()
        self.cursor.close()

        if party:
            return self.map_parties(party)
        return None

    def get_specific_party_by_id(self, id):
        """ get a specific party by id."""

        self.cursor.execute(
            "SELECT * FROM parties WHERE id=%s", (id, )
        )

        party = self.cursor.fetchone()
        self.conn.commit()
        self.cursor.close()

        if party:
            return self.map_parties(party)
        return None

    def get_all_parties(self):
        """fetch all parties."""

        self.cursor.execute("SELECT * FROM parties")
        parties = self.cursor.fetchall()
        self.conn.commit()
        self.cursor.close()

        if parties:
            return [self.map_parties(party) for party in parties]
        return None

    def delete_party(self, id):
        """delete party."""

        self.cursor.execute(
            "DELETE FROM parties WHERE id=%s", (id,)
        )
        self.conn.commit()
        self.cursor.close()

    def update_party(self, id):
        """update specific party by id"""

        self.cursor.execute(
            """
            UPDATE parties SET name =%s,hqaddress=%s, logourl=%s WHERE id=%s""",
            (self.name, self.hqAddress, self.logoUrl, id)
        )
        self.conn.commit()
        self.cursor.close()

    def map_parties(self, data):
        """ convert party tuple to an object"""
        party = Parties(name=data[1], hqAddress=data[2], logoUrl=data[3])
        party.id = data[0]
        party.date_created = data[4]
        self = party

        return self


class CreatePoliticalOffice(DatabaseConnection):
    """ create new political office class."""

    def __init__(self, Type=None, name=None):
        super().__init__()
        self.Type = Type
        self.name = name
        self.date_created = datetime.now().replace(microsecond=0, second=0)
        self.office_id = None

    def create_office_table(self):
        """create table offices."""

        self.cursor.execute(
            """
                CREATE TABLE offices (
                    office_id serial PRIMARY KEY,
                    Type VARCHAR NOT NULL,
                    name VARCHAR NOT NULL,
                    date_created TIMESTAMP
                );
                """
        )
        self.conn.commit()
        self.cursor.close()

    def drop_table_offices(self):
        """ function to drop table offices """

        self.cursor.execute(
            """
                DROP TABLE IF EXISTS offices
                """
        )
        self.conn.commit()

    def create_office(self):
        """insert office data into a database."""

        self.cursor.execute(

            """INSERT INTO offices(Type,name,date_created) VALUES(%s, %s, %s)""",
            (self.Type, self.name, self.date_created)
        )
        self.conn.commit()
        self.cursor.close()

    def serializer(self):
        """convert office data into a dictionary."""

        return dict(
            office_id=self.office_id,
            Type=self.Type,
            name=self.name,
            date_created=str(self.date_created)
        )

    def fetch_all_offices(self):
        """get all offices."""

        self.cursor.execute("SELECT * FROM offices")
        offices = self.cursor.fetchall()
        self.conn.commit()
        self.cursor.close()

        if offices:
            return [self.Objectify_office(office) for office in offices]
        return None

    def get_office_by_name(self, name):
        """ fetch an office by name."""

        self.cursor.execute(
            "SELECT * FROM offices WHERE name=%s", (name,)
        )

        office = self.cursor.fetchone()
        self.conn.commit()
        self.cursor.close()

        if office:
            return self.Objectify_office(office)
        None

    def get_office_by_id(self, office_id):
        """ fetch office by id."""

        self.cursor.execute(
            "SELECT * FROM offices WHERE office_id=%s", (office_id,)
        )
        office = self.cursor.fetchone()
        self.conn.commit()
        self.cursor.close()

        if office:
            return self.Objectify_office(office)
        return None

    def delete_office(self, office_id):
        """delete office by id."""

        self.cursor.execute(
            "DELETE FROM offices WHERE office_id =%s", (office_id,)
        )
        self.conn.commit()
        self.cursor.close()

    def update_office(self, office_id):
        """update specific party."""

        self.cursor.execute(
            """UPDATE offices SET Type=%s, name=%s WHERE office_id=%s""",
            (self.Type, self.name, office_id)

        )
        self.conn.commit()
        self.cursor.close()

    def Objectify_office(self, office_data):
        """convert office data from tuple to an objet"""

        office = CreatePoliticalOffice(
            name=office_data[2], Type=office_data[1])
        office.office_id = office_data[0]
        office.date_created = office_data[3]
        self = office
        return self


class User(DatabaseConnection):
    """ creating class users."""

    def __init__(self, national_id=None, firstname=None, lastname=None, othername=None,
                 email=None, phoneNumber=None, passportUrl=None,
                 password=None, isAdmin=False):

        super().__init__()
        self.national_id = national_id
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phoneNumber
        self.passportUrl = passportUrl
        if password:
            self.hashed_password = generate_password_hash(password)
        self.isAdmin = isAdmin
        self.createdDate = str(datetime.now().replace(second=0, microsecond=0))
        self.user_id = None

    def create_table_users(self):
        """create table users """

        self.cursor.execute(
            """
            CREATE TABLE users(
                user_id serial PRIMARY KEY,
                national_id VARCHAR NOT NULL,
                firstname VARCHAR NOT NULL,
                lastname VARCHAR NOT NULL,
                othername VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                phoneNumber VARCHAR NOT NULL,
                passportUrl VARCHAR NOT NULL,
                password VARCHAR NOT NULL,
                isAdmin BOOLEAN NOT NULL,
                createdDate TIMESTAMP
            ) 
            """
        )
        self.conn.commit()

    def drop_table_user(self):
        """drop table users if already exist."""

        self.cursor.execute(
            """
                DROP TABLE IF EXISTS users
            """
        )
        self.conn.commit()

    def register_user(self):
        """insert user data into a database."""

        self.cursor.execute(
            """
            INSERT INTO users (national_id,firstname,lastname,othername,email,
            phoneNumber,passportUrl,password,isAdmin,createdDate
            ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING user_id
            """,
            (self.national_id, self.firstname, self.lastname, self.othername, self.email,
             self.phoneNumber, self.passportUrl, self.hashed_password, self.isAdmin,
             self.createdDate)
        )
        self.conn.commit()
        self.cursor.close()

    def serialize(self):
        """ convert user data into a dictionary."""

        return dict(
            national_id=self.national_id,
            firstname=self.firstname,
            lastname=self.lastname,
            othername=self.othername,
            email=self.email,
            phoneNumber=self.phoneNumber,
            passportUrl=self.passportUrl,
            password=self.hashed_password,
            isAdmin=self.isAdmin,
            createdDate=str(self.createdDate),
            user_id=self.user_id,

        )

    def get_user_by_email(self, email):
        """ get user by email."""
        self.cursor.execute(
            "SELECT * FROM users WHERE email=%s", (email, )
        )
        user_data = self.cursor.fetchone()
        self.conn.commit()
        self.cursor.close()
        if user_data:
            return self.objectify_user_data(user_data)
        return None

    def get_user_by_id(self, user_id):
        """ get user by user_id."""
        self.cursor.execute(
            "SELECT * FROM users WHERE user_id=%s", (user_id, )
        )
        user_data = self.cursor.fetchone()
        self.conn.commit()
        self.cursor.close()
        if user_data:
            return self.objectify_user_data(user_data)
        return None

    def get_user_national_id(self, national_id):
        """ get user national id"""
        self.cursor.execute(
            "SELECT * FROM users WHERE national_id=%s", (national_id, )
        )
        user_data = self.cursor.fetchone()
        self.conn.commit()
        self.cursor.close()
        if user_data:
            return self.objectify_user_data(user_data)
        return None

    def get_user_phone_number(self, phoneNumber):
        """ get user phone number."""
        self.cursor.execute(
            "SELECT * FROM users WHERE phoneNumber=%s", (phoneNumber, )
        )
        user_data = self.cursor.fetchone()
        self.conn.commit()
        self.cursor.close()
        if user_data:
            return self.objectify_user_data(user_data)
        return None

    def get_user_passport_url(self, passportUrl):
        """ get user by user_id."""
        self.cursor.execute(
            "SELECT * FROM users WHERE passportUrl=%s", (passportUrl, )
        )
        user_data = self.cursor.fetchone()
        self.conn.commit()
        self.cursor.close()
        if user_data:
            return self.objectify_user_data(user_data)
        return None

    def objectify_user_data(self, user_data):
        """convert user data into a dictionary """

        user = User(national_id=user_data[1], firstname=user_data[2],
                    lastname=user_data[3], othername=user_data[4],
                    email=user_data[5], phoneNumber=user_data[6],
                    passportUrl=user_data[7], password=user_data[8], isAdmin=user_data[9])
        user.user_id = user_data[0]
        user.hashed_password = user_data[8]
        user.createdDate = user_data[10]

        self = user

        return self


class GetUsers(User):

    def fetch_all_users(self):
        """get all users."""

        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        self.conn.commit()
        self.cursor.close()

        if users:
            return [self.objectify_user_data(user) for user in users]
        return None


class Candidates(DatabaseConnection):
    """ creating class candidates."""

    def __init__(self, office_id=None, party_id=None, candidate_id=None, date_created=None):

        super().__init__()
        self.office_id = office_id
        self.party_id = party_id
        self.candidate_id = candidate_id
        self.date_created = datetime.now().replace(second=0, microsecond=0)
        self.id = None

    def create_table_candidates(self):
        """create table candidate """

        self.cursor.execute(
            """
            CREATE TABLE candidates(
                id serial PRIMARY KEY,
                office_id INTEGER NOT NULL,
                party_id INTEGER NOT NULL,
                candidate_id INTEGER,
                date_created TIMESTAMP
            )
            """
        )
        self.conn.commit()
        self.cursor.close()

    def get_all_candidates(self):
        """"get all candidates"""

        self.cursor.execute(
            """
               SELECT * FROM candidates
          """
        )
        candidates = self.cursor.fetchall()
        self.conn.commit()
        self.cursor.close()

        if candidates:
            return [self.map_candidates(candidate) for candidate in candidates]
        return None

    def get_candidate_by_id(self, candidate_id):
        """ get a specific party by id."""
        try:

            self.cursor.execute(
                "SELECT * FROM candidates WHERE candidate_id={}".format(
                    candidate_id)
            )
            candidate = self.cursor.fetchone()
            self.conn.commit()
            self.cursor.close()
            if candidate:
                return self.map_candidates(candidate)
            return None

        except psycopg2.DatabaseError as error:
            print(error)

    def check_if_party_and_office_taken(self, office_id, party_id):
        """check if there is a candidate registered under the same office and party"""
        self.cursor.execute(
            "SELECT * FROM candidates WHERE office_id=%s AND party_id=%s", (
                office_id, party_id)
        )
        party_office_exist = self.cursor.fetchone()

        self.conn.commit()
        self.cursor.close()

        if party_office_exist:
            return self.map_candidates(party_office_exist).serialize()
        return None

    def drop_table_candidates(self):
        """drop table candidates if already exist."""

        self.cursor.execute(
            """
                DROP TABLE IF EXISTS candidates
            """
        )
        self.conn.commit()
        self.cursor.close()

    def register_candidates(self):
        """insert candidates data into a database."""

        self.cursor.execute(
            """
            INSERT INTO candidates (office_id, party_id, candidate_id, date_created)
             VALUES(%s,%s,%s,%s)
            """,
            (self.office_id, self.party_id, self.candidate_id, self.date_created)
        )
        self.conn.commit()
        self.cursor.close()

    def serialize(self):
        """ convert candidate data into a dictionary."""

        return dict(
            office_id=self.office_id,
            party_id=self.party_id,
            candidate_id=self.candidate_id,
            date_created=str(self.date_created),
            id=self.id,

        )

    def map_candidates(self, data):
        """ convert candidate tuple to an object"""

        candidate = Candidates(
            office_id=data[2], party_id=data[1], candidate_id=data[0])
        candidate.id = data[3]
        candidate.date_created = data[4]
        self = candidate
        return self


class Votes(DatabaseConnection):
    """ creating votes """

    def __init__(self, createdBy=None, office_id=None, candidate_id=None, party_id=None, date_created=None):

        super().__init__()
        self.createdBy = createdBy
        self.office_id = office_id
        self.candidate_id = candidate_id
        self.party_id = party_id
        self.date_created = str(
            datetime.now().replace(second=0, microsecond=0))

    def create_table_votes(self):
        """create table votes """

        self.cursor.execute(
            """
            CREATE TABLE votes(
                id serial PRIMARY KEY,
                createdBy INTEGER NOT NULL,
                office_id INTEGER NOT NULL,
                candidate_id INTEGER NOT NULL,
                party_id INTEGER NOT NULL,
                date_created TIMESTAMP
            )
            """
        )
        self.conn.commit()
        self.cursor.close()

    def drop_table_votes(self):
        """drop table votes if already exist."""
        self.cursor.execute(
            """
                DROP TABLE IF EXISTS votes
            """
        )
        self.conn.commit()

    def add_vote(self):
        """insert candidates data into a database."""

        self.cursor.execute(
            """
            INSERT INTO votes(createdBy,office_id, candidate_id,party_id, date_created)
             VALUES(%s,%s,%s,%s,%s)
            """,
            (self.createdBy, self.office_id, self.candidate_id,
             self.party_id, self.date_created)
        )
        self.conn.commit()
        self.cursor.close()

    def get_already_voted_users(self, createdby, office_id):
        self.cursor.execute(
            "SELECT * FROM votes WHERE createdby=%s AND office_id=%s", (
                createdby, office_id)
        )
        voted_users = self.cursor.fetchone()
        self.conn.commit()
        self.cursor.close()

        if voted_users:
            return self.objectify_votes_data(voted_users)
        None

    def get_votes_for_a_specific_candidate(self, office_id, candidate_id):
        """get votes for a specific candidate """

        self.cursor.execute(
            "SELECT * FROM votes WHERE office_id=%s AND candidate_id=%s", (
                office_id, candidate_id)
        )
        votes = self.cursor.fetchall()
        print(votes)

        self.conn.commit()
        self.cursor.close()

        if votes:
            return [self.objectify_votes_data(vote) for vote in votes]

        return None

    def serialize(self):
        """ convert vote data into a dictionary."""

        return dict(
            office_id=self.office_id,
            candidate_id=self.candidate_id,
            createdBy=self.createdBy,
            date_created=self.date_created
        )

    def objectify_votes_data(self, votes_data):
        """convert votes into a dictionary """
        votes = Votes(createdBy=votes_data[1], office_id=votes_data[2],
                      candidate_id=votes_data[3], date_created=votes_data[5])
        return votes
