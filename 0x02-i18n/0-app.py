#!/usr/bin/env python3
""" Module for trying out Flask """
from flask import Flask, render_template

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def get_index() -> str:
    """ Function to render html file """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
