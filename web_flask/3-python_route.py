#!/usr/bin/python3
from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def base_display():
    """ Method for inicial display of tests """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display():
    """ Method for display of tests """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """ Method that display the text's pass in route """
    return "C "+str(text).replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_default_text(text='is cool'):
    """ Method that display the text's pass in route, default case='is cool' """
    return "Python "+str(text).replace('_', ' ')


if __name__ == '__main__':
    """Run on port 5000 as default and listen to 0.0.0.0"""
    app.run(debug=True, port=5000, host='0.0.0.0')
