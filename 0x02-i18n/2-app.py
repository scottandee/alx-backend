#!/usr/bin/env python3
"""Basic flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel


def get_locale():
    """This returns the suitable language"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


class Config:
    """Configurations for flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


app.config.from_object(Config)


@app.route("/")
def hello():
    """This route returns the
    index.html file
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
