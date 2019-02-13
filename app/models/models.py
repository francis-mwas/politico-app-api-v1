"""import datetime to help you get the current date and time."""
from datetime import datetime
from werkzeug.security import generate_password_hash
import psycopg2
from flask import current_app


class DatabaseConnection:
    def __init__(self):
        self.host = current_app.config["DB_HOST"]
        self.name = current_app.config["DB_NAME"]
        self.username = current_app.config["DB_USERNAME"]
        self.password = current_app.config["DB_PASSWORD"]

        self.conn = psycopg2.connect(
            host=self.host,
            database= self.name,
            password=self.password,
            user =self.username
            )


        self.cursor = self.conn.cursor()



class Parties(DatabaseConnection):
    """ create class party that will hold party related data."""

    def __init__(self, name=None, hqAddress=None, logoUrl=None):
        
        super().__init__()
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl
        self.date_created = str(
            datetime.now().replace(microsecond=0, second=0))
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
            date_created=self.date_created
        )


    def get_party_by_name(self, name):
        """get party by nanme."""

        self.cursor.execute(
            "SELECT * FROM parties WHERE name=%s",(name,)
        )
        party = self.cursor.fetchone()
        self.conn.commit()
        self.cursor.close()

        if party:
            return party
        return None

    def get_specific_party_by_id(self, id):
        """ get a specific party by id."""

        self.cursor.execute(
            "SELECT * FROM parties WHERE id=%s",(id,)
        )

        party = self.cursor.fetchone()
        self.conn.commit()
        self.cursor.close()

        if party:
            return self.map_party(party)
        return None

    def map_party(self, data):
        """ party to an object"""

        self.id = data[0]
        self.name = data[1]
        self.hqAddress = data[2]
        self.logoUrl = data[3]
        self.date_created = data[4]

        return self

class CreatePoliticalOffice(DatabaseConnection):
    """ create new political office class."""
 

    def __init__(self, name=None, Type=None):
        super().__init__()
        self.name = name
        self.Type = Type
        self.date_created = str(
            datetime.now().replace(microsecond=0, second=0))
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
            name=self.name,
            Type=self.Type,
            date_created=self.date_created
        )

    def get_office_by_name(self, name):
        """ fetch an office by name."""

        for office in offices:
            if office.name == name:
                return office

    def get_office_by_id(self, office_id):
        """ fetch office by id."""

        for office in offices:
            if office.office_id == office_id:
                return office


class User(DatabaseConnection):
    """ creating class users."""

    user_id = 1

    def __init__(self, firstname=None, lastname=None, othername=None,
     email=None, phoneNumber=None, passportUrl=None, 
     password=None, isAdmin=False):

        super().__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phoneNumber = phoneNumber
        self.passportUrl = passportUrl
        if password:
            self.hashed_password =generate_password_hash(password)
        self.isAdmin = isAdmin
        self.createdDate = str(datetime.now().replace(second=0, microsecond=0))
        self.user_id = User.user_id
        User.user_id += 1
    
    def create_table_users(self):
        """create table users """

        self.cursor.execute(
            """
            CREATE TABLE users(
                user_id serial PRIMARY KEY,
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
            INSERT INTO users (firstname,lastname,othername,email,
            phoneNumber,passportUrl,password,isAdmin,createdDate
            ) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, 
            (self.firstname, self.lastname, self.othername,self.email,
            self.phoneNumber,self.passportUrl, self.hashed_password,self.isAdmin,
            self.createdDate)
        )
        self.conn.commit()
        self.cursor.close()

               

    def serialize(self):
        """ convert user data into a dictionary."""

        return dict(
            firstname=self.firstname,
            lastname=self.lastname,
            othername=self.othername,
            email=self.email,
            phoneNumber=self.phoneNumber,
            passportUrl=self.passportUrl,
            isAdmin=self.isAdmin,
            password=self.hashed_password,
            createdDate=self.createdDate,
            user_id=self.user_id,

        )

    def get_user_by_email(self,email):
        """ get user by email."""

        for user in users:
            if user.email == email:
                return user

