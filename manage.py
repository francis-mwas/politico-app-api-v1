from app.models.models import Parties, CreatePoliticalOffice, User, Candidates, Votes
from run import app


class Tables:
    def migrate(self):
        """function to create tables."""
        Parties().create_tables()
        CreatePoliticalOffice().create_office_table()
        User().create_table_users()
        Candidates().create_table_candidates()
        Votes().create_table_votes()


    def drop_table(self):
        """function to drop tables."""
        Parties().drop_table()
        CreatePoliticalOffice().drop_table_offices()
        User().drop_table_user()
        Candidates().drop_table_candidates()
        Votes().drop_table_votes()

    def create_admin(self):
        """creating admin."""
        user = User(32875802, "fram", "mwas", "admin", "admin@gmail.com",
                    1234567, "http://andela.com/imgeas/img1.jpg", "12345", True)
        user.register_user()

if __name__ == '__main__':
    with app.app_context():
        Tables().drop_table()
        Tables().migrate()
        Tables().create_admin()
        
        
