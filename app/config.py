# db config class
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Benzokolon1@localhost/flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET = 'test'  # api keys, passwords etc.
