#! /usr/bin/python
# _*_coding: utf-8

import os
from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
from datetime import datetime
from flask import render_template
from flask.ext.moment import Moment
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from flask.ext.mail import Message


# Flask Class/Sub-Class instantiation
app = Flask(__name__)
manager = Manager(app)
moment = Moment(app)
mail = Mail(app)
bootstrap = Bootstrap(app)

# app configuration
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =
    'mysql://root:LoveDesign**@localhost/flask_dev'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['FLASK_ADMIN'] = os.environ.get('FLASK_ADMIN')
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <18568595@qq.com>'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
db = SQLAlchemy(app)


def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
    sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt' + **kwargs)
    msg.html = render_template(template + '.html' + **kwargs)
    mail.send(msg)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
	return '<User %r>' % self.username



@app.route('/', methods=['GET', 'POST'])
def index():
    # user_agent = request.headers.get('User-Agent')
    # return render_template('index.html', current_time=datetime.utcnow())
    name = None
    form = NameForm()
    if form.validate_on_submit():
	old_name = session.get('name')
	if old_name is not None and old_name != form.name.data:
	    flash('Looks like you changed your name!')
	session['name'] = form.name.data
	return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
