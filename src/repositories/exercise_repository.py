from src.entities.exercise import Exercise
from src.database_connection import get_database_connection

class ExerciseRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, exercise: Exercise):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO exercises (day_id, name, sets, reps, weight) VALUES (?, ?, ?, ?, ?)",
            (exercise.day_id, exercise.name,
             exercise.sets, exercise.reps, exercise.weight)
        )

        self._connection.commit()
        return exercise

    def find_by_day(self, day_id):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT id, day_id, name, sets, reps, weight FROM exercises WHERE day_id = ?",
            (day_id,)
        )
        rows = cursor.fetchall()

        return [Exercise(row["id"], row["day_id"], row["name"], row["sets"], row["reps"], row["weight"]) for row in rows]

exercise_repository = ExerciseRepository(get_database_connection())
