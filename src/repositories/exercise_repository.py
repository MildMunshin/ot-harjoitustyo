from src.entities.exercise import Exercise
from src.database_connection import get_database_connection


class ExerciseRepository:
    """Harjoitteisiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self._connection = connection

    def create(self, exercise: Exercise):
        """Luo uuden harjoitteen.

        Args:
            exercise: Tallennettava Exercise-olio.

        Returns:
            Palauttaa luodun Exercise-olion.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO exercises (day_id, name, sets, reps, weight) VALUES (?, ?, ?, ?, ?)",
            (exercise.day_id, exercise.name,
             exercise.sets, exercise.reps, exercise.weight)
        )

        self._connection.commit()
        exercise.id = cursor.lastrowid

        return exercise

    def find_by_day(self, day_id):
        """Palauttaa valittuun päivään liittyvät harjoitteet.

        Args:
            day_id: Kokonaisluku, joka kuvaa päivän uniikkia id-tunnusta.

        Returns:
            Palauttaa päivään liittyvät harjoitteet.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT id, day_id, name, sets, reps, weight FROM exercises WHERE day_id = ?",
            (day_id,)
        )
        rows = cursor.fetchall()

        return [
            Exercise(
                row["id"],
                row["day_id"],
                row["name"],
                row["sets"],
                row["reps"],
                row["weight"]) for row in rows]

    def delete(self, exercise_id):
        """Poistaa valitun harjoitteen.

        Args:
            exercise_id: Kokonaisluku, joka kuvaa harjoitteen uniikkia id-tunnusta.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM exercises WHERE id = ?",
            (exercise_id,)
        )

        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM exercises")

        self._connection.commit()

    # AI code starts here
    def update(self, exercise):
        """Päivittää harjoitteen arvoja.

        Args:
            exercise: Exercise-olio.

        Returns:
            Palauttaa päivitetyn Exercise-olion.
        """

        self._connection.execute(
            """
            UPDATE exercises
            SET day_id = ?, name = ?, sets = ?, reps = ?, weight = ?
            WHERE id = ?
            """,
            (exercise.day_id, exercise.name, exercise.sets,
             exercise.reps, exercise.weight, exercise.id)
        )
        self._connection.commit()
        return exercise
    # AI code ends here

exercise_repository = ExerciseRepository(get_database_connection())
