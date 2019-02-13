from app.models.models import Parties
from run import app

class Tables:
    def migrate(self):
        Parties().create_tables()


    def drop_table(self):
        Parties().drop_table()

    def drop_table_test(self):
        Parties().drop_table_test()

if __name__ == '__main__':
    with app.app_context():
        Tables().drop_table()
        Tables().migrate()




