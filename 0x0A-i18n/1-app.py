#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]


app = Flask(__name__)
app.config.from_pyfile(Config)
babel = Babel(app)


@app.route('/')
def hello_world():
    """ Greeting

        Return:
            Initial template html
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
