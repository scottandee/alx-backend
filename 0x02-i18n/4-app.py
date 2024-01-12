#!/usr/bin/env python3
"""This flask app parametizes the templates
based on the locale of the user.
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
    if request.args.get("locale"):
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def hello():
    """This route returns the
    index.html file
    """
    home_title = _("Welcome to Holberton")
    home_header = _("Hello world!")
    return render_template(
        "4-index.html", title=home_title, header=home_header
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
