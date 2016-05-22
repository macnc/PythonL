#! /usr/bin/python
# _*_coding: utf-8

from flask import Flask
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)


@app.route('/')
def index():
    # return '<h3>Bad Request</h3>', 400
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/rc')
def rc():
    return redirect('http://www.apple.com')

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name


if __name__ == '__main__':
    app.run(debug=True)
