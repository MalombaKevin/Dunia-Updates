from distutils.debug import DEBUG


class Config :
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True