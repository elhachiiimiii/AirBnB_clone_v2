#!/usr/bin/python3
""" should return html text """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ should returns Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """ should returns HBNB """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ should replace text """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ should replace more text """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    """ should replace with int number """
    n = str(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def html_num(n):
    """ should return html """
    n = str(n)
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
