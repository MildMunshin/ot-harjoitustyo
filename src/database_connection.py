import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(
    dirname, "..", "data", "database.sqlite"))
connection.row_factory = sqlite3.Row

connection.execute("PRAGMA foreign_keys = ON")


def get_database_connection():
    return connection

# Code copied from the reference app starts here
# import sqlite3
# from config import DATABASE_FILE_PATH

# connection = sqlite3.connect(DATABASE_FILE_PATH)
# connection.row_factory = sqlite3.Row


# def get_database_connection():
#     return connection
# Code copied from the reference app ends here


# AI code starts here
# import os
# import sqlite3

# def get_database_connection(test=False):
#     if test:
#         connection = sqlite3.connect(":memory:")
#     else:
#         dirname = os.path.dirname(__file__)
#         connection = sqlite3.connect(os.path.join(
#             dirname, "..", "data", "database.sqlite"))

#     connection.row_factory = sqlite3.Row
#     connection.execute("PRAGMA foreign_keys = ON")
#     return connection
# AI code ends here