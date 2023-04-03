#!usr/bin/env python3
import os
from pprint import pprint
from logging import info, error, warning
from functions import configuration, Logger
from database import load_queries, DatabaseConnection


def add_data(debug: bool):
    logger = Logger(filename="add_data.log", logging_level=debug)
    if debug:
        config = "example_data.ini"
    else:
        config = "data.ini"
    config = configuration(config)
    database_config = configuration("config.ini")["postgresql"]
    queries_manager = load_queries()
    db_connection = DatabaseConnection(database_config)
    for element in config.sections():
        if element == "author":
            try:
                query_data = {"name": config[element]["name"]}
            except KeyError as e:
                error("minimal author data is not provided")
                raise e
            try:
                birthday = config[element]["birthday"]
                query_data["birthday"] = birthday
                info("birthday loaded")
            except KeyError:
                query_data["birthday"] = None
                warning("author's birthday is not loaded")
            try:
                nationality = config[element]["nationality"]
                query_data["nationality"] = nationality
                info("nationality loaded")
            except KeyError:
                query_data["nationality"] = None
                warning("author's nationality is not loaded")
            try:
                description_file = config[element]["description"]
                with open(description_file, encoding="utf-8") as file:
                    description = file.read()
                query_data["description"] = description
                info("author description loaded")
            except KeyError:
                query_data["description"] = None
                warning("author's description is not configured")
            except FileNotFoundError:
                query_data["description"] = None
                error("provided author's description file does not exist")
            try:
                wikilink = config[element]["wikilink"]
                query_data["wikilink"] = wikilink
                info("author's wikilink loaded")
            except KeyError:
                query_data["wikilink"] = None
                warning("author's wikilink is not loaded")
        elif element == "book":
            try:
                query_data = {"name": config[element]["name"],
                              "author": config[element]["author"],
                              "downloadscounter": 0,
                              "viewerscounter": 0,
                              "rating": None}
                info("minimal book data loaded")
            except KeyError as e:
                error("minimal book data is not provided")
                raise e
            try:
                duedate = config[element]["duedate"]
                query_data["duedate"] = duedate
                info("book date data loaded")
            except KeyError:
                query_data["duedate"] = None
                warning("book date is not configured")
            try:
                language = config[element]["language"]
                query_data["language"] = language
                info("book language loaded")
            except KeyError:
                query_data["language"] = None
                warning("book language is not configured")
            try:
                pages_number = config[element]["pages"]
                query_data["pages"] = int(pages_number)
                info("book pages number loaded")
            except KeyError:
                query_data["pages"] = None
                warning("book pages number is not configured")
            try:
                genre = config[element]["genre"]
                query_data["genre"] = genre
                info("book genre loaded")
            except KeyError:
                query_data["genre"] = None
                warning("book genre is not configured")
            try:
                description_file = config[element]["description"]
                with open(description_file, encoding="utf-8") as file:
                    description = file.read()
                query_data["description"] = description
                info("book description loaded")
            except KeyError:
                query_data["description"] = None
                warning("book description is not configured")
            except FileNotFoundError:
                query_data["description"] = None
                error("provided book description file does not exist")
            try:
                wikilink = config[element]["wikilink"]
                query_data["wikilink"] = wikilink
                info("book wikilink loaded")
            except KeyError:
                query_data["wikilink"] = None
                warning("book wiki link is not configured")
            try:
                epub_file = config[element]["epub"]
                with open(epub_file, "rb") as bytestream:
                    contents = bytestream.read()
                    query_data["epub"] = contents  
                info("book epub file loaded")
                query_data["epubsize"] = len(contents)
                info("book eoub file size loaded")
            except KeyError:
                query_data["epub"] = None
                query_data["epubsize"] = None
                warning("book epub file is not configured")
            except FileNotFoundError:
                query_data["epub"] = None
                query_data["epubsize"] = None
                info("provided epub file does not exist")
            try:
                pdf_file = config[element]["pdf"]
                with open(pdf_file, "rb") as bytestream:
                    contents = bytestream.read()
                    print(type(contents))
                    query_data["pdf"] = contents
                info("book pdf file loaded")
                query_data["pdfsize"] = len(contents)
                info("book pdf file size loaded")
            except KeyError:
                query_data["pdf"] = None
                query_data["pdfsize"] = None
                warning("book pdf file is not configured")
            except FileNotFoundError:
                query_data["pdf"] = None
                query_data["pdfsize"] = None
                info("provided pdf file does not exist")
            queries_manager = load_queries()
            query = queries_manager["add_book"]
            db_connection.execute_query(query, query_data)


if __name__ == "__main__":
    add_data(debug=True)
