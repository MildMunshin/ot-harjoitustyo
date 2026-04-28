from src.repositories.day_repository import day_repository as default_day_repository
from src.entities.day import Day


class DayService:
    """Päivien käsittelyyn liittyvästä sovelluslogiikasta vastaava luokka.
    """

    def __init__(self, day_repository=default_day_repository):
        self._day_repository = day_repository
        """Luokan konstruktori, joka luo päiviin liittyvästä sovelluslogiikasta vastaavan palvelun.

        Args:
            day_repository: Olio, jolla on DayRepository-luokkaa vastaavat metodit.
        """

    def create_day(self, username, day_name):
        self._day_repository.create(Day(None, username, day_name))
        # "None" added/fixed by AI
        """Luo uuden päivän.

        Args:
            username: Merkkijono, joka kuvaa käyttäjänimeä, jolla päivä kuuluu.
            day_name: Merkkijono, joka kuvaa päivän nimeä.
        """

    def get_days_by_user(self, username):
        """Palauttaa kaikki käyttäjän päivät.

        Args:
            username: Merkkijono, joka kuvaa käyttän käyttäjänimeä.
        Returns:
            Palauttaa kaikki käyttäjän luomat päivät.
        """

        return self._day_repository.find_by_username(username)

    def delete_day(self, day):
        self._day_repository.delete_day(day)
        """Poistaa valitun päivän päivänäkymästä

        Args:
            day: Päivä-olio, jonka käyttäjä on valinnut poistettavaksi. 
        """


day_service = DayService()
