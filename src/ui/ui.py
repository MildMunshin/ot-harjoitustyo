from tkinter import Tk, ttk, constants, Frame, Label, messagebox
from src.services.user_service import user_service, UsernameExistsError, InvalidCredentialsError, UsernameTooShortError, PasswordTooShortError, PasswordsDoNotMatchError
from src.services.day_service import day_service
from src.ui.login_view import LoginView
from src.ui.user_view import UserView
from src.ui.day_view import DayView
from src.ui.exercises_view import ExercisesView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

        self._header = None
        self._sidebar = None
        self._container = None

    def start(self):
        self._build_layout()
        self._show_login_view()

    def _build_layout(self):
        # AI code starts here
        self._root.grid_rowconfigure(1, weight=1)
        self._root.grid_columnconfigure(1, weight=1)

        self._root.grid_columnconfigure(0, minsize=120)
        self._root.grid_columnconfigure(1, minsize=400)
        self._root.grid_rowconfigure(1, minsize=300)
        # AI code ends here

        # self._container.grid()

        # AI code starts here
        self._header = Frame(self._root, height=50, bg="red")
        self._header.grid(row=0, column=0, columnspan=2, sticky="ew")

        self._header.grid_columnconfigure(0, weight=1)
        self._header.grid_columnconfigure(1, weight=1)
        # AI code ends here

        # ttk.Button(
        #     self._header,
        #     text="Logout",
        #     command=self._show_login_view
        # ).grid(row=0, column=0, sticky="w", padx=10, pady=10)

        Label(
            self._header,
            text="GymMonsterApp",
            bg="red"
        ).grid(row=0, column=1, sticky="e", padx=10, pady=10)

        # AI code starts here
        self._sidebar = Frame(self._root, width=300, bg="gray")
        self._sidebar.grid(row=1, column=0, sticky="nsew")

        self._sidebar.grid_columnconfigure(0, weight=1)
        self._sidebar.grid_columnconfigure(1, weight=1)
        # self._sidebar.grid_columnconfigure(2, weight=1)

        self._container = ttk.Frame(self._root)
        self._container.grid(row=1, column=1, sticky="nsew")

        self._sidebar.grid_propagate(False)
        self._header.grid_propagate(False)

        # self._header.grid_remove()
        self._sidebar.grid_remove()

    def _render_header(self, mode):
        for child in self._header.winfo_children():
            child.destroy()

        if mode == "login":
            ttk.Button(
                self._header,
                text="Create User",
                command=self._show_create_user_view
            ).grid(row=0, column=0, sticky="w", padx=10, pady=10)

        elif mode == "app":
            ttk.Button(
                self._header,
                text="Logout",
                command=self._show_login_view
            ).grid(row=0, column=0, sticky="w", padx=10, pady=10)
            # AI code ends here

        elif mode == "create_user":
            ttk.Button(
                self._header,
                text="Back",
                command=self._show_login_view
            ).grid(row=0, column=0, sticky="w", padx=10, pady=10)

        # AI code starts here
        Label(
            self._header,
            text="GymMonsterApp",
            bg="red"
        ).grid(row=0, column=1, sticky="e", padx=10, pady=10)
        # AI code ends here

    def _show_login_view(self):
        # self._header.grid_remove()
        self._sidebar.grid_remove()

        if self._current_view:
            self._current_view.destroy()

        # AI code starts here
        self._render_header("login")
        # AI code ends here

        self._current_view = LoginView(
            self._container,
            self._handle_login,
            self._show_create_user_view
        )
        self._current_view.pack()

    def _show_create_user_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._render_header("create_user")

        self._current_view = UserView(
            self._container,
            self._handle_create_user,
            self._show_login_view
        )
        self._current_view.pack()

    def _show_exercises_view(self, day):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = ExercisesView(
            self._container,
            day,
            self._show_day_view,
        )
        self._current_view.pack()

    # def _show_day_view(self):
    #     if self._current_view:
    #         self._current_view.destroy()
    #     self._current_view = DayView(
    #         self._container,
    #         self._show_login_view,
    #         self._show_exercises_view,
    #         self._current_user
    #     )
    #     self._current_view.pack()

    def _show_day_view(self):
        # self._header.grid()
        self._sidebar.grid()

        if self._current_view:
            self._current_view.destroy()

        # AI code starts here
        self._render_header("app")
        # AI code ends here

        self._current_view = DayView(
            self._container,
            self._show_login_view,
            self._show_exercises_view,
            self._current_user
        )
        self._current_view.pack()
        self._render_days()

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
        except UsernameTooShortError:
            print("User name is too short")
        except PasswordTooShortError:
            print("Password is too short")
        except PasswordsDoNotMatchError:
            print("Passwords don't match")

    def _render_days(self):
        for child in self._sidebar.winfo_children():
            child.destroy()

        # ttk.Label(self._sidebar, text="Add New Day").grid(row=0, column=0)
        self._day_name_entry = ttk.Entry(master=self._sidebar)
        self._day_name_entry.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        ttk.Button(
            self._sidebar,
            text="Add New Day",
            command=self._handle_create_day
        ).grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        days = day_service.get_days_by_user(self._current_user.username)

        # AI code starts here
        Frame(self._sidebar, height=1, bg="#cccccc").grid(
            row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5
        )

        row = 3
        # AI code ends here

        for day in days:
            ttk.Button(
                self._sidebar,
                text=day.day_name,
                command=lambda d=day: self._show_exercises_view(d)
                # AI code starts here
            ).grid(row=row, column=0, sticky="ew", padx=5, pady=5)
            # AI code ends here

            ttk.Button(
                self._sidebar,
                text="Delete",
                command=lambda d=day: self._delete_day(d)
                # AI code starts here
            ).grid(row=row, column=1, sticky="ew", padx=5, pady=5)

            row += 1
            # AI code ends here

    def _delete_day(self, day):
        response = messagebox.askyesno(
            "Confirmation", f'Do you really want to delete "{day.day_name}"?')
        if response:
            day_service.delete_day(day)
        self._render_days()

    def _day_refresh(self):
        for child in self._sidebar.winfo_children():
            child.destroy()

        self._render_days()

    def _handle_create_day(self):
        day_name = self._day_name_entry.get()
        day_service.create_day(self._current_user.username, day_name)

        # AI code starts here
        self._day_name_entry.delete(0, "end")
        self._render_days()
        # AI code ends here

    # def _open_day(self, day):
    #     self._show_exercises_view(day)
    #     print(
    #         f"Opening day: {day.day_name}, id={day.id}, username={day.username}")
