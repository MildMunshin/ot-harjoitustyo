from src.repositories.exercise_repository import exercise_repository as default_exercise_repository
from src.entities.exercise import Exercise


class ExerciseService:
    def __init__(self, exercise_repository=default_exercise_repository):
        self._exercise_repository = exercise_repository
        self._exercise = None

    # Ai code begins
    def create_exercise(self, day_id, name, sets, reps, weight):
        exercise = self._exercise_repository.create(
            Exercise(None, day_id, name, sets, reps, weight)
        )
        return exercise

    def get_exercises_by_day(self, day_id):
        return self._exercise_repository.find_by_day(day_id)
    # Ai code ends


exercise_service = ExerciseService()
