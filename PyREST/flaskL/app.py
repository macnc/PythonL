#!~/anaconda2/bin/python
# _*_coding: utf-8

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello 孙涛!"

if __name__ == "__main__":
    app.run(debug = True)