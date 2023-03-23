#!/usr/bin/env python3
import sys
from flask import Flask, redirect, url_for, render_template

app = Flask("bookhmsrvr")
app.secret_key = sys.argv[1].encode()
app.permanent_session_lifetime = False


@app.route('/')
def hello():
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    return redirect(url_for('favicon.ico'))


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="127.0.0.1", port=80)
