from src.entities.day import Day
from src.database_connection import get_database_connection


class DayRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, day: Day):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO days (username, day_name) VALUES (?, ?)",
            (day.username, day.day_name)
        )

        self._connection.commit()
        return day

    def find_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT id, username, day_name FROM days WHERE username = ?",
            (username,)
        )
        rows = cursor.fetchall()
        return [Day(row["id"], row["username"], row["day_name"]) for row in rows]


day_repository = DayRepository(get_database_connection())
