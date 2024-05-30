#!/usr/bin/env python3
from flask import Flask, render_template
from flask_babel import Babel

"""The Babel extension is initialized with the Flask instance app.
The Config class is created with the LANGUAGES, BABEL_DEFAULT_LOCALE,
and BABEL_DEFAULT_TIMEZONE attributes. The LANGUAGES attribute is
a list of languages that the application supports.
The BABEL_DEFAULT_LOCALE attribute is set to "en" to set the
default language to English. The BABEL_DEFAULT_TIMEZONE attribute
is set to "UTC" to set the default timezone to Coordinated Universal
Time (UTC). The app.config.from_object(Config) method is called to
load the configuration from the Config class.
"""


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """ Function to render html file """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
