import os


class Config:
    SQLALCHEMY_URI = 'sqlite:///'


class Local:
    SQLALCHEMY_URI = os.environ.get('SQLALCHEMY_URI')


class Test:
    SQLALCHEMY_URI = 'sqlite:///'
