import sqlite3
import unittest

from src.services.user_service import UserService
from src.repositories.user_repository import UserRepository
from src.entities.user import User

class TestCreateUser(unittest.TestCase):

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

        self.user_repository = UserRepository(self.connection)
        self.service = UserService(self.user_repository)


    def test_create_user(self):
        self.service.create_user(
            "Test-Matthew", "testpassword123", "testpassword123")
        testuser = self.service._user_repository.find_by_username(
            "Test-Matthew")
        print(f"Username: {testuser.username}, Password: {testuser.password}")
        self.assertEqual(("Test-Matthew", "testpassword123"),
                         (testuser.username, testuser.password))