from src.repositories.exercise_repository import exercise_repository as default_exercise_repository
from src.entities.exercise import Exercise


class ExerciseService:
    """Harjoitteiden käsittelyyn liittyvästä sovelluslogiikasta vastaava luokka.
    """

    def __init__(self, exercise_repository=default_exercise_repository):
        self._exercise_repository = exercise_repository
        # self._exercise = None
        """Luokan konstruktori, joka luo harjoitteisiin liittyvästä sovelluslogiikasta vastaavan palvelun.

        Args:
            exercise_repository: Olio, jolla on ExerciseRepository-luokkaa vastaavat metodit.
        """        

    
    # Ai code begins
    def create_exercise(self, day_id, name, sets, reps, weight):
        """Luo uuden harjoitteen.

        Args:
            day_id: Kokonaisluku, joka kuvaa uniikkia id-tunnistetta päivälle, johon harjoite luodaan.
            name: Merkkijono, joka kuvaa harjoitteen nimeä.
            sets: Kokonaisluku, joka kuvaa sarjojen määrää.
            reps: Kokonaisluku, joka kuvaa toistojen määrää.
            weight: Liukuluku, joka kuvaa käytettävän painon määrää.
        Returns:
            Palauttaa luodun harjoite-olion.
        """

        exercise = self._exercise_repository.create(
            Exercise(None, day_id, name, sets, reps, weight)
        )
        return exercise

    def get_exercises_by_day(self, day_id):
        """Palauttaa kaikki halutun päivän sisältämät harjoitteet.

        Args:
            day_id: Kokonaisluku, joka kuvaa päivän uniikkia id-tunnusta.
        Returns:
            Palauttaa kaikki päivän sisältämät harjoitteet.
        """    

        return self._exercise_repository.find_by_day(day_id)
    # Ai code ends


    def delete_exercise(self, exercise_id):
        self._exercise_repository.delete(exercise_id)
        """Poistaa valitun harjoitteen.

        Args:
            exercise_id: Kokonaisluku, joka kuvaa harjoitteen uniikkia id-tunnusta.
        """        

    def update_exercise(self, exercise_id, day_id, name, sets, reps, weight):
        """Päivittää valitun harjoitteen arvoja.

        Args:
            exercise_id: Kokonaisluku, joka kuvaa harjoitteen uniikkia id-tunnusta.
            day_id: Kokonaisluku, joka kuvaa uniikkia id-tunnistetta päivälle, johon harjoite luodaan.
            name: Merkkijono, joka kuvaa harjoitteen nimeä.
            sets: Kokonaisluku, joka kuvaa sarjojen määrää.
            reps: Kokonaisluku, joka kuvaa toistojen määrää.
            weight: Liukuluku, joka kuvaa käytettävän painon määrää.

        Returns:
            Palauttaa päivitetyn harjoite-olion.
        """    

        exercise = self._exercise_repository.update(
            Exercise(exercise_id, day_id, name, sets, reps, weight)
        )
        return exercise

exercise_service = ExerciseService()
