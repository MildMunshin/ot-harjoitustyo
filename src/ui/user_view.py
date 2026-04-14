from tkinter import ttk, constants


class UserView:
    def __init__(self, root, handle_create_user, handle_show_login):
        self._frame = ttk.Frame(master=root)
        self._handle_create_user = handle_create_user

        self._username_entry = ttk.Entry(master=self._frame)
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        ttk.Label(self._frame, text="Create user").grid(
            row=0, column=0, columnspan=2)

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
