import unittest
from src.services.day_service import DayService
from src.services.exercise_service import ExerciseService
from src.services.user_service import UserService
from src.entities.user import User
from src.entities.exercise import Exercise
from src.entities.day import Day

from src.repositories.user_repository import user_repository
from src.repositories.exercise_repository import exercise_repository
from src.repositories.day_repository import day_repository
from src.initialize_database import initialize_database


class TestCreateDay(unittest.TestCase):

    def setUp(self):
        # The test now wipes out the whole database also outside the test. Going to fix that later
        initialize_database()
        self.user_service = UserService()
        self.day_service = DayService()

    def test_create_day(self):
        self.user_service.create_user("Test-Matthew", "testpassword123")
        self.day_service.create_day("Test-Matthew", "Day 1")
        testday = self.day_service.get_days_by_user("Test-Matthew")
        print(
            f"Username: {testday[0].username}, Day Name: {testday[0].day_name}")
        self.assertEqual(testday[0].day_name, "Day 1")
