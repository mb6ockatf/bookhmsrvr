from psycopg2 import connect


class DatabaseConnection:
    def __init__(self, connection_config: dict):
        try:
            self.connection = connect(**connection_config)
        except BaseException as error:
            print(error)

    def execute_query(self, query: str, data) -> tuple:
        cursor = self.connection.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        self.connection.commit()
        result = cursor.fetchall()
        cursor.close()
        return result

    def close(self):
        self.connection.close()
