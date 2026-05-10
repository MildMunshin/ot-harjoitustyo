import unittest
import sqlite3
from unittest.mock import patch
from src.entities.user import User
from src.initialize_database import initialize_database, drop_tables, create_tables

class TestDoesDatabaseWork(unittest.TestCase):

    def setUp(self):

        # AI code starts here
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        # AI code ends here

    def test_does_database_work(self):
        # AI code starts here
        with patch("src.initialize_database.get_database_connection", return_value=self.connection):
        # AI code ends here

            drop_tables(self.connection)

            cursor = self.connection.cursor()

            # AI code starts here
            cursor.execute("""
                SELECT name FROM sqlite_master
                WHERE type='table' AND name='users'
            """)
            # AI code ends here

            table_users = cursor.fetchone()
            self.assertIsNone(table_users)

            cursor.execute("""
                SELECT name FROM sqlite_master
                WHERE type='table' AND name='days'
            """)

            table_days = cursor.fetchone()
            self.assertIsNone(table_days)

            cursor.execute("""
                SELECT name FROM sqlite_master
                WHERE type='table' AND name='exercises'
            """)

            table_exercises = cursor.fetchone()
            self.assertIsNone(table_exercises)

            create_tables(self.connection)

            cursor.execute("""
                SELECT name FROM sqlite_master
                WHERE type='table' AND name='users'
            """)

            table_users = cursor.fetchall()
            self.assertTrue(table_users)

            cursor.execute("""
                SELECT name FROM sqlite_master
                WHERE type='table' AND name='days'
            """)

            table_days = cursor.fetchall()
            self.assertIsNotNone(table_days)

            cursor.execute("""
                SELECT name FROM sqlite_master
                WHERE type='table' AND name='exercises'
            """)

            table_exercises = cursor.fetchall()
            self.assertIsNotNone(table_exercises)

            initialize_database()
