from tkinter import ttk, constants, messagebox
from src.services.day_service import day_service


class DayView:
    def __init__(self, root, back_to_login, show_exercises_view, user):
        self._frame = ttk.Frame(master=root)
        self._user = user
        self._day_container = ttk.Frame(self._frame)
        self._show_exercises_view = show_exercises_view

        self._day_container.grid(row=3, column=0, columnspan=3)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()