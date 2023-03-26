#!/usr/bin/env python3
import sys
from flask import Flask, redirect, url_for, render_template
from werkzeug.exceptions import HTTPException


app = Flask("bookhmsrvr")
app.secret_key = sys.argv[1].encode()
app.permanent_session_lifetime = False


@app.route('/')
def hello():
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    return redirect(url_for('favicon.ico'))


@app.errorhandler(HTTPException)
def http_error_handler(error):
    return render_template("error.html", error=error), error.code


@app.errorhandler(Exception)
def other_error_handler(error):
    return render_template("error.html", error=error)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=8080)

