from src.repositories.user_repository import user_repository as default_user_repository
from src.entities.user import User

from src.errors.user_errors import (
    InvalidCredentialsError,
    UsernameExistsError,
    UsernameTooShortError,
    PasswordTooShortError,
    PasswordsDoNotMatchError
)


class UserService:
    """Käyttäjien käsittelyyn liittyvästä sovelluslogiikasta vastaava luokka.
    """

    def __init__(self, user_repository=default_user_repository):
        """Luokan konstruktori.

        Args:
            user_repository: Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """

        self._user_repository = user_repository
        self._user = None

    def create_user(self, username, password, password2, login=True):
        """Luo uuden käyttäjän.

        Args:
            username: Merkkijono, joka kuvaa käyttäjän nimimerkkiä
            password: Merkkijono, joka kuvaa käyttäjän salasanaa
            password2: Merkkijono, joka varmistaa, että käyttäjä on syöttänyt salasanan oikein.
            login: Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään
            onnistuneen luonnin jälkeen.

        Raises:
            UsernameTooShortError: Virhe, joka ilmoittaa liian lyhyestä käyttäjänimestä.
            PasswordsDoNotMatch: Virhe, joka ilmoittaa jos salasanat eivät täsmää käyttäjän
            luomisen yhteydessä.
            PasswordTooShortError: Virhe, joka ilmoittaa liian lyhyestä käyttäjänimestä.
            UsernameExistsError: Virhe, joka ilmoittaa olemassa olevasta käyttäjänimestä.

        Returns:
            Palauttaa luodun käyttäjän.
        """

        if len(username) < 5:
            # print("username is too short")
            raise UsernameTooShortError()

        if password != password2:
            # print("passwords don't match")
            raise PasswordsDoNotMatchError()

        if len(password) < 5:
            # print("password is too short")
            raise PasswordTooShortError()

        existing = self._user_repository.find_by_username(username)

        if existing:
            # print("username already exists")
            raise UsernameExistsError()

        user = self._user_repository.create(User(username, password))
        if login:
            self._user = user
            print(username, password, login)
        return user

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Merkkijono, joka kuvaa käyttäjän käyttäjänimeä.
            password: Merkkijono, joka kuvaa käyttäjän salasanaa.

        Returns:
            Palauttaa User-olion.
        """

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError()

        self._user = user
        return user


user_service = UserService()
