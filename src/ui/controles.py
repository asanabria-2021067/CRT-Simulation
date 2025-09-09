# controles.py
import tkinter as tk
from tkinter import ttk
import math

class Controles:
    def __init__(self, parent):
        self.modo_sinusoidal = tk.BooleanVar(value=False)
        
        # Variables de control mejoradas con rangos apropiados para las figuras de Lissajous
        self.valores = {
            "voltaje_aceleracion": tk.DoubleVar(value=2000),
            "voltaje_vertical": tk.DoubleVar(value=0),
            "voltaje_horizontal": tk.DoubleVar(value=0),
            "frecuencia_vertical": tk.DoubleVar(value=1.0),
            "fase_vertical": tk.DoubleVar(value=0),
            "frecuencia_horizontal": tk.DoubleVar(value=1.0),
            "fase_horizontal": tk.DoubleVar(value=0),
            "persistencia": tk.DoubleVar(value=1.5),
            "brillo": tk.DoubleVar(value=1.0)
        }

        # Frame principal con diseño moderno
        self.frame_principal = tk.Frame(parent, bg="#1e2a3a", relief=tk.RAISED, bd=3)
        self.frame_principal.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Título con estilo
        titulo = tk.Label(self.frame_principal, text="⚡ CONTROLES CRT ⚡", 
                         font=("Consolas", 16, "bold"), fg="#00ffff", bg="#1e2a3a")
        titulo.pack(pady=15)
        
        # Separador estilizado
        sep1 = tk.Frame(self.frame_principal, height=3, bg="#00ffff")
        sep1.pack(fill=tk.X, padx=15, pady=8)
        
        self._crear_controles_basicos()
        self._crear_modo_selector()
        self._crear_controles_sinusoidales()
        self._crear_control_display()
        self._crear_botones_accion()

    def _crear_controles_basicos(self):
        """Crea controles básicos de voltajes con diseño mejorado"""
        frame_basicos = tk.LabelFrame(self.frame_principal, text="⚡ VOLTAJES DE CONTROL", 
                                    fg="#ffff00", bg="#283848", font=("Consolas", 11, "bold"),
                                    bd=2, relief=tk.GROOVE)
        frame_basicos.pack(fill=tk.X, padx=12, pady=8)
        
        # Voltaje de aceleración con indicador visual
        self._crear_slider_avanzado(frame_basicos, "🚀 Voltaje Aceleración (V)", 
                          self.valores["voltaje_aceleracion"], 500, 5000, 100, "#00ff00")
        
        # Voltaje vertical 
        self._crear_slider_avanzado(frame_basicos, "⬆ Voltaje Vertical (V)", 
                          self.valores["voltaje_vertical"], -600, 600, 25, "#ffff00")
        
        # Voltaje horizontal
        self._crear_slider_avanzado(frame_basicos, "➡ Voltaje Horizontal (V)", 
                          self.valores["voltaje_horizontal"], -600, 600, 25, "#ff8800")

    def _crear_modo_selector(self):
        """Crea selector de modo con diseño cyberpunk"""
        frame_modo = tk.LabelFrame(self.frame_principal, text="🔄 MODO DE OPERACIÓN", 
                                 fg="#ff00ff", bg="#283848", font=("Consolas", 11, "bold"),
                                 bd=2, relief=tk.GROOVE)
        frame_modo.pack(fill=tk.X, padx=12, pady=8)
        
        # Botón de modo estilizado
        btn_frame = tk.Frame(frame_modo, bg="#283848")
        btn_frame.pack(pady=10)
        
        self.btn_modo = tk.Checkbutton(btn_frame, text="🌊 MODO SINUSOIDAL (Lissajous)", 
                                     variable=self.modo_sinusoidal, 
                                     fg="#ffffff", bg="#4a5568", activebackground="#ff00ff",
                                     selectcolor="#1a202c", font=("Consolas", 10, "bold"),
                                     relief=tk.RAISED, bd=2, padx=10, pady=5,
                                     command=self._toggle_modo)
        self.btn_modo.pack()

    def _crear_controles_sinusoidales(self):
        """Crea controles para señales sinusoidales con presets mejorados"""
        self.frame_sinusoidal = tk.LabelFrame(self.frame_principal, text="📊 SEÑALES SINUSOIDALES", 
                                            fg="#00ffaa", bg="#283848", font=("Consolas", 11, "bold"),
                                            bd=2, relief=tk.GROOVE)
        self.frame_sinusoidal.pack(fill=tk.X, padx=12, pady=8)
        
        # Canal Vertical
        canal_v_frame = tk.LabelFrame(self.frame_sinusoidal, text="📈 CANAL VERTICAL (Y)", 
                                    fg="#ffff00", bg="#3a4a5a", font=("Consolas", 9, "bold"))
        canal_v_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self._crear_slider_compacto(canal_v_frame, "Frecuencia (Hz)", 
                          self.valores["frecuencia_vertical"], 1, 4, 1, "#ffff00")
        
        self._crear_slider_compacto(canal_v_frame, "Fase (°)", 
                          self.valores["fase_vertical"], 0, 360, 10, "#ffaa00")
        
        # Canal Horizontal
        canal_h_frame = tk.LabelFrame(self.frame_sinusoidal, text="📉 CANAL HORIZONTAL (X)", 
                                    fg="#00ffff", bg="#3a4a5a", font=("Consolas", 9, "bold"))
        canal_h_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self._crear_slider_compacto(canal_h_frame, "Frecuencia (Hz)", 
                          self.valores["frecuencia_horizontal"], 1, 4, 1, "#00ffff")
        
        self._crear_slider_compacto(canal_h_frame, "Fase (°)", 
                          self.valores["fase_horizontal"], 0, 360, 10, "#00aaff")
        
        # Presets de figuras de Lissajous corregidos
        self._crear_presets_lissajous()
        
        # Inicialmente deshabilitado
        self._toggle_modo()

    def _crear_presets_lissajous(self):
        """Crea presets basados en las figuras mostradas en la imagen, CORREGIDOS"""
        frame_presets = tk.LabelFrame(self.frame_sinusoidal, text="🎯 PRESETS LISSAJOUS", 
                                    fg="#ff8800", bg="#3a4a5a", font=("Consolas", 9, "bold"))
        frame_presets.pack(fill=tk.X, padx=5, pady=5)
        
        # Fila 1:1 (frecuencias 1:1) - CORREGIDA
        fila_1_1 = tk.Frame(frame_presets, bg="#3a4a5a")
        fila_1_1.pack(fill=tk.X, pady=2)
        tk.Label(fila_1_1, text="1:1", fg="#ffffff", bg="#3a4a5a", font=("Consolas", 8, "bold")).pack(side=tk.LEFT)
        
        presets_1_1 = [
            ("/", lambda: self._aplicar_preset(1, 1, 0, 0)),      # δ=0: línea diagonal
            ("()", lambda: self._aplicar_preset(1, 1, 0, 45)),    # δ=π/4: elipse
            ("O", lambda: self._aplicar_preset(1, 1, 0, 90)),     # δ=π/2: círculo
            ("()", lambda: self._aplicar_preset(1, 1, 0, 135)),   # δ=3π/4: elipse
            ("\\", lambda: self._aplicar_preset(1, 1, 0, 180))    # δ=π: línea diagonal opuesta
        ]
        
        for nombre, comando in presets_1_1:
            btn = tk.Button(fila_1_1, text=nombre, command=comando,
                           bg="#2d3748", fg="#ffffff", font=("Consolas", 7),
                           relief=tk.FLAT, padx=3, pady=1, width=4)
            btn.pack(side=tk.LEFT, padx=1)
        
        # Fila 1:2 (frecuencias 1:2)
        fila_1_2 = tk.Frame(frame_presets, bg="#3a4a5a")
        fila_1_2.pack(fill=tk.X, pady=2)
        tk.Label(fila_1_2, text="1:2", fg="#ffffff", bg="#3a4a5a", font=("Consolas", 8, "bold")).pack(side=tk.LEFT)
        
        presets_1_2 = [
            ("∩", lambda: self._aplicar_preset(2, 1, 0, 0)),
            ("∼", lambda: self._aplicar_preset(2, 1, 45, 0)),
            ("∞", lambda: self._aplicar_preset(2, 1, 90, 0)),
            ("∼", lambda: self._aplicar_preset(2, 1, 135, 0)),
            ("∪", lambda: self._aplicar_preset(2, 1, 180, 0))
        ]
        
        for nombre, comando in presets_1_2:
            btn = tk.Button(fila_1_2, text=nombre, command=comando,
                           bg="#2d3748", fg="#00ff00", font=("Consolas", 7),
                           relief=tk.FLAT, padx=3, pady=1, width=4)
            btn.pack(side=tk.LEFT, padx=1)
        
        # Fila 1:3
        fila_1_3 = tk.Frame(frame_presets, bg="#3a4a5a")
        fila_1_3.pack(fill=tk.X, pady=2)
        tk.Label(fila_1_3, text="1:3", fg="#ffffff", bg="#3a4a5a", font=("Consolas", 8, "bold")).pack(side=tk.LEFT)
        
        presets_1_3 = [
            ("N", lambda: self._aplicar_preset(3, 1, 0, 0)),
            ("M", lambda: self._aplicar_preset(3, 1, 45, 0)),
            ("W", lambda: self._aplicar_preset(3, 1, 90, 0)),
            ("M", lambda: self._aplicar_preset(3, 1, 135, 0)),
            ("N", lambda: self._aplicar_preset(3, 1, 180, 0))
        ]
        
        for nombre, comando in presets_1_3:
            btn = tk.Button(fila_1_3, text=nombre, command=comando,
                           bg="#2d3748", fg="#ffff00", font=("Consolas", 7),
                           relief=tk.FLAT, padx=3, pady=1, width=4)
            btn.pack(side=tk.LEFT, padx=1)
        
        # Fila 2:3
        fila_2_3 = tk.Frame(frame_presets, bg="#3a4a5a")
        fila_2_3.pack(fill=tk.X, pady=2)
        tk.Label(fila_2_3, text="2:3", fg="#ffffff", bg="#3a4a5a", font=("Consolas", 8, "bold")).pack(side=tk.LEFT)
        
        presets_2_3 = [
            ("α", lambda: self._aplicar_preset(3, 2, 0, 0)),
            ("∞", lambda: self._aplicar_preset(3, 2, 45, 0)),
            ("✱", lambda: self._aplicar_preset(3, 2, 90, 0)),
            ("∞", lambda: self._aplicar_preset(3, 2, 135, 0)),
            ("α", lambda: self._aplicar_preset(3, 2, 180, 0))
        ]
        
        for nombre, comando in presets_2_3:
            btn = tk.Button(fila_2_3, text=nombre, command=comando,
                           bg="#2d3748", fg="#ff00ff", font=("Consolas", 7),
                           relief=tk.FLAT, padx=3, pady=1, width=4)
            btn.pack(side=tk.LEFT, padx=1)

    def _crear_control_display(self):
        """Crea controles de display mejorados"""
        frame_display = tk.LabelFrame(self.frame_principal, text="📺 CONFIGURACIÓN PANTALLA", 
                                    fg="#ff6600", bg="#283848", font=("Consolas", 11, "bold"),
                                    bd=2, relief=tk.GROOVE)
        frame_display.pack(fill=tk.X, padx=12, pady=8)
        
        self._crear_slider_compacto(frame_display, "🕐 Persistencia (s)", 
                          self.valores["persistencia"], 0.2, 5.0, 0.2, "#ff6600")
        
        self._crear_slider_compacto(frame_display, "💡 Brillo", 
                          self.valores["brillo"], 0.3, 2.0, 0.1, "#ffffff")

    def _crear_botones_accion(self):
        """Crea botones de acción con estilo futurista"""
        frame_botones = tk.Frame(self.frame_principal, bg="#1e2a3a")
        frame_botones.pack(fill=tk.X, padx=12, pady=10)
        
        # Botón limpiar pantalla
        btn_limpiar = tk.Button(frame_botones, text="🗑 LIMPIAR", 
                               command=self._limpiar_pantalla,
                               bg="#ff4444", fg="white", font=("Consolas", 9, "bold"),
                               relief=tk.RAISED, bd=2, padx=15, pady=5)
        btn_limpiar.pack(fill=tk.X, pady=2)
        
        # Botón reset
        btn_reset = tk.Button(frame_botones, text="🔄 RESET", 
                             command=self._reset_valores,
                             bg="#44ff44", fg="black", font=("Consolas", 9, "bold"),
                             relief=tk.RAISED, bd=2, padx=15, pady=5)
        btn_reset.pack(fill=tk.X, pady=2)

    def _crear_slider_avanzado(self, parent, texto, variable, min_val, max_val, resolution, color):
        """Crea slider avanzado con etiqueta y valor"""
        frame = tk.Frame(parent, bg="#283848")
        frame.pack(fill=tk.X, padx=5, pady=3)
        
        label = tk.Label(frame, text=texto, fg=color, bg="#283848", font=("Consolas", 9, "bold"))
        label.pack(side=tk.LEFT, padx=5)
        
        valor_label = tk.Label(frame, textvariable=variable, fg="#ffffff", bg="#283848", font=("Consolas", 9))
        valor_label.pack(side=tk.RIGHT, padx=5)
        
        slider = tk.Scale(parent, from_=min_val, to=max_val, resolution=resolution,
                         orient=tk.HORIZONTAL, variable=variable, length=250,
                         fg=color, bg="#1e2a3a", troughcolor="#0a0f1c", activebackground=color)
        slider.pack(fill=tk.X, padx=5)

    def _crear_slider_compacto(self, parent, texto, variable, min_val, max_val, resolution, color):
        """Crea slider compacto"""
        frame = tk.Frame(parent, bg="#3a4a5a")
        frame.pack(fill=tk.X, pady=2)
        
        label = tk.Label(frame, text=texto, fg=color, bg="#3a4a5a", font=("Consolas", 8))
        label.pack(side=tk.LEFT, padx=5)
        
        valor_label = tk.Label(frame, textvariable=variable, fg="#ffffff", bg="#3a4a5a", font=("Consolas", 8))
        valor_label.pack(side=tk.RIGHT, padx=5)
        
        slider = tk.Scale(parent, from_=min_val, to=max_val, resolution=resolution,
                         orient=tk.HORIZONTAL, variable=variable, length=200,
                         fg=color, bg="#3a4a5a", troughcolor="#1e2a3a", activebackground=color)
        slider.pack(fill=tk.X, padx=5)

    def _toggle_modo(self):
        """Activa/desactiva controles según el modo"""
        estado = tk.NORMAL if self.modo_sinusoidal.get() else tk.DISABLED
        
        for widget in self.frame_sinusoidal.winfo_children():
            if isinstance(widget, (tk.Scale, tk.Button)):
                widget.configure(state=estado)
            elif hasattr(widget, 'winfo_children'):
                for subwidget in widget.winfo_children():
                    if isinstance(subwidget, (tk.Scale, tk.Button)):
                        try:
                            subwidget.configure(state=estado)
                        except tk.TclError:
                            pass

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

    def _limpiar_pantalla(self):
        """Señal para limpiar la pantalla"""
        # Esta función será llamada por el display
        pass

    def _reset_valores(self):
        """Resetea todos los valores a sus defaults"""
        defaults = {
            "voltaje_aceleracion": 2000,
            "voltaje_vertical": 0,
            "voltaje_horizontal": 0,
            "frecuencia_vertical": 1.0,
            "fase_vertical": 0,
            "frecuencia_horizontal": 1.0,
            "fase_horizontal": 0,
            "persistencia": 1.5,
            "brillo": 1.0
        }
        
        for key, valor in defaults.items():
            if key in self.valores:
                self.valores[key].set(valor)
        
        self.modo_sinusoidal.set(False)
        self._toggle_modo()

    def get_valores(self):
        """Retorna todos los valores actuales"""
        valores = {k: v.get() for k, v in self.valores.items()}
        valores["modo_sinusoidal"] = self.modo_sinusoidal.get()
        return valores

    def get_voltajes_actuales(self, tiempo=0):
        """Calcula voltajes actuales considerando el modo"""
        valores = self.get_valores()
        
        if valores["modo_sinusoidal"]:
            # Calcular voltajes sinusoidales con amplitud ajustable
            freq_v = valores["frecuencia_vertical"]
            fase_v = math.radians(valores["fase_vertical"])
            freq_h = valores["frecuencia_horizontal"]
            fase_h = math.radians(valores["fase_horizontal"])
            
            # Amplitud base para las figuras de Lissajous
            amplitud_base = 250
            
            # CORRECCIÓN: usar sin para Y (vertical) y cos para X (horizontal)
            voltaje_v = amplitud_base * math.sin(2 * math.pi * freq_v * tiempo + fase_v)
            voltaje_h = amplitud_base * math.cos(2 * math.pi * freq_h * tiempo + fase_h)
            
            return voltaje_v, voltaje_h
        else:
            return valores["voltaje_vertical"], valores["voltaje_horizontal"]

    def get_limpiar_signal(self):
        """Retorna True si se debe limpiar la pantalla (implementar según necesidad)"""
        return False
