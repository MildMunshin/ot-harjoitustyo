# from database_connection import get_database_connection
# from repositories.user_repository import UserRepository
# from services.user_service import UserService, InvalidCredentialsError, UsernameExistsError
# from initialize_database import initialize_database

# initialize_database()

# def main():
#     connection = get_database_connection()

#     repo = UserRepository(connection)
#     service = UserService(repo)

#     username = "test"
#     password = "123"

#     try:
#         user = service.create_user(username, password)
#         print(f"Käyttäjä luotu: {user.username}")
#         print(f"Salasana: {user.password}")
#     except UsernameExistsError:
#         print(f"Käyttäjä '{username}' on jo olemassa!")

#     try:
#         user = service.login(username, password)
#         print(f"Kirjautuminen onnistui: {user.username}")
#         print(f"Salasana: {user.password}")
#     except InvalidCredentialsError:
#         print("Virheellinen käyttäjänimi tai salasana!")

# if __name__ == "__main__":
#     main()