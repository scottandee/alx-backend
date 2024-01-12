#!/usr/bin/env python3
"""Basic flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configurations for flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """This returns the suitable language"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello():
    """This route returns the
    index.html file
    """
    home_title = _("Welcome to Holberton")
    home_header	 = _("Hello world!")
    return render_template("3-index.html", home_header=home_header, home_title=home_title)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
