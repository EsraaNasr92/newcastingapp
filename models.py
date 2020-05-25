"""
import os
from sqlalchemy import Column, String, Integer, create_engine, Text
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "postgres"
database_path = "postgres://{}/{}".format('postgres:123456@localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

"""


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, String, Integer, create_engine, Text

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
database_name = "postgres"
db_path = "postgres://{}/{}".format('postgres:123456@localhost:5432', database_name)
db = SQLAlchemy()
def setup_db(app, db_path=db_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = db_path
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
