import os


class Config:
    DEBUG = False
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = 'hellofrancis'


class ProductionConfiguration(Config):
    DEBUG = False
    TESTING = False


class DevelopmentConfiguration(Config):
    DEBUG = True


class TestingConfiguration(Config):
    TESTING = True
    DEBUG = True


app_config = {
    'production': ProductionConfiguration,
    'testing': TestingConfiguration,
    'development': DevelopmentConfiguration,
    'default': DevelopmentConfiguration
}
