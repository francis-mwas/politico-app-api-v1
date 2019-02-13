from app.models.models import Parties, CreatePoliticalOffice, User
from run import app

class Tables:
    def migrate(self):
        Parties().create_tables()
        CreatePoliticalOffice().create_office_table()
        User().create_table_users()


    def drop_table(self):
        Parties().drop_table()
        CreatePoliticalOffice().drop_table_offices()
        User().drop_table_user()

    def drop_table_test(self):
        Parties().drop_table_test()

if __name__ == '__main__':
    with app.app_context():
        Tables().drop_table()
        Tables().migrate()
        




