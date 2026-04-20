from src.repositories.day_repository import day_repository as default_day_repository
from src.entities.day import Day


class DayService:
    def __init__(self, day_repository=default_day_repository):
        self._day_repository = day_repository

    def create_day(self, username, day_name):
        self._day_repository.create(Day(None, username, day_name))
        # "None" added/fixed by AI

    def get_days_by_user(self, username):
        return self._day_repository.find_by_username(username)

    def delete_day(self, day):
        self._day_repository.delete_day(day)


day_service = DayService()
