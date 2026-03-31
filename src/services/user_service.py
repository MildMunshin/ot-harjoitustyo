from src.repositories.user_repository import user_repository as default_user_repository
from src.entities.user import User

class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository
        self._user = None

    def create_user(self, username, password, login=True):

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