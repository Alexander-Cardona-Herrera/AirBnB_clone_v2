#!/usr/bin/python3
""" Module for the implementation of flask in the AirBnB clone project,
    looking for a wide comprehension of lasagna code (layered code)

"""

from flask import Flask, escape, request, render_template

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
    """ Method that display the text's pass in route,
        default case='is cool' """
    return "Python "+str(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ Method that display the number if an int is pass in route """
    return str(n)+" is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    """ Method that display 5-number.html if an int is pass in route """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """Run on port 5000 as default and listen to 0.0.0.0"""
    app.run(debug=True, port=5000, host='0.0.0.0')
