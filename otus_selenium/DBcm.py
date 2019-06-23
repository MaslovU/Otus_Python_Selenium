"""Helper"""
import mysql.connector


class ConnectionError(Exception):
    """Custom Error"""
    pass


class CredentialsError(Exception):
    """Custom Error"""
    pass


class SQLError(Exception):
    """Custom Error"""
    pass


class UseDatabase:
    """Use Database"""
    def __init__(self, config: dict):
        """Init"""
        self.configuration = config

    def __enter__(self) -> "cursor":
        """Enter"""
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err)
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err)

    def __exit__(self, exc_type, exc_value, exc_trace):
        """Exit"""
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)
