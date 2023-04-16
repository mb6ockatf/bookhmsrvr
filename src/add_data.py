#!usr/bin/env python3
import os
from logging import info, error, warning, DEBUG
from functions import configuration, Logger
from database import load_queries, DatabaseConnection


def add_data():
    logger = Logger(filename="add_data.log", logging_level=DEBUG)
    config = "data.ini"
    config = configuration(config)
    database_config = configuration("config.ini")["postgresql"]
    queries_manager = load_queries()
    db_connection = DatabaseConnection(database_config)
    for element in config.sections():
        if element == "author":
            try:
                query_data = [config[element]["name"],]
            except KeyError as e:
                error("minimal author data is not provided")
                raise e
            try:
                birthday = config[element]["birthday"]
                if birthday == "":
                    query_data.append("01.01.0001")
                else:
                    query_data.append(birthday)
                info("birthday loaded")
            except KeyError:
                query_data.append("01.01.0001")
                warning("author's birthday is not loaded")
            try:
                nationality = config[element]["nationality"]
                if nationality == "":
                    query_data.append(None)
                else:
                    query_data.append(nationality)
                info("nationality loaded")
            except KeyError:
                query_data.append(None)
                warning("author's nationality is not loaded")
            query_data.append(1)  # viewscounter
            try:
                description_file = config[element]["description"]
                with open(description_file, encoding="utf-8") as file:
                    description = file.read()
                query_data.append(description)
                info("author description loaded")
            except KeyError:
                print("keyerror in desc")
                query_data.append(None)
                warning("author's description is not configured")
            except FileNotFoundError:
                print("fileerror in desc")
                query_data.append(None)
                error("provided author's description file does not exist")
            try:
                wikilink = config[element]["wikilink"]
                if wikilink == "":
                    query_data.append(None)
                else:
                    query_data.append(wikilink)
                info("author's wikilink loaded")
            except KeyError:
                query_data.append(None)
                warning("author's wikilink is not loaded")
            queries_manager = load_queries()
            query = queries_manager["add_author"]
            db_connection.execute_query(query, query_data)
            info("BOOK ADDED SUCCESSFULLY")
        elif element == "book":
            print(element)
            try:
                name = config[element]["name"].replace("_", " ")
                author = config[element]["author"].replace("_", " ")
                query_data = [name, author,]
                info("name and author loaded")
            except KeyError as e:
                error("minimal book data is not provided")
                raise e
            try:
                duedate = config[element]["duedate"]
                if duedate == "":
                    query_data.append("01.01.0001")
                else:
                    query_data.append(duedate)
                info("book date data loaded")
            except KeyError:
                query_data.append("01.01.0001")
                warning("book date is not configured")
            try:
                language = config[element]["language"]
                query_data.append(language)
                info("book language loaded")
            except KeyError:
                query_data.append(None)
                warning("book language is not configured")
            try:
                pages_number = config[element]["pages"]
                query_data.append(int(pages_number))
                info("book pages number loaded")
            except KeyError:
                query_data.append(None)
                warning("book pages number is not configured")
            try:
                genre = config[element]["genre"]
                query_data.append(genre)
                info("book genre loaded")
            except KeyError:
                query_data.append(None)
                warning("book genre is not configured")
            try:
                description_file = config[element]["description"]
                with open(description_file, encoding="utf-8") as file:
                    description = file.read()
                query_data.append(description)
                info("book description loaded")
            except KeyError:
                query_data.append(None)
                warning("book description is not configured")
            except FileNotFoundError:
                query_data.append(None)
                error("provided book description file does not exist")
            try:
                wikilink = config[element]["wikilink"]
                query_data.append(wikilink)
                info("book wikilink loaded")
            except KeyError:
                query_data.append(None)
                warning("book wiki link is not configured")
            query_data.append(0)  # rating
            query_data.append(1)  # viewerscounter
            query_data.append(1)  # downloadscounter
            try:
                epub_file = config[element]["epub"]
                with open(epub_file, "rb") as bytestream:
                    contents = bytestream.read()
                    query_data.append(contents)
                info("book epub file loaded")
                query_data.append(len(contents))
                info("book eoub file size loaded")
            except KeyError:
                query_data.appned([None, None])
                warning("book epub file is not configured")
            except FileNotFoundError:
                for _ in range(2):
                    query_data.append(None)
                info("provided epub file does not exist")
            try:
                pdf_file = config[element]["pdf"]
                with open(pdf_file, "rb") as bytestream:
                    contents = bytestream.read()
                    query_data.append(contents)
                info("book pdf file loaded")
                query_data.append(len(contents))
                info("book pdf file size loaded")
            except KeyError:
                for _ in range(2):
                    query_data.append(None)
                warning("book pdf file is not configured")
            except FileNotFoundError:
                for _ in range(2):
                    query_data.append(None)
                info("provided pdf file does not exist")
            queries_manager = load_queries()
            query = queries_manager["add_book"]
            db_connection.execute_query(query, query_data)
            info("BOOK ADDED SUCCESSFULLY")


if __name__ == "__main__":
    add_data()
