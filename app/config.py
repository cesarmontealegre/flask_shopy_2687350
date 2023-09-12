#configurar app para conectarse a bd
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3308/flask-shopy-2687350'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'loquequieran'