import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, String, Integer, create_engine, Text

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
database_path = os.environ['DATABASE_URL']


#database_name = "postgres"
#db_path = "postgres://tyxzuqccfokonr:194f366cda0405fecff4331ed1b1643654c5e47cd178885aaa60db63bc124171@ec2-35-171-31-33.compute-1.amazonaws.com:5432/d3iq930ftck64c"
db = SQLAlchemy()
def setup_db(app, database_path=database_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  db.init_app(app)
  db.create_all()
'''
Movie

'''
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    release_date  = db.Column(String(), nullable=False)


    def __init__(self, title, release_date):
        self.title= title
        self.release_date= release_date

    def details(self):
        return{
        'id':self.id,
        'title':self.title,
        'release_date':self.release_date,
    }
    def update(self):
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'title': self.title,
        'release_date': self.release_date,
    }
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def insert(self):
        db.session.add(self)
        db.session.commit()

'''
Actors

'''
class Actors(db.Model):
    __tablename__ = 'actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(Text(), nullable=False)

    def __init__(self, name, age, gender):
        self.name= name
        self.age= age
        self.gender= gender

    def details(self):
        return{
        'id':self.id,
        'name':self.name,
        'age':self.age,
        'gender':self.gender
    }
    def update(self):
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'name': self.name,
        'age':self.age,
        'gender': self.gender
    }
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()
