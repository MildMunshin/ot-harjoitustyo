# import unittest
# from src.services.user_service import UserService
# from src.entities.user import User
# from src.repositories.user_repository import user_repository
# from src.repositories.day_repository import day_repository
# from src.repositories.exercise_repository import exercise_repository


# class TestUserLogin(unittest.TestCase):

#     def setUp(self):
#         exercise_repository.delete_all()
#         day_repository.delete_all()
#         user_repository.delete_all()
#         self.service = UserService()

#     def test_create_user(self):
#         self.service.create_user(
#             "Test-Matthew", "testpassword123", "testpassword123")
#         this_should_return_user = self.service.login(
#             "Test-Matthew", "testpassword123")
#         print(this_should_return_user.username,
#               this_should_return_user.password)
#         self.assertEqual(("Test-Matthew", "testpassword123"),
#                          (this_should_return_user.username, this_should_return_user.password))
