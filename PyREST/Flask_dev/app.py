#! /usr/bin/python
# _*_coding: utf-8

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Big welcome to come here with Flask!<h1><p>You browser is \n %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h2>Hey, {}</h2>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
