#!~/anaconda2/bin/python
# _*_coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db_user = 'root'
db_pwd = 'LoveDesign**!'
db_host = 'localhost:3306/Flask_RESTful'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}'.format(db_user, db_pwd, db_host)
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique = True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))

    def __int__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name
