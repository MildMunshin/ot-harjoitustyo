import sqlite3
import unittest

from src.services.user_service import UserService, UsernameTooShortError, PasswordTooShortError, PasswordsDoNotMatchError, UsernameExistsError
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

    def test_username_too_short(self):
        with self.assertRaises(UsernameTooShortError):
            self.service.create_user(
                "Test", "testpassword123", "testpassword123")
            
        failed_user = self.service._user_repository.find_by_username(
            "Test")
        self.assertIsNone(failed_user)

    def test_username_too_short(self):
        with self.assertRaises(PasswordTooShortError):
            self.service.create_user(
                "Test-Matthew", "test", "test")
            
        failed_user = self.service._user_repository.find_by_username(
            "Test-Matthew")
        self.assertIsNone(failed_user)

    def test_passwords_do_not_match(self):
        with self.assertRaises(PasswordsDoNotMatchError):
            self.service.create_user(
                "Test-Matthew", "testpassword123", "testpassword12345")

        failed_user = self.service._user_repository.find_by_username(
            "Test-Matthew")
        self.assertIsNone(failed_user)

    def test_username_already_exists(self):
        self.service.create_user(
            "Test-Hammo", "testpassword12345", "testpassword12345")
        with self.assertRaises(UsernameExistsError):
            self.service.create_user(
                "Test-Hammo", "testpassword12345", "testpassword12345")

    def test_create_user(self):
        self.service.create_user(
            "Test-Matthew", "testpassword123", "testpassword123")
        testuser = self.service._user_repository.find_by_username(
            "Test-Matthew")
        print(f"Username: {testuser.username}, Password: {testuser.password}")
        self.assertEqual(("Test-Matthew", "testpassword123"),
                         (testuser.username, testuser.password))
