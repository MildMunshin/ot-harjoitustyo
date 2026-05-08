from tkinter import ttk, constants, messagebox
from src.services.day_service import day_service


# class DayView:
#     def __init__(self, root, back_to_login, show_exercises_view, user):
#         self._frame = ttk.Frame(master=root)
#         self._user = user
#         self._day_container = ttk.Frame(self._frame)
#         self._show_exercises_view = show_exercises_view

#         ttk.Label(
#             self._frame,
#             text="Workout days"
#         ).grid(row=1, column=0, columnspan=2, sticky=constants.W, padx=55, pady=55)

#         ttk.Label(self._frame, text="Add New Day").grid(row=2, column=0)
#         self._day_name_entry = ttk.Entry(master=self._frame)
#         self._day_name_entry.grid(row=2, column=1)
#         ttk.Button(
#             self._frame,
#             text="+",
#             command=self._handle_create_day
#         ).grid(row=2, column=2)

#         ttk.Button(
#             self._frame,
#             text="Back to Login",
#             command=back_to_login
#         ).grid(row=0, column=0, columnspan=2)

#         self._day_container.grid(row=3, column=0, columnspan=3)

#         self._render_days()

#     def _handle_create_day(self):
#         day_name = self._day_name_entry.get()
#         day_service.create_day(self._user.username, day_name)

#         self._render_days()

#     def _render_days(self):
#         for child in self._day_container.winfo_children():
#             child.destroy()

#         days = day_service.get_days_by_user(self._user.username)
#         for day in days:
#             ttk.Button(
#                 self._day_container,
#                 text=day.day_name,
#                 # AI code starts
#                 command=lambda d=day: self._open_day(d)
#             ).pack(fill="x", pady=2)
#             # AI code ends

#             ttk.Button(
#                 self._day_container,
#                 text="Delete day",
#                 command=lambda d=day: self._delete_day(d)
#             ).pack()

#     def _open_day(self, day):
#         self._show_exercises_view(day)
#         print(
#             f"Opening day: {day.day_name}, id={day.id}, username={day.username}")

#     def _delete_day(self, day):
#         response = messagebox.askyesno(
#             "Confirmation", f'Do you really want to delete "{day.day_name}"?')
#         if response:
#             day_service.delete_day(day)
#             self._refresh()
#         else:
#             self._refresh()

#     def pack(self):
#         self._frame.pack(fill=constants.X)

#     def destroy(self):
#         self._frame.destroy()

#     def _refresh(self):
#         for child in self._day_container.winfo_children():
#             child.destroy()

#         self._render_days()

class DayView: 
    def __init__(self, root, back_to_login, show_exercises_view, user):
        self._frame = ttk.Frame(master=root)
        self._user = user
        self._day_container = ttk.Frame(self._frame)
        self._show_exercises_view = show_exercises_view

        # ttk.Label(
        #     self._frame,
        #     text="Workout days"
        # ).grid(row=1, column=0, columnspan=2, sticky=constants.W, padx=55, pady=55)

        # ttk.Label(self._frame, text="Add New Day").grid(row=2, column=0)
        # self._day_name_entry = ttk.Entry(master=self._frame)
        # self._day_name_entry.grid(row=2, column=1)
        # ttk.Button(
        #     self._frame,
        #     text="+",
        #     command=self._handle_create_day
        # ).grid(row=2, column=2)

        # ttk.Button(
        #     self._frame,
        #     text="Back to Login",
        #     command=back_to_login
        # ).grid(row=0, column=0, columnspan=2)

        self._day_container.grid(row=3, column=0, columnspan=3)

        # self._render_days()

    # def _handle_create_day(self):
    #     day_name = self._day_name_entry.get()
    #     day_service.create_day(self._user.username, day_name)

        # self._render_days()

    # def _render_days(self):
    #     for child in self._day_container.winfo_children():
    #         child.destroy()

    #     days = day_service.get_days_by_user(self._user.username)
    #     for day in days:
    #         ttk.Button(
    #             self._day_container,
    #             text=day.day_name,
    #             # AI code starts
    #             command=lambda d=day: self._open_day(d)
    #         ).pack(fill="x", pady=2)
    #         # AI code ends

    #         ttk.Button(
    #             self._day_container,
    #             text="Delete day",
    #             command=lambda d=day: self._delete_day(d)
    #         ).pack()

    # def _open_day(self, day):
    #     self._show_exercises_view(day)
    #     print(
    #         f"Opening day: {day.day_name}, id={day.id}, username={day.username}")

    # def _delete_day(self, day):
    #     response = messagebox.askyesno(
    #         "Confirmation", f'Do you really want to delete "{day.day_name}"?')
    #     if response:
    #         day_service.delete_day(day)
    #         self._refresh()
    #     else:
    #         self._refresh()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    # def _refresh(self):
    #     for child in self._day_container.winfo_children():
    #         child.destroy()

    #     self._render_days()