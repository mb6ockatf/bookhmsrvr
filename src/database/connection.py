import os
from logging import info, critical, error
from psycopg2 import connect


class DatabaseConnection:
    """
    handle database connection: open, close
    execute passed queries
    """
    def __init__(self, connection_config: dict):
        try:
            self.connection = connect(**connection_config)
            info_message = "database connection successfully initialized"
            info(info_message)
        except BaseException as e:
            critical_message = "database connection failed to initialize "
            critical_message += "with these settings: "
            critical_message += str(connection_config)
            critical(critical_message)
            raise e

    def execute_query(self, query: str, data=None, debug=False) -> tuple:
        """
        execute SQL query with given params if some
        raise critical exception on error
        """
        result = None
        cursor = self.connection.cursor()
        try:
            if data:
                cursor.execute(query, data)
                result = cursor.fetchall()
            else:
                if debug:
                    info(query)
                cursor.execute(query)
        except BaseException as e:
            self.close()
            critical_message = "query failed to execute:\n"
            critical_message += str(query)
            critical(critical_message)
            raise e
        self.connection.commit()
        cursor.close()
        return result

    def close(self):
        """close database connection"""
        try:
            self.connection.close()
            info("database connection successfully closed")
        except BaseException as e:
            critical("database connection failed to close")
            raise e


class QueriesManager:
    """
    preload & store SQL queries
    this object is supposed to be initialized with load_queries function (see
    below)
    """
    def __init__(self):
        self._queries = {}

    def add_query(self, path: str, name: str):
        """
        load SQL queries from files, and store them
        """
        try:
            with open(path, "r", encoding="utf-8") as file:
                contents = file.read()
            self._queries[name] = contents
            info(f"query {name}: contents successfully loaded")
        except FileNotFoundError as e:
            error(f"query {name}: file not found - " + str(e))
        except BaseException as e:
            error(f"query {name}: contents failed to load - " + str(e))

    def __getitem__(self, query_name: str) -> str:
        try:
            result = self._queries[query_name]
            info(query_name + " was successfully returned by QueryManager")
            return result
        except KeyError:
            error_message = str(query_name) + " failed to be found\n"
            error_message += "whether it has been tried to access in a wrong "
            error_message += "way, or it is not present in query manager yet"
            error(error_message)
        except BaseException as e:
            error_message = str(query_name) + " failed to be accessed: "
            error_message += str(e)

    def __setitem__(self, query_name: str, path: str) -> str:
        """more convenient way of adding queries"""
        return self.add_query(path, query_name)

    def items(self):
        """
        convenient iterator - so object looks more like a simple dictionary
        """
        for name, query in self._queries.items():
            yield name, query

    def __str__(self) -> str:
        """pretty print the object - for debugging purposes"""
        result = []
        result.append("QueriesManager")
        for query_name, query in self._queries.items():
            shortened_query = query.split()[0]
            buffer = f"\t{query_name}: {shortened_query}...;"
            result.append(buffer)
        result = "\n".join(result)
        return result


def load_queries() -> QueriesManager:
    """add all SQL queries from `queries` directory to QueriesManager"""
    base_path = "src/database/queries/"
    manager = QueriesManager()
    for root, dirs, files in os.walk(base_path):
        for name in files:
            nice_name = name.split(".")[0]
            manager[nice_name] = os.path.join(root, name)
    return manager
