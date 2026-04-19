from src.repositories.user_repository import user_repository as default_user_repository
from src.entities.user import User

class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class UsernameTooShortError(Exception):
    pass

class PasswordTooShortError(Exception):
    pass

class PasswordsDoNotMatch(Exception):
    pass

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository
        self._user = None

    def create_user(self, username, password, password2, login=True):

        if len(username) < 5:
            print("username is too short")
            raise UsernameTooShortError
        
        if password != password2:
            print("passwords don't match")
            raise PasswordsDoNotMatch

        if len(password) < 5:
            print("password is too short")
            raise PasswordTooShortError

        existing = self._user_repository.find_by_username(username)

        if existing:
            print("username already exists")
            raise UsernameExistsError
        
        user = self._user_repository.create(User(username, password))
        if login:
            self._user = user
            print(username, password, login)
        return user

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError()

        self._user = user
        return user


user_service = UserService()
