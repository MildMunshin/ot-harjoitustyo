import unittest
from src.services.user_service import UserService
from src.entities.user import User
from src.repositories.user_repository import user_repository
from src.initialize_database import initialize_database


class TestUserLogin(unittest.TestCase):

    def setUp(self):
        # The test now wipes out the whole database also outside the test. Going to fix that later
        initialize_database()
        self.service = UserService()

    def test_create_user(self):
        self.service.create_user(
            "Test-Matthew", "testpassword123", "testpassword123")
        this_should_return_user = self.service.login(
            "Test-Matthew", "testpassword123")
        print(this_should_return_user.username,
              this_should_return_user.password)
        self.assertEqual(("Test-Matthew", "testpassword123"),
                         (this_should_return_user.username, this_should_return_user.password))
