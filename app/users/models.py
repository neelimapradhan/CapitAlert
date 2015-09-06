from app.users import constants as USER
from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)


class User(db.Model):

    __tablename__ = 'users_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    role = db.Column(db.SmallInteger, default=USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)
    user_data = relationship("UserData",
    __tablename__ = 'user_data'
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Integer, default=0)
    

def __init__(self, name=None, email=None, password=None):
  self.name = name
  self.email = email
  self.password = password

def getStatus(self):
  return USER.STATUS[self.status]

def getRole(self):
  return USER.ROLE[self.role]

def __repr__(self):
  return '<User %r>' % (self.name)