#!/usr/bin/env python3
import sys
from os import getenv
from flask import Flask, redirect, url_for, render_template
from werkzeug.exceptions import HTTPException
from waitress import serve
from functions import initialize, configuration


app = Flask(__name__)
app.secret_key = sys.argv[1].encode()
app.permanent_session_lifetime = False


@app.route('/')
def index():
    """Main page"""
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    """Favicon picture"""
    return redirect(url_for("favicon.ico"))


@app.errorhandler(HTTPException)
def http_error_handler(error):
    """http error page"""
    return render_template("error.html", error=error), error.code


@app.errorhandler(Exception)
def other_error_handler(error):
    """
    system error handler
    return internal server error http code
    """
    return render_template("error.html", error=error), 500


if __name__ == "__main__":
    config = configuration("config.ini")
    if getenv("FLASK_DEBUG"):
        app.run(debug=True)
    else:
        serve(app, host="127.0.0.1", port=8080)
