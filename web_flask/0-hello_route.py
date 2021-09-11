from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def base_display():
    """ Method for inicial display of tests """
    return 'Hello HBNB!'


if __name__ == '__main__':
    """ Run on port 5000 as default and listen to 0.0.0.0 """
    app.run(debug=True, port=5000, host='0.0.0.0')
