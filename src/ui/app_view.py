# from tkinter import Tk, ttk, constants
# from src.services.user_service import user_service, UsernameExistsError, InvalidCredentialsError
# from src.services.exercise_service import exercise_service
# from src.ui.components.exercise_element import ExerciseElement

# class AppView:
#     def __init__(self, root, back_to_login):
#         self._frame = ttk.Frame(master=root)
#         self._exercise_service = exercise_service
#         self._exercise_container = ttk.Frame(self._frame)

#         ttk.Label(
#             self._frame,
#             text="The GymApp"
#             ).grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=55, pady=55)

#         # Labels not in a perfect line with exercise elements. Fix later
#         ttk.Label(self._frame, text="Exercise", anchor="center").grid(row=1, column=0, padx=20, pady=10, sticky="ew")
#         ttk.Label(self._frame, text="Sets", anchor="center").grid(row=1, column=1, padx=20, pady=10, sticky="ew")
#         ttk.Label(self._frame, text="Reps", anchor="center").grid(row=1, column=2, padx=20, pady=10, sticky="ew")
#         ttk.Label(self._frame, text="Weight", anchor="center").grid(row=1, column=3, padx=20, pady=10, sticky="ew")
#         ttk.Label(self._frame, text="", anchor="center").grid(row=1, column=4, padx=20, pady=10, sticky="ew")

#         for i in range(5):
#             self._frame.columnconfigure(i, weight=1)

#         self._exercise_container.grid(row=2, column=0, columnspan=5, padx=20, pady=10, sticky="ew")

#         ttk.Button(
#             self._frame,
#             text="Add Exercise",
#             command=self.add_exercise
#         ).grid(row=3, column=0, columnspan=2, pady=10)

#         ttk.Button(
#             self._frame,
#             text="Back to Login",
#             command=back_to_login
#         ).grid(row=4, column=0, columnspan=2)

#         self._refresh()

#     def pack(self):
#         self._frame.pack(fill=constants.X)

#     def destroy(self):
#         self._frame.destroy()

#     # Ai code begins
#     def add_exercise(self):
#         element = ExerciseElement(
#             self._exercise_container,
#             save_callback=self._handle_save
#         )
#         element.pack(fill="x", pady=5)

#     def _handle_save(self, name, sets, reps, weight):
#         self._exercise_service.create_exercise(name, sets, reps, weight)
#         self._refresh()

#     def _refresh(self):
#         for child in self._exercise_container.winfo_children():
#             child.destroy()

#         exercises = self._exercise_service.get_all_exercises()

#         for exercise in exercises:
#             element = ExerciseElement(
#                 self._exercise_container,
#                 save_callback=self._handle_save,
#                 exercise=exercise
#             )
#             element.pack(fill="x", pady=5)
#     # Ai code ends
