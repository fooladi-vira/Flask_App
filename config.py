import os

class config:
    BASE_DIR=os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLE=True
    CSRF_SESSION_KEY='ff3790a7011c88cf84b7f1bfaf955615bab556ca141b3c12eddb90bd5392c46b'
    SECRET_KEY='46317c6aa0e20ee66d6ee04dab3604728b22a16feb119ec6d17ae0fe9a337473'

class ProdConfig(config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI=...

class DevConfig(config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='sqlite:///'+ os.path.join(config.BASE_DIR,'app.db')