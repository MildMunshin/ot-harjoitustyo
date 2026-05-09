# import unittest
# from src.services.user_service import UserService
# from src.entities.user import User
# from src.repositories.user_repository import user_repository
# from src.repositories.day_repository import day_repository
# from src.repositories.exercise_repository import exercise_repository


# class TestCreateUser(unittest.TestCase):

#     def setUp(self):
#         exercise_repository.delete_all()
#         day_repository.delete_all()
#         user_repository.delete_all()
#         self.service = UserService()

#     def test_create_user(self):
#         self.service.create_user(
#             "Test-Matthew", "testpassword123", "testpassword123")
#         testuser = self.service._user_repository.find_by_username(
#             "Test-Matthew")
#         print(f"Username: {testuser.username}, Password: {testuser.password}")
#         self.assertEqual(("Test-Matthew", "testpassword123"),
#                          (testuser.username, testuser.password))
