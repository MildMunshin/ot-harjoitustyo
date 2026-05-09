class InvalidCredentialsError(Exception):
    pass
    """Luokka, joka ilmoittaa väärästä käyttäjänimestä tai salasanasta.
    """


class UsernameExistsError(Exception):
    pass
    """Luokka, joka ilmoittaa olemassa olevasta käyttäjänimestä.
    """


class UsernameTooShortError(Exception):
    pass
    """Luokka, joka ilmoittaa liian lyhyestä käyttäjänimestä.
    """


class PasswordTooShortError(Exception):
    pass
    """Luokka, joka ilmoittaa liian lyhyestä salasanasta.
    """


class PasswordsDoNotMatchError(Exception):
    pass
    """Luokka, joka ilmoittaa jos salasanat eivät täsmää käyttäjän luomisen yhteydessä.
    """