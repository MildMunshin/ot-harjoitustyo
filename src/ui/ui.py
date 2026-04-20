from tkinter import Tk, ttk, constants
from src.services.user_service import user_service, UsernameExistsError, InvalidCredentialsError
from src.ui.login_view import LoginView
from src.ui.user_view import UserView
from src.ui.day_view import DayView
from src.ui.exercises_view import ExercisesView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _show_login_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = LoginView(
            self._root,
            self._handle_login,
            self._show_create_user_view
        )
        self._current_view.pack()

    def _show_create_user_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = UserView(
            self._root,
            self._handle_create_user,
            self._show_login_view
        )
        self._current_view.pack()

    def _show_exercises_view(self, day):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = ExercisesView(
            self._root,
            day,
            self._show_day_view,
        )
        self._current_view.pack()

    def _show_day_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = DayView(
            self._root,
            self._show_login_view,
            self._show_exercises_view,
            self._current_user
        )
        self._current_view.pack()

    def _handle_login(self, username, password):
        try:
            user = user_service.login(username, password)
            self._current_user = user
            print("Login success")
            self._show_day_view()
        except InvalidCredentialsError:
            print("Invalid username or password")

    def _handle_create_user(self, username, password, password2):
        try:
            user_service.create_user(username, password, password2)
            print("User created")
            self._show_login_view()
        except UsernameExistsError:
            print("Username already exists")
