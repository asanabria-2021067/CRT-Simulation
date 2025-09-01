import tkinter as tk

class Display:
    def __init__(self, root, width=700, height=500):
        self.canvas = tk.Canvas(root, width=width, height=height, bg="black")
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

    def handle_draw(self, valores):
        """Dibuja el CRT en tres vistas usando un canvas de Tkinter"""
        self.canvas.delete("all")  # limpiar frame

        # Colores
        verde = "lime"
        blanco = "white"

        # --- Vista lateral ---
        self.canvas.create_rectangle(50, 50, 300, 250, outline=blanco)
        self.canvas.create_oval(145, 145, 155, 155, fill=verde)

        # --- Vista superior ---
        self.canvas.create_rectangle(350, 50, 600, 250, outline=blanco)
        self.canvas.create_oval(445, 145, 455, 155, fill=verde)

        # --- Pantalla frontal ---
        self.canvas.create_rectangle(650, 50, 900, 300, outline=blanco)

        # Punto de impacto depende de voltajes
        x = 775 + int(valores["voltaje_horizontal"])
        y = 175 + int(valores["voltaje_vertical"])
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill=verde)
