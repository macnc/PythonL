#!/usr/local/bin/python3
# _*_coding: utf-8


from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save')
def save():
    return redirect(url_for('index'))

app.run(debug=True, host='0.0.0.0', port=8000)