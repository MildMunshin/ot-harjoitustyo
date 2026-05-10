from tkinter import Tk, ttk, constants, messagebox
from src.services.user_service import user_service, UsernameExistsError, InvalidCredentialsError
from src.services.exercise_service import exercise_service
from src.ui.components.exercise_element import ExerciseElement


class ExercisesView:
    def __init__(self, root, day, back_to_days):
        self._frame = ttk.Frame(master=root)
        self._current_day = day
        self._exercise_service = exercise_service
        self._exercises_container = ttk.Frame(self._frame)

        self._exercises_container.grid(row=2)

        for i in range(6):
            self._frame.columnconfigure(i, weight=1)

        ttk.Button(
            self._frame,
            text="Add Exercise",
            command=self._handle_create_exercise
        ).grid(row=3, column=0, columnspan=6, pady=10)

        self._refresh()

    # AI code begins
    def _handle_create_exercise(self):

        # AI code starts here
        row = len(self._exercises_container.winfo_children())
        # AI code ends here

        element = ExerciseElement(
            self._exercises_container,
            self._current_day,
            save_callback=self._handle_save
        )
        # AI code starts here
        element.grid(row=row, column=0, columnspan=6, sticky="ew")
        # AI code ends here

    def _handle_save(self, day_id, name, sets, reps, weight):
        self._exercise_service.create_exercise(
            day_id, name, sets, reps, weight)
        self._refresh()

    # AI code ends

    def _handle_delete(self, exercise_id):
        response = messagebox.askyesno(
            "Confirmation", "Do you really want to delete the exercise?")
        if response:
            self._exercise_service.delete_exercise(exercise_id)
            self._refresh()
        else:
            self._refresh()

    def _handle_update(self, exercise_id, day_id, name, sets, reps, weight):
        self._exercise_service.update_exercise(
            exercise_id, day_id, name, sets, reps, weight)
        self._refresh()

    # AI code begins

    def _refresh(self):
        for child in self._exercises_container.winfo_children():
            child.destroy()

        exercises = self._exercise_service.get_exercises_by_day(
            self._current_day.id)

        if len(exercises) > 0:
            ttk.Label(self._exercises_container, text="Exercise").grid(
                row=0, column=0, sticky="ew", padx=5)
            ttk.Label(self._exercises_container, text="Sets").grid(
                row=0, column=1, sticky="ew", padx=5)
            ttk.Label(self._exercises_container, text="Reps").grid(
                row=0, column=2, sticky="ew", padx=5)
            ttk.Label(self._exercises_container, text="Weight").grid(
                row=0, column=3, sticky="ew", padx=5)
            ttk.Label(self._exercises_container, text="").grid(
                row=0, column=4, sticky="ew", padx=5)
            ttk.Label(self._exercises_container, text="").grid(
                row=0, column=5, sticky="ew", padx=5)

        for row, ex in enumerate(exercises, start=1):
            element = ExerciseElement(
                self._exercises_container,
                self._current_day,
                save_callback=self._handle_save,
                delete_callback=self._handle_delete,
                update_callback=self._handle_update,
                exercise=ex
            )

            element.grid(row=row, column=0, columnspan=6, sticky="ew")

            for i in range(6):
                self._exercises_container.columnconfigure(
                    i,
                    weight=1,
                    uniform="col"
                )
            # AI code ends

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
