import os


class Config:
    """ main class configurations."""
    DEBUG = False
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = 'hellofrancis'


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
