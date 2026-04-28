from src.entities.user import User
from src.database_connection import get_database_connection


class UserRepository:
    """Käyttäjiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self._connection = connection

    def find_all(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            Palauttaa kaikki User-oliot tietokannasta.
        """
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return [User(row["username"], row["password"]) for row in rows]

    def create(self, user: User):
        """Luo uuden käyttäjän.

        Args:
            user: User-olio.

        Returns:
            Palauttaa luodun User-olion.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()
        return user

    def find_by_username(self, username):
        """Palauttaa halutun käyttäjän.

        Args:
            username: Merkkijono, joka kuvaa käyttäjän käyttäjänimeä.

        Returns:
            Palauttaa haetun käyttäjän User-olion.
        """
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
