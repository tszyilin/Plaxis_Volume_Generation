# controller.py

from model.model import PlaxisModel
from view.view import PlaxisView
import tkinter as tk

class PlaxisController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_run_command(self.run_plaxis_volume_generation)

    def run_plaxis_volume_generation(self):
        file_name = self.view.file_name_entry.get()

        try:
            results = list(self.model.plaxis_volume_generation(file_name))
            if results:
                self.view.display_results(results)
            else:
                self.view.display_results(self.model.valid_rows_dict)
        except Exception as e:
            messagebox.showerror("Error", str(e))
