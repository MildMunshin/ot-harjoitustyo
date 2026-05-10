class Exercise:
    """Luokka, joka kuvaa yksittäistä harjoitetta.

    Attributes:
        id: Kokonaisluku, joka kuvaa harjoitteen uniikkia id-tunnusta.
        day_id: Kokonaisluku, joka kuvaa uniikkia id-tunnusta sille päivälle, johon harjoite kuuluu.
        name: Merkkijono, joka kuvaa harjoitteen nimeä.
        sets: Kokonaisluku, joka kuvaa sarjojen määrää.
        reps: Kokonaisluku, joka kuvaa toistojen määrää.
        weight: Liukuluku, joka kuvaa käytettävää painoa.
    """

    def __init__(self, exercise_id, day_id, name, sets, reps, weight):
        """Luo uuden harjoitteen.

        Args:
            exercise_id: Harjoitteen uniikki id-tunnus.
            day_id: Päivän uniikki id-tunnus.
            name: Harjoitteen nimi.
            sets: Sarjojen määrä.
            reps: Toistojen määrä.
            weight: Käytettävä paino.
        """

        self.id = exercise_id
        self.day_id = day_id
        self.name = name
        self.sets = sets
        self.reps = reps
        self.weight = weight
