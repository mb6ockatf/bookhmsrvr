#!/usr/bin/env python3
from sys import argv
from logging import WARNING
from dataclasses import dataclass
from datetime import datetime
from pprint import pprint
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.exceptions import HTTPException
from waitress import serve
from functions import configuration, Logger
from database import load_queries, DatabaseConnection
from add_data import add_data


def get_safe_url(url: str) -> str:
    return url.replace(" ", "_")


@dataclass
class BookExpressEntry:
    name: str
    author: str
    language: str

    def link(self) -> str:
        result = f"/books/{self.author}/{self.name}"
        result = get_safe_url(result)
        return result


@dataclass
class BookEntry:
    name: str
    author: str
    datetime.date: str
    language: str
    pages: str
    description: str
    wikilink: str
    rating: str
    viewerscounter: int
    downloadscounter: int
    epubsize: int
    pdfsize: int


app = Flask(__name__)
app.secret_key = argv[1].encode()
app.permanent_session_lifetime = False
logger = Logger("main.log")
config = configuration("config.ini")
DEBUG = config["application"]["debug"] == "true"
if not DEBUG:
    logger.update_level(WARNING)
queries_manager = load_queries()
db_connection = DatabaseConnection(config["postgresql"])
destructive_query = queries_manager["drop_all"]
if DEBUG:
    db_connection.execute_query(destructive_query)
    print("old tables dropped")
db_connection.execute_query(queries_manager["users_table"], debug=DEBUG)
db_connection.execute_query(queries_manager["reviews_table"], debug=DEBUG)
db_connection.execute_query(queries_manager["authors_table"], debug=DEBUG)
db_connection.execute_query(queries_manager["books_table"], debug=DEBUG)
if DEBUG:
    add_data()


@app.route('/')
def index():
    """main page"""
    query = queries_manager["select_some_books"]
    books_list = []
    result = db_connection.execute_query(query)
    for book_data in result:
        current_book = BookExpressEntry(book_data[0], book_data[1], book_data[2])
        books_list.append(current_book)
    if result is None:
        result = str(result)
    return render_template("index.html", top_book_list=books_list)


@app.route('/books/<author>/<book>')
def book(author: str, book: str):
    """return book page"""
    query = queries_manager["select_book"]
    book, author = book.replace("_", " "), author.replace("_", " ")
    query_data = (book, author)
    result = db_connection.execute_query(query, query_data)[0]
    template_data = dict()
    template_data["author"] = result[0]
    template_data["book"] = book
    template_data["duedate"] = result[1]
    template_data["language"] = result[2]
    template_data["pages"] = result[3]
    template_data["description"] = result[4]
    template_data["wikilink"] = result[5]
    template_data["rating"] = result[6]
    template_data["viewerscounter"] = result[7]
    template_data["downloadscounter"] = result[8]
    template_data["epubsize"] = result[9]
    template_data["pdfsize"] = result[10]
    return render_template("book.html", **template_data)


@app.route("/favicon.ico")
def favicon():
    """favicon picture"""
    return redirect(url_for("favicon.ico"))


@app.errorhandler(HTTPException)
def http_error_handler(error):
    '''http error page'''
    return render_template("error.html", error=error), error.code


@app.errorhandler(Exception)
def other_error_handler(error):
    '''system error handler. returns internal server error http code'''
    return render_template("error.html", error=error), 500


if DEBUG:
    app.run(debug=True)
else:
    serve(app, host="127.0.0.1", port=5000)
