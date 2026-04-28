class Day:

    """Luokka, joka kuvaa yksittäistä päivää.

    Attributes:
        id: Kokonaislukuarvo, joka kuvaa päivän unniikia id-tunnusta.
        username: Merkkijono, joka kuvaa kelle käyttäjälle päivä kuuluu.
        day_name: Merkkijono, joka muodostaa päivän nimen.
    """

    def __init__(self, day_id, username, day_name):
        self.id = day_id
        self.username = username
        self.day_name = day_name

        """Luokan konstruktori, joka luo uuden päivän.
        
        Args:
            id: Kokonaislukuarvo, joka kuvaa päivän unniikia id-tunnusta.
            username: Merkkijono, joka kuvaa kelle käyttäjälle päivä kuuluu.
            day_name: Merkkijono, joka muodostaa päivän nimen.
        """
