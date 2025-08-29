import tkinter as tk
from .controles import Controles
from .display import Display


class Ventana:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulación CRT")

        # UI components
        self.display = Display(self.root)
        self.controles = Controles(self.root)

        # Loop de actualización (cada 50 ms)
        self.update_loop()

    def update_loop(self):
        valores = self.controles.get_valores()
        self.display.handle_draw(valores)
        self.root.after(50, self.update_loop)

    def run(self):
        self.root.mainloop()
