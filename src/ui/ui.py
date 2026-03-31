from tkinter import Tk, ttk, constants
from src.services.user_service import user_service, UsernameExistsError, InvalidCredentialsError

# Allocate the following classes into own modules in the future

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

    def _show_app_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = AppView(
            self._root,
            self._show_login_view
        )
        self._current_view.pack()

    def _handle_login(self, username, password):
        try:
            user_service.login(username, password)
            print("Login success")
            self._show_app_view()
        except InvalidCredentialsError:
            print("Invalid username or password")

    def _handle_create_user(self, username, password):
        try:
            user_service.create_user(username, password)
            print("User created")
            self._show_login_view()
        except UsernameExistsError:
            print("Username already exists")

class LoginView:
    def __init__(self, root, handle_login, handle_show_create_user):
        self._frame = ttk.Frame(master=root)
        self._handle_login = handle_login

        self._username_entry = ttk.Entry(master=self._frame)
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        ttk.Label(self._frame, text="Login").grid(row=0, column=0, columnspan=2)

        ttk.Label(self._frame, text="Username").grid(row=1, column=0)
        self._username_entry.grid(row=1, column=1)

        ttk.Label(self._frame, text="Password").grid(row=2, column=0)
        self._password_entry.grid(row=2, column=1)

        ttk.Button(
            self._frame,
            text="Login",
            command=self._handle_login_click
        ).grid(row=3, column=0, columnspan=2)

        ttk.Button(
            self._frame,
            text="Create user",
            command=handle_show_create_user
        ).grid(row=4, column=0, columnspan=2)

    def _handle_login_click(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        self._handle_login(username, password)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

class UserView:
    def __init__(self, root, handle_create_user, handle_show_login):
        self._frame = ttk.Frame(master=root)
        self._handle_create_user = handle_create_user

        self._username_entry = ttk.Entry(master=self._frame)
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        ttk.Label(self._frame, text="Create user").grid(row=0, column=0, columnspan=2)

        ttk.Label(self._frame, text="Username").grid(row=1, column=0)
        self._username_entry.grid(row=1, column=1)

        ttk.Label(self._frame, text="Password").grid(row=2, column=0)
        self._password_entry.grid(row=2, column=1)

        ttk.Button(
            self._frame,
            text="Create",
            command=self._handle_create_user_click
        ).grid(row=3, column=0, columnspan=2)

        ttk.Button(
            self._frame,
            text="Back to login",
            command=handle_show_login
        ).grid(row=4, column=0, columnspan=2)

    def _handle_create_user_click(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        self._handle_create_user(username, password)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

class AppView:
    def __init__(self, root, back_to_login):
        self._frame = ttk.Frame(master=root)

        ttk.Label(self._frame, text="The App will be here").grid(columnspan=2, sticky=constants.W, padx=55, pady=55)

        ttk.Button(
            self._frame,
            text="Back to Login",
            command=back_to_login
        ).grid(row=3, column=0, columnspan=2)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

if __name__ == "__main__":
    window = Tk()
    window.title("App")

    ui = UI(window)
    ui.start()

    window.mainloop()