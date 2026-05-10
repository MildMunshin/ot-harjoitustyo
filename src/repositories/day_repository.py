from src.entities.day import Day
from src.database_connection import get_database_connection


class DayRepository:
    """Päiviin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self._connection = connection

    def create(self, day: Day):
        """Luo uuden päivän.

        Args:
            day: tallennettava Day-olio.

        Returns:
            Palauttaa Day-olion.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO days (username, day_name) VALUES (?, ?)",
            (day.username, day.day_name)
        )

        self._connection.commit()
        return day

    def find_by_username(self, username):
        """Palauttaa käyttäjän päivät.

        Args:
            username: Merkkijono, joka kuvaa käyttäjän käyttäjänimeä.

        Returns:
            Palauttaa käyttäjän luomat päivät.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT id, username, day_name FROM days WHERE username = ?",
            (username,)
        )
        rows = cursor.fetchall()
        return [Day(row["id"], row["username"], row["day_name"]) for row in rows]

    def delete_day(self, day):
        """Poistaa valitun päivän.

        Args:
            day: poistettava Day-olio.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM days WHERE id = ?",
            (day.id,)
        )

        self._connection.commit()

    def delete_all(self):

        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM days"
        )

        self._connection.commit()

day_repository = DayRepository(get_database_connection())
