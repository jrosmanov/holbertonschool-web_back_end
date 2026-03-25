#!/usr/bin/env python3
"""simple flask"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    """main page"""
    return render_template('0-index.html')


if "__main__" == __name__:
    app.run(debug=True)