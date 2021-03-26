# Flask App Configuration
class BaseConfig(object):
    'Base Config Class'
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'xIHMuZ07yBKRBKvZ5t2D'

class ProductionConfig(BaseConfig):
    'Production configuration'
    DEBUG = False
    SECRET_KEY = open('.\key').read()

class DevelopmentConfig(BaseConfig):
    'Development configuration'
    DEBUG = True
    TESTING = True

class StagingConfig(BaseConfig):
    'Staging configuration'
    DEBUG = True