#! /usr/bin/python
# _*_coding: utf-8

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

app = Flask(__name__)
manager = Manager(app)
moment = Moment(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

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
