import tkinter as tk
from tkinter import ttk
import math

class Controles:
    def __init__(self, root):
        self.modo_sinusoidal = tk.BooleanVar(value=False)
        
        # Variables de control
        self.valores = {
            "voltaje_aceleracion": tk.DoubleVar(value=2000),
            "voltaje_vertical": tk.DoubleVar(value=0),
            "voltaje_horizontal": tk.DoubleVar(value=0),
            "frecuencia_vertical": tk.DoubleVar(value=1),
            "fase_vertical": tk.DoubleVar(value=0),
            "frecuencia_horizontal": tk.DoubleVar(value=1),
            "fase_horizontal": tk.DoubleVar(value=90),
            "persistencia": tk.DoubleVar(value=0.5),
        }

        # Frame principal para controles
        self.frame_principal = tk.Frame(root, bg="#2c3e50", relief=tk.RAISED, bd=2)
        self.frame_principal.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)
        
        # Título
        titulo = tk.Label(self.frame_principal, text="CONTROLES CRT", 
                         font=("Arial", 14, "bold"), fg="white", bg="#2c3e50")
        titulo.pack(pady=10)
        
        # Separador
        sep1 = ttk.Separator(self.frame_principal, orient='horizontal')
        sep1.pack(fill=tk.X, padx=10, pady=5)
        
        self._crear_controles_basicos()
        self._crear_modo_selector()
        self._crear_controles_sinusoidales()
        self._crear_control_persistencia()

    def _crear_controles_basicos(self):
        """Crea controles básicos de voltajes"""
        frame_basicos = tk.LabelFrame(self.frame_principal, text="Voltajes de Control", 
                                    fg="white", bg="#34495e", font=("Arial", 10, "bold"))
        frame_basicos.pack(fill=tk.X, padx=10, pady=5)
        
        # Voltaje de aceleración
        self._crear_slider(frame_basicos, "Voltaje Aceleración (V)", 
                          self.valores["voltaje_aceleracion"], 500, 5000, 50)
        
        # Voltaje vertical
        self._crear_slider(frame_basicos, "Voltaje Vertical (V)", 
                          self.valores["voltaje_vertical"], -500, 500, 10)
        
        # Voltaje horizontal
        self._crear_slider(frame_basicos, "Voltaje Horizontal (V)", 
                          self.valores["voltaje_horizontal"], -500, 500, 10)

    def _crear_modo_selector(self):
        """Crea selector de modo manual/sinusoidal"""
        frame_modo = tk.LabelFrame(self.frame_principal, text="Modo de Operación", 
                                 fg="white", bg="#34495e", font=("Arial", 10, "bold"))
        frame_modo.pack(fill=tk.X, padx=10, pady=5)
        
        # Botón de cambio de modo
        btn_modo = tk.Checkbutton(frame_modo, text="Modo Sinusoidal (Lissajous)", 
                                variable=self.modo_sinusoidal, fg="white", bg="#34495e",
                                selectcolor="#2c3e50", font=("Arial", 9),
                                command=self._toggle_modo)
        btn_modo.pack(pady=5)

    def _crear_controles_sinusoidales(self):
        """Crea controles para señales sinusoidales"""
        self.frame_sinusoidal = tk.LabelFrame(self.frame_principal, text="Señales Sinusoidales", 
                                            fg="white", bg="#34495e", font=("Arial", 10, "bold"))
        self.frame_sinusoidal.pack(fill=tk.X, padx=10, pady=5)
        
        # Controles verticales
        lbl_v = tk.Label(self.frame_sinusoidal, text="Canal Vertical:", 
                        fg="yellow", bg="#34495e", font=("Arial", 9, "bold"))
        lbl_v.pack()
        
        self._crear_slider(self.frame_sinusoidal, "Frecuencia V (Hz)", 
                          self.valores["frecuencia_vertical"], 0.1, 10, 0.1)
        
        self._crear_slider(self.frame_sinusoidal, "Fase V (°)", 
                          self.valores["fase_vertical"], 0, 360, 5)
        
        # Separador pequeño
        sep = tk.Frame(self.frame_sinusoidal, height=2, bg="#2c3e50")
        sep.pack(fill=tk.X, pady=5)
        
        # Controles horizontales
        lbl_h = tk.Label(self.frame_sinusoidal, text="Canal Horizontal:", 
                        fg="cyan", bg="#34495e", font=("Arial", 9, "bold"))
        lbl_h.pack()
        
        self._crear_slider(self.frame_sinusoidal, "Frecuencia H (Hz)", 
                          self.valores["frecuencia_horizontal"], 0.1, 10, 0.1)
        
        self._crear_slider(self.frame_sinusoidal, "Fase H (°)", 
                          self.valores["fase_horizontal"], 0, 360, 5)
        
        # Presets de Lissajous
        frame_presets = tk.Frame(self.frame_sinusoidal, bg="#34495e")
        frame_presets.pack(fill=tk.X, pady=5)
        
        tk.Label(frame_presets, text="Presets:", fg="white", bg="#34495e",
                font=("Arial", 8, "bold")).pack()
        
        presets = [
            ("Círculo", lambda: self._aplicar_preset(1.0, 1.0, 0, 90)),
            ("Línea /", lambda: self._aplicar_preset(1.0, 1.0, 0, 0)),
            ("Línea \\", lambda: self._aplicar_preset(1.0, 1.0, 0, 180)),
            ("Figura 8", lambda: self._aplicar_preset(2.0, 1.0, 0, 90)),
            ("Pétalos", lambda: self._aplicar_preset(3.0, 2.0, 0, 90))
        ]
        
        for i, (nombre, comando) in enumerate(presets):
            btn = tk.Button(frame_presets, text=nombre, command=comando,
                           bg="#3498db", fg="white", font=("Arial", 7),
                           relief=tk.FLAT, padx=5, pady=2)
            btn.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Inicialmente deshabilitado
        self._toggle_modo()

    def _crear_control_persistencia(self):
        """Crea control de persistencia"""
        frame_persistencia = tk.LabelFrame(self.frame_principal, text="Display", 
                                         fg="white", bg="#34495e", font=("Arial", 10, "bold"))
        frame_persistencia.pack(fill=tk.X, padx=10, pady=5)
        
        self._crear_slider(frame_persistencia, "Persistencia (s)", 
                          self.valores["persistencia"], 0.1, 3.0, 0.1)

    def _crear_slider(self, parent, texto, variable, min_val, max_val, resolution):
        """Crea un slider con etiqueta y valor"""
        # Frame para el slider
        frame = tk.Frame(parent, bg="#34495e")
        frame.pack(fill=tk.X, padx=5, pady=2)
        
        # Etiqueta
        label = tk.Label(frame, text=texto, fg="white", bg="#34495e", 
                        font=("Arial", 8))
        label.pack()
        
        # Slider
        slider = tk.Scale(frame, from_=min_val, to=max_val, resolution=resolution,
                         orient=tk.HORIZONTAL, variable=variable, length=200,
                         bg="#34495e", fg="white", highlightbackground="#2c3e50",
                         troughcolor="#2c3e50", activebackground="#3498db")
        slider.pack()
        
        # Etiqueta de valor actual
        valor_label = tk.Label(frame, textvariable=variable, fg="lime", bg="#34495e", 
                              font=("Arial", 8, "bold"))
        valor_label.pack()

    def _toggle_modo(self):
        """Activa/desactiva controles según el modo"""
        estado = tk.NORMAL if self.modo_sinusoidal.get() else tk.DISABLED
        
        for widget in self.frame_sinusoidal.winfo_children():
            if isinstance(widget, tk.Scale):
                widget.configure(state=estado)

    def get_valores(self):
        """Retorna todos los valores actuales"""
        valores = {k: v.get() for k, v in self.valores.items()}
        valores["modo_sinusoidal"] = self.modo_sinusoidal.get()
        return valores

    def _aplicar_preset(self, freq_v, freq_h, fase_v, fase_h):
        """Aplica un preset de configuración para Lissajous"""
        self.valores["frecuencia_vertical"].set(freq_v)
        self.valores["frecuencia_horizontal"].set(freq_h)
        self.valores["fase_vertical"].set(fase_v)
        self.valores["fase_horizontal"].set(fase_h)
        
        # Activar modo sinusoidal si no está activo
        if not self.modo_sinusoidal.get():
            self.modo_sinusoidal.set(True)
            self._toggle_modo()

    def get_voltajes_actuales(self, tiempo=0):
        """Calcula voltajes actuales considerando el modo"""
        valores = self.get_valores()
        
        if valores["modo_sinusoidal"]:
            # Calcular voltajes sinusoidales
            freq_v = valores["frecuencia_vertical"]
            fase_v = math.radians(valores["fase_vertical"])
            freq_h = valores["frecuencia_horizontal"]
            fase_h = math.radians(valores["fase_horizontal"])
            
            # Amplitud mayor para mejor visualización de Lissajous
            amplitud = 300
            voltaje_v = amplitud * math.sin(2 * math.pi * freq_v * tiempo + fase_v)
            voltaje_h = amplitud * math.sin(2 * math.pi * freq_h * tiempo + fase_h)
            
            return voltaje_v, voltaje_h
        else:
            return valores["voltaje_vertical"], valores["voltaje_horizontal"]