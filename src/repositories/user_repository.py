from src.entities.user import User
from src.database_connection import get_database_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return [User(row["username"], row["password"]) for row in rows]

    def create(self, user: User):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()
        return user

    def find_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )
        row = cursor.fetchone()

        if row:
            return User(row["username"], row["password"])

        return None


user_repository = UserRepository(get_database_connection())
users = user_repository.find_all()
