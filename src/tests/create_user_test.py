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

    # This is not really a test, just trying things out on my own
    # def test_show_users(self):
    #     users = self.service._user_repository.find_all()
    #     print("Users in database:")
    #     for user in users:
    #         print(f"Username: {user.username}, Password: {user.password}")

    def test_create_user(self): 
        self.service.create_user("Test-Matthew", "testpassword123")
        testuser = self.service._user_repository.find_by_username("Test-Matthew")
        print(f"Username: {testuser.username}, Password: {testuser.password}")
        self.assertEqual(("Test-Matthew", "testpassword123"),(testuser.username, testuser.password))
