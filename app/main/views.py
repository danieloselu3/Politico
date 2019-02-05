"""view functions live here"""

from flask import Flask  #import flask

APP = Flask(__name__)  #instantiate flask as app

@APP.route('/')
def index():
    """desribes the default page"""
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    APP.run(debug=True)
