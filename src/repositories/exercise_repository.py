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

    def delete(self, exercise_id):
        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM exercises WHERE id = ?",
            (exercise_id,)
        )

        self._connection.commit()

    # AI code starts here
    def update(self, exercise):
        self._connection.execute(
            """
            UPDATE exercises
            SET day_id = ?, name = ?, sets = ?, reps = ?, weight = ?
            WHERE id = ?
            """,
            (exercise.day_id, exercise.name, exercise.sets, exercise.reps, exercise.weight, exercise.id)
        )
        self._connection.commit()
        return exercise
    # AI code ends here

exercise_repository = ExerciseRepository(get_database_connection())
