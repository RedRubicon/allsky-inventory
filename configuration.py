class BaseConfig(object):
    'Base Configuration'
    SECRET_KEY = 'yZQ27jONv7m1nZnsd82C'
    DEBUG = True
    TESTING = False

class ProductionConfig(BaseConfig):
    'Production Configuration'
    DEBUG = False
    SECRET_KEY = open("D:\\Code\\allsky-inventory\\key").read()

class StagingConfig(BaseConfig):
    DEBUG = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'TFpH00aL5SUfppWQUaiJ'