import os
from app import create_app
from app.models.models import Parties
app = create_app(os.getenv("APP_SETTINGS") or "default")



if __name__ == '__main__':
     """run flask application in debug mode."""
     app.run(debug=True)
     
    
