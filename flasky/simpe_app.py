#!/usr/local/bin/python3
# _*_coding: utf-8


from flask import Flask
from flask import render_template
# from flask import request


app = Flask(__name__)

# The root of RESTful API for http request.
@app.route('/')
@app.route('/<name>')
def index(name = 'Beautiful world'):
    # Accept args value from query string.
    # name = request.args.get('name', name)
    # return "Hello from suntao's Mac for {}".format(name)
    return render_template("index.html", name=name)

# Accept all of scenarios for data types.
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
    context = {'num1': num1, 'num2': num2}
    return render_template('add.html', **context)

app.run(debug=True, port=8000, host='0.0.0.0')