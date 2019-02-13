import os

class Config:
    """ main class configurations."""
    DEBUG = False
    TESTING = True
    CSRF_ENABLED = True

    SECRET_KEY = os.getenv('SECRET_KEY')
    DB_HOST = os.getenv('DB_HOST')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')


class ProductionConfiguration(Config):
    """production mode configurations."""
    DEBUG = False
    TESTING = False


class DevelopmentConfiguration(Config):
    """ application development configuration."""
    DEBUG = True


class TestingConfiguration(Config):
    """ application testing configuration."""
    TESTING = True
    DEBUG = True


app_config = {
    'production': ProductionConfiguration,
    'testing': TestingConfiguration,
    'development': DevelopmentConfiguration,
    'default': DevelopmentConfiguration
}


