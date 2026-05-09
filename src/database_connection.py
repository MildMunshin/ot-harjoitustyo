import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(
    dirname, "..", "data", "database.sqlite"))
connection.row_factory = sqlite3.Row

connection.execute("PRAGMA foreign_keys = ON")


def get_database_connection():
    return connection

# AI code starts here
# DB_PATH = os.path.join(dirname, "..", "data", "database.sqlite")


# def get_database_connection(db_path=None):
#     path = db_path or DB_PATH
#     conn = sqlite3.connect(path)
#     conn.row_factory = sqlite3.Row
#     conn.execute("PRAGMA foreign_keys = ON")
    return conn
# AI code ends here