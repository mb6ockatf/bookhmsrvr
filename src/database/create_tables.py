"""
There are SQL queries that create necessary database tables if the do not exist
Also, broken tables might be dropped if they're corrupted
"""
from .connection import DatabaseConnection


class DatabaseCreateTable(DatabaseConnection):
    def create_table_book(self) -> tuple:
        """Create table for stoting book info"""
        query = """
        CREATE TABLE

