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



class TestDeleteExercise(unittest.TestCase):

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

    def test_delete_exercise(self):
        self.user_service.create_user(
            "Test-Matthew", "testpassword123", "testpassword123")
        self.day_service.create_day("Test-Matthew", "Day 1")

        testday = self.day_service.get_days_by_user("Test-Matthew")
        day_id = testday[0].id

        self.exercise_service.create_exercise(day_id, "Deadlift", 3, 6, 90.0)
        test_exercise = self.exercise_service.get_exercises_by_day(day_id)
        self.assertEqual(test_exercise[0].name, "Deadlift")

        self.exercise_service.delete_exercise(test_exercise[0].id)
        new_exercise_search = self.exercise_service.get_exercises_by_day(
            day_id)
        self.assertEqual(new_exercise_search, [])
