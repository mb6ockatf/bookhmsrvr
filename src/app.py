#!/usr/bin/env python3
from sys import argv
from logging import WARNING
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.exceptions import HTTPException
from waitress import serve
from functions import configuration, Logger
from database import load_queries, DatabaseConnection


app = Flask(__name__)
app.secret_key = argv[1].encode()
app.permanent_session_lifetime = False


@app.route('/')
def index():
    """main page"""
    return render_template("index.html")


@app.route('/books/<author>/<book_name>')
def book():
    """return book page"""
    author = request.args.get("author")
    book_name = request.args.get("book_name")


@app.route("/favicon.ico")
def favicon():
    """favicon picture"""
    return redirect(url_for("favicon.ico"))


@app.errorhandler(HTTPException)
def http_error_handler(error):
    """http error page"""
    return render_template("error.html", error=error), error.code


@app.errorhandler(Exception)
def other_error_handler(error):
    """system error handler. returns internal server error http code"""
    return render_template("error.html", error=error), 500


if __name__ == "__main__":
    logger = Logger("main.log")
    config = configuration("config.ini")
    DEBUG = config["application"]["debug"] == "true"
    if not DEBUG:
        logger.update_level(WARNING)
    queries_manager = load_queries()
    db_connection = DatabaseConnection(config["postgresql"])
    destructive_query = queries_manager["drop_all"]
    print(DEBUG)
    if DEBUG:
        db_connection.execute_query(destructive_query)
    db_connection.execute_query(queries_manager["users_table"], debug=DEBUG)
    db_connection.execute_query(queries_manager["reviews_table"], debug=DEBUG)
    db_connection.execute_query(queries_manager["authors_table"], debug=DEBUG)
    db_connection.execute_query(queries_manager["books_table"], debug=DEBUG)
    if DEBUG:
        app.run(debug=True)
    else:
        serve(app, host="127.0.0.1", port=8080)