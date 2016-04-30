#!~/anaconda2/bin/python
# _*_coding: utf-8

from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db_user = 'root'
db_pwd = 'LoveDesign**!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@localhost:3306/SQLAlchemy_db'.format(db_user, db_pwd)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique = True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))

    def __int__(self, name, email, username):
        self.name = name
        self.email = email
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.name


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	body = db.Column(db.Text)
	pub_date = db.Column(db.DateTime)

	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
	category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

	def __init__(self, title, body, category, pub_date=None):
		self.title = title
		self.body = body
		if pub_date is None:
			pub_date = datetime.utcnow()
		self.pub_date = pub_date
		self.category = category

	def __repr__(self):
		return '<Post %r>' % self.title


class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return '<Category %r>' % self.name