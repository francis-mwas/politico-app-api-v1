import re 

class Validations:
    """ main validation class."""

    def validate_email(self, email):
        """ validate for email """
        return re.match("^[^@]+@[^@]+\.[^@]+$", email)


    
    def validate_phone_number(self, phoneNumber):
        """phone number must start with a digit and end with

        a digit, and must be ten digits onnly
         """
        return re.match(r'^\d{4}-\d{3}-\d{3}$', phoneNumber)

    
    def validate_ids(self, ids):
        """ validate ids """
        return re.match("^[1-9]{,2}$", ids)        
    
    def validate_input_fields(self, input_fields):
        """ validate input fields to accept characters only."""

        return re.match("^[a-zA-Z]{3,}", input_fields)

   
    def validate_password(self, password):
        """ validate password."""

        return re.match("^[a-zA-Z0-9]{3,10}$",password)

    def validate_national_id(self, national_id):
        """validate national id"""
        
        return re.match("^\d[1-9]\d{8}$", national_id)

  
    def validate_url(self, url):
        """ function to validate url."""

        return re.search(r"^https?://(?:[a-z0-9\-]+\.)+[a-z]{2,}(?:/[^/#?]+)+\.(?:jp?g|gif|png)$",url)
            
         

   

    