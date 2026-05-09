# import unittest

# from src.services.day_service import DayService
# from src.services.exercise_service import ExerciseService
# from src.services.user_service import UserService

# from src.entities.user import User
# from src.entities.exercise import Exercise
# from src.entities.day import Day

# from src.repositories.user_repository import user_repository
# from src.repositories.exercise_repository import exercise_repository
# from src.repositories.day_repository import day_repository



# class TestDeleteDay(unittest.TestCase):

#     def setUp(self):
#         day_repository.delete_all()
#         user_repository.delete_all()
#         self.user_service = UserService()
#         self.day_service = DayService()

#     def test_delete_day(self):
#         self.user_service.create_user(
#             "Test-Alice", "testpassword666", "testpassword666")
#         self.day_service.create_day("Test-Alice", "Pull Day")
#         testday = self.day_service.get_days_by_user("Test-Alice")
#         self.assertEqual(testday[0].day_name, "Pull Day")
#         self.day_service.delete_day(testday[0])
#         testdays = self.day_service.get_days_by_user("Test-Alice")
#         self.assertEqual(testdays, [])
