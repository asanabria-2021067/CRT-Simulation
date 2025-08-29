import tkinter as tk

class Controles:
    def __init__(self, root):
        # Diccionario con valores controlables
        self.valores = {
            "voltaje_aceleracion": tk.DoubleVar(value=100),
            "voltaje_vertical": tk.DoubleVar(value=0),
            "voltaje_horizontal": tk.DoubleVar(value=0),
            "frecuencia": tk.DoubleVar(value=1),
            "fase": tk.DoubleVar(value=0),
            "persistencia": tk.DoubleVar(value=0.5),
        }

        frame = tk.Frame(root, bg="black")
        frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        # Crear sliders dinámicamente
        for i, (k, var) in enumerate(self.valores.items()):
            label = tk.Label(frame, text=k, fg="white", bg="black")
            label.pack()
            slider = tk.Scale(
                frame, from_=-100, to=100, resolution=1,
                orient=tk.HORIZONTAL, variable=var, length=200
            )
            slider.pack(pady=5)

    def get_valores(self):
        return {k: v.get() for k, v in self.valores.items()}
