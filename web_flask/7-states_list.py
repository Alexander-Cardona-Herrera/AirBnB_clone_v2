#!/usr/bin/python3
""" Module for the implementation of flask in the AirBnB clone project,
    looking for a wide comprehension of lasagna code (layered code)

"""


from flask import Flask, escape, request, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """ Method that display a list of states """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """ Method to close the current database session """
    storage.close()


if __name__ == '__main__':
    """Run on port 5000 as default and listen to 0.0.0.0"""
    app.run(debug=True, port=5000, host='0.0.0.0')
