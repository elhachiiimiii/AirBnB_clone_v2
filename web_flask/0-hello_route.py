#!/usr/bin/python3
""" should return html text """

from flask import Flask


app = Flask(__name__)


# root route
@app.route('/', strict_slashes=False)
def hello_world():
    """ should returns Hello HBNB! """
    return 'Hello HBNB!'

if __name__ == '__main__':
    # listen on port 5000
    app.run(host='0.0.0.0', port=5000)
