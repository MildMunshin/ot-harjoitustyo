import unittest
import sqlite3

from src.services.day_service import DayService
from src.services.exercise_service import ExerciseService
from src.services.user_service import UserService

from src.entities.user import User
from src.entities.exercise import Exercise
from src.entities.day import Day

from src.repositories.user_repository import UserRepository
from src.repositories.exercise_repository import ExerciseRepository
from src.repositories.day_repository import DayRepository


class TestDeleteAll(unittest.TestCase):

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

        self.day_repository = DayRepository(self.connection)
        self.user_repository = UserRepository(self.connection)
        self.exercise_repository = ExerciseRepository(self.connection)

        self.exercise_service = ExerciseService(self.exercise_repository)
        self.user_service = UserService(self.user_repository)
        self.day_service = DayService(self.day_repository)

    def test_delete_all(self):
        self.user_service.create_user(
            "Test-Richard", "testpassword12345", "testpassword12345")
        self.day_service.create_day("Test-Richard", "Pull Day")

        testday = self.day_service.get_days_by_user("Test-Richard")
        day_id = testday[0].id

        self.exercise_service.create_exercise(day_id, "Pull-up", 3, 6, 90.0)
        test_exercise = self.exercise_service.get_exercises_by_day(day_id)
        self.assertEqual(test_exercise[0].name, "Pull-up")

        self.exercise_repository.delete_all()
        second_exercise_search = self.exercise_service.get_exercises_by_day(
            day_id)
        self.assertEqual(second_exercise_search, [])

        self.day_repository.delete_all()
        day_search = self.day_service.get_days_by_user("Test-Richard")
        self.assertEqual(day_search, [])

        self.user_repository.delete_all()
        user_search = self.user_repository.find_all()
        self.assertEqual(user_search, [])