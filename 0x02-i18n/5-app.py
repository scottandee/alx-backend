#!/usr/bin/env python3
"""This flask app parametizes the templates
based on the locale of the user.
"""

from flask import Flask, render_template, request, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Returns a user dictionary if exists or
    None otherwise
    """
    if request.args.get("login_as"):
        id = request.args.get("login_as")
        return users.get(int(id))
    return


@app.before_request
def before_request():
    """This function runs just before any
    request is processed
    """
    user = get_user()
    g.user = user


@app.route("/")
def hello():
    """This route returns the
    index.html file
    """
    home_title = _("Welcome to Holberton")
    home_header = _("Hello world!")
    logged_in_as = _("You are logged in as %(username)s.")
    not_logged_in = _("You are not logged in.")
    return render_template(
        "5-index.html", title=home_title, header=home_header,
        not_logged_in=not_logged_in, logged_in_as=logged_in_as
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
