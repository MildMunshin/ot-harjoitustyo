import unittest
import sqlite3

from src.services.user_service import UserService, InvalidCredentialsError
from src.entities.user import User
from src.repositories.user_repository import UserRepository


class TestUserLogin(unittest.TestCase):

    def setUp(self):
        # AI code starts here
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row

        self.connection.execute("""
            CREATE TABLE users (
                username TEXT,
                password TEXT
            )
        """)
        # AI code ends here

        self.connection.execute('''
            create table days (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                day_name TEXT NOT NULL,
                FOREIGN KEY (username) REFERENCES users(username)
            )
        ''')

        self.connection.execute('''
            create table exercises (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                day_id INTEGER,
                name TEXT,
                sets INTEGER,
                reps INTEGER,
                weight REAL,
                FOREIGN KEY (day_id)
                    REFERENCES days(id)
                    ON DELETE CASCADE
            )
        ''')

        self.user_repository = UserRepository(self.connection)
        self.user_service = UserService(self.user_repository)

    def test_user_login(self):
        self.user_service.create_user(
            "Test-Matthew", "testpassword123", "testpassword123")
        this_should_return_user = self.user_service.login(
            "Test-Matthew", "testpassword123")
        print(this_should_return_user.username,
              this_should_return_user.password)
        self.assertEqual(("Test-Matthew", "testpassword123"),
                         (this_should_return_user.username, this_should_return_user.password))
        self.user_service.login("Test-Matthew", "testpassword123")

    def test_failed_login(self):
        self.user_service.create_user(
            "Test-Dork", "testpassword666", "testpassword666")
        with self.assertRaises(InvalidCredentialsError):
            self.user_service.login("Test-Matthew", "testpassword123")

    def test_wrong_password(self):
        self.user_service.create_user(
            "Test-Dork", "testpassword666", "testpassword666")
        with self.assertRaises(InvalidCredentialsError):
            self.user_service.login("Test-Dork", "testpassword444")