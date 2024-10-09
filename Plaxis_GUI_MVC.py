
import tkinter as tk
from controller.controller import PlaxisController
from model.model import PlaxisModel
from view.view import PlaxisView

def main():
    root = tk.Tk()
    model = PlaxisModel()
    view = PlaxisView(root)
    controller = PlaxisController(model, view)

    root.mainloop()

if __name__ == "__main__":
    main()
