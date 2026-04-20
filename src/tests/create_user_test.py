import unittest
from src.services.user_service import UserService
from src.entities.user import User
from src.repositories.user_repository import user_repository
from src.initialize_database import initialize_database


class TestCreateUser(unittest.TestCase):

    def setUp(self):
        # The test now wipes out the whole database also outside the test. Going to fix that later
        initialize_database()
        self.service = UserService()

    def test_create_user(self):
        self.service.create_user(
            "Test-Matthew", "testpassword123", "testpassword123")
        testuser = self.service._user_repository.find_by_username(
            "Test-Matthew")
        print(f"Username: {testuser.username}, Password: {testuser.password}")
        self.assertEqual(("Test-Matthew", "testpassword123"),
                         (testuser.username, testuser.password))
