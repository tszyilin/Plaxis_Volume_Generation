# view.py

import tkinter as tk
from tkinter import filedialog, messagebox

class PlaxisView:
    def __init__(self, master):
        self.master = master
        master.title("Plaxis Volume Generation")

        self.file_name_label = tk.Label(master, text="File Name:")
        self.file_name_label.grid(row=0, column=0)

        self.file_name_entry = tk.Entry(master, width=50)
        self.file_name_entry.grid(row=0, column=1)

        self.import_button = tk.Button(master, text="Import", command=self.import_file)
        self.import_button.grid(row=0, column=2)


        self.run_button = tk.Button(master, text="Run", command=None)  # To be set by the controller
        self.run_button.grid(row=2, column=0, columnspan=3, pady=10)

        self.text_box = tk.Text(master, height=20, width=80)
        self.text_box.grid(row=3, column=0, columnspan=3)

    def import_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.file_name_entry.delete(0, tk.END)
            self.file_name_entry.insert(0, file_path)

    def set_run_command(self, command):
        self.run_button.config(command=command)

    def display_results(self, results):
        self.text_box.delete(1.0, tk.END)
        if isinstance(results, dict):
            self.text_box.insert(tk.END, "Valid rows dictionary:\n")
            self.text_box.insert(tk.END, str(results) + "\n")
        elif isinstance(results, list):
            for row, errors in results:
                self.text_box.insert(tk.END, f"Row {row}, Errors: {', '.join(errors)}\n")


