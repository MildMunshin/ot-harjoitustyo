from tkinter import Tk, ttk, constants

# Code created by AI starts here


class ExerciseElement(ttk.Frame):
    def __init__(self, parent, current_day, save_callback, delete_callback=None, update_callback=None, exercise=None):
        super().__init__(parent)

        self._save_callback = save_callback
        self._delete_callback = delete_callback
        self._update_callback = update_callback
        self._current_day = current_day

        self._name_entry = ttk.Entry(self)
        self._name_entry.grid(row=0, column=0, sticky="ew", padx=5)

        self._sets_entry = ttk.Entry(self)
        self._sets_entry.grid(row=0, column=1, sticky="ew", padx=5)

        self._reps_entry = ttk.Entry(self)
        self._reps_entry.grid(row=0, column=2, sticky="ew", padx=5)

        self._weight_entry = ttk.Entry(self)
        self._weight_entry.grid(row=0, column=3, sticky="ew", padx=5)

        if exercise:
            self._name_entry.insert(0, exercise.name)
            self._sets_entry.insert(0, exercise.sets)
            self._reps_entry.insert(0, exercise.reps)
            self._weight_entry.insert(0, exercise.weight)

            ttk.Button(self, text="Update",
                        command=lambda: self._handle_update(exercise.id)
                       ).grid(row=0, column=4, padx=5)

            ttk.Button(self, text="Delete exercise",
                       # AI code starts here
                       command=lambda: self._handle_delete(exercise.id)
                       # AI code ends here
                       ).grid(row=0, column=5, padx=5)

        else:
            self._name_entry.insert(0, "exercise name")
            self._sets_entry.insert(0, "sets")
            self._reps_entry.insert(0, "reps")
            self._weight_entry.insert(0, "weight")

            ttk.Button(self, text="Save", command=self._handle_save).grid(
                row=0, column=4, padx=5)

        for i in range(6):
            self.columnconfigure(i, weight=1)

    def _handle_save(self):
        try:
            day_id = self._current_day.id
            name = self._name_entry.get()
            sets = int(self._sets_entry.get())
            reps = int(self._reps_entry.get())
            weight = float(self._weight_entry.get())
        except ValueError:
            return

        self._save_callback(day_id, name, sets, reps, weight)

    # Code created by AI ends here

    def _handle_update(self, exercise_id):
        try:
            day_id = self._current_day.id
            name = self._name_entry.get()
            sets = int(self._sets_entry.get())
            reps = int(self._reps_entry.get())
            weight = float(self._weight_entry.get())
        except ValueError: 
            return

        self._update_callback(exercise_id, day_id, name, sets, reps, weight)

    def _handle_delete(self, exercise_id):
        self._delete_callback(exercise_id)
