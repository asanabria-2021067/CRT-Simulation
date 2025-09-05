import tkinter as tk
from tkinter import ttk
import math

class Controles:
    def __init__(self, root):
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
        self.frame_principal = tk.Frame(root, bg="#1e2a3a", relief=tk.RAISED, bd=3)
        self.frame_principal.pack(side=tk.RIGHT, fill=tk.Y, padx=15, pady=15)
        
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
        self._crear_slider_avanzado(frame_basicos, "↔ Voltaje Horizontal (V)", 
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
                          self.valores["fase_vertical"], 0, 360, 90, "#ffaa00")
        
        # Canal Horizontal
        canal_h_frame = tk.LabelFrame(self.frame_sinusoidal, text="📉 CANAL HORIZONTAL (X)", 
                                    fg="#00ffff", bg="#3a4a5a", font=("Consolas", 9, "bold"))
        canal_h_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self._crear_slider_compacto(canal_h_frame, "Frecuencia (Hz)", 
                          self.valores["frecuencia_horizontal"], 1, 4, 1, "#00ffff")
        
        self._crear_slider_compacto(canal_h_frame, "Fase (°)", 
                          self.valores["fase_horizontal"], 0, 360, 90, "#00aaff")
        
        # Presets de figuras de Lissajous basados en la imagen
        self._crear_presets_lissajous()
        
        # Inicialmente deshabilitado
        self._toggle_modo()

    def _crear_presets_lissajous(self):
        """Crea presets basados en las figuras mostradas en la imagen"""
        frame_presets = tk.LabelFrame(self.frame_sinusoidal, text="🎯 PRESETS LISSAJOUS", 
                                    fg="#ff8800", bg="#3a4a5a", font=("Consolas", 9, "bold"))
        frame_presets.pack(fill=tk.X, padx=5, pady=5)
        
        # Fila 1:1 (frecuencias 1:1)
        fila_1_1 = tk.Frame(frame_presets, bg="#3a4a5a")
        fila_1_1.pack(fill=tk.X, pady=2)
        tk.Label(fila_1_1, text="1:1", fg="#ffffff", bg="#3a4a5a", font=("Consolas", 8, "bold")).pack(side=tk.LEFT)
        
        presets_1_1 = [
            ("   /", lambda: self._aplicar_preset(1, 1, 0, 0)),      # Línea diagonal
            ("  ( )", lambda: self._aplicar_preset(1, 1, 0, 90)),    # Elipse/Círculo  
            ("  O", lambda: self._aplicar_preset(1, 1, 90, 90)),     # Círculo
            ("  ( )", lambda: self._aplicar_preset(1, 1, 180, 90)),  # Elipse
            ("   \\", lambda: self._aplicar_preset(1, 1, 180, 0))    # Línea diagonal opuesta
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
            (" 8 ", lambda: self._aplicar_preset(1, 2, 0, 90)),      # Figura 8
            (" ∞ ", lambda: self._aplicar_preset(1, 2, 90, 0)),     # Infinito
            (" ∩ ", lambda: self._aplicar_preset(1, 2, 90, 90)),    # Forma de U
            (" ∩ ", lambda: self._aplicar_preset(1, 2, 180, 90)),   # Forma de U invertida
            (" 8 ", lambda: self._aplicar_preset(1, 2, 270, 0))     # Figura 8 rotada
        ]
        
        for nombre, comando in presets_1_2:
            btn = tk.Button(fila_1_2, text=nombre, command=comando,
                           bg="#2d3748", fg="#00ff00", font=("Consolas", 7),
                           relief=tk.FLAT, padx=3, pady=1, width=4)
            btn.pack(side=tk.LEFT, padx=1)
        
        # Fila 1:3 (frecuencias 1:3)
        fila_1_3 = tk.Frame(frame_presets, bg="#3a4a5a")
        fila_1_3.pack(fill=tk.X, pady=2)
        tk.Label(fila_1_3, text="1:3", fg="#ffffff", bg="#3a4a5a", font=("Consolas", 8, "bold")).pack(side=tk.LEFT)
        
        presets_1_3 = [
            (" ∿ ", lambda: self._aplicar_preset(1, 3, 0, 0)),      # Onda
            (" W ", lambda: self._aplicar_preset(1, 3, 0, 90)),     # Forma W
            (" M ", lambda: self._aplicar_preset(1, 3, 90, 0)),     # Forma M
            (" W ", lambda: self._aplicar_preset(1, 3, 90, 90)),    # W rotada
            (" ∿ ", lambda: self._aplicar_preset(1, 3, 180, 0))     # Onda invertida
        ]
        
        for nombre, comando in presets_1_3:
            btn = tk.Button(fila_1_3, text=nombre, command=comando,
                           bg="#2d3748", fg="#ffff00", font=("Consolas", 7),
                           relief=tk.FLAT, padx=3, pady=1, width=4)
            btn.pack(side=tk.LEFT, padx=1)
        
        # Fila 2:3 (frecuencias 2:3)
        fila_2_3 = tk.Frame(frame_presets, bg="#3a4a5a")
        fila_2_3.pack(fill=tk.X, pady=2)
        tk.Label(fila_2_3, text="2:3", fg="#ffffff", bg="#3a4a5a", font=("Consolas", 8, "bold")).pack(side=tk.LEFT)
        
        presets_2_3 = [
            (" ⬢ ", lambda: self._aplicar_preset(2, 3, 0, 0)),      # Patrón complejo
            (" ✤ ", lambda: self._aplicar_preset(2, 3, 0, 90)),     # Estrella
            (" ⬢ ", lambda: self._aplicar_preset(2, 3, 90, 0)),     # Hexágono-like
            (" ✤ ", lambda: self._aplicar_preset(2, 3, 90, 90)),    # Estrella rotada
            (" ⬢ ", lambda: self._aplicar_preset(2, 3, 180, 0))     # Patrón invertido
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
                             bg="#4444ff", fg="white", font=("Consolas", 9, "bold"),
                             relief=tk.RAISED, bd=2, padx=15, pady=5)
        btn_reset.pack(fill=tk.X, pady=2)

    def _crear_slider_avanzado(self, parent, texto, variable, min_val, max_val, resolution, color):
        """Crea un slider con diseño avanzado y indicadores visuales"""
        frame = tk.Frame(parent, bg="#283848")
        frame.pack(fill=tk.X, padx=8, pady=6)
        
        # Etiqueta con estilo
        label = tk.Label(frame, text=texto, fg=color, bg="#283848", 
                        font=("Consolas", 9, "bold"))
        label.pack()
        
        # Frame para slider y valor
        slider_frame = tk.Frame(frame, bg="#283848")
        slider_frame.pack(fill=tk.X)
        
        # Slider estilizado
        slider = tk.Scale(slider_frame, from_=min_val, to=max_val, resolution=resolution,
                         orient=tk.HORIZONTAL, variable=variable, length=220,
                         bg="#1a202c", fg=color, highlightbackground="#283848",
                         troughcolor="#2d3748", activebackground=color,
                         font=("Consolas", 8), relief=tk.FLAT)
        slider.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        # Valor numérico con fondo
        valor_frame = tk.Frame(slider_frame, bg=color, relief=tk.RAISED, bd=1)
        valor_frame.pack(side=tk.RIGHT, padx=(5,0))
        
        valor_label = tk.Label(valor_frame, textvariable=variable, fg="#000000", bg=color, 
                              font=("Consolas", 8, "bold"), width=6)
        valor_label.pack(padx=2, pady=1)

    def _crear_slider_compacto(self, parent, texto, variable, min_val, max_val, resolution, color):
        """Crea un slider compacto para los controles sinusoidales"""
        frame = tk.Frame(parent, bg="#3a4a5a")
        frame.pack(fill=tk.X, padx=5, pady=3)
        
        # Etiqueta a la izquierda
        label = tk.Label(frame, text=texto, fg=color, bg="#3a4a5a", 
                        font=("Consolas", 8), width=12, anchor='w')
        label.pack(side=tk.LEFT)
        
        # Slider más pequeño
        slider = tk.Scale(frame, from_=min_val, to=max_val, resolution=resolution,
                         orient=tk.HORIZONTAL, variable=variable, length=130,
                         bg="#2d3748", fg=color, highlightbackground="#3a4a5a",
                         troughcolor="#1a202c", activebackground=color,
                         font=("Consolas", 7), relief=tk.FLAT, showvalue=0)
        slider.pack(side=tk.LEFT, expand=True, padx=(5,5))
        
        # Valor a la derecha
        valor_label = tk.Label(frame, textvariable=variable, fg=color, bg="#1a202c", 
                              font=("Consolas", 8, "bold"), width=5, relief=tk.SUNKEN)
        valor_label.pack(side=tk.RIGHT)

    def _toggle_modo(self):
        """Activa/desactiva controles según el modo con efectos visuales"""
        if self.modo_sinusoidal.get():
            # Modo sinusoidal activo
            self.btn_modo.config(bg="#00ff00", fg="#000000")
            estado = tk.NORMAL
            color_frame = "#2a4a2a"
        else:
            # Modo manual activo  
            self.btn_modo.config(bg="#4a5568", fg="#ffffff")
            estado = tk.DISABLED
            color_frame = "#4a3a3a"
        
        self.frame_sinusoidal.config(bg=color_frame)
        
        # Cambiar estado de todos los widgets en el frame sinusoidal
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
            amplitud_base = 400  # Aumentada para mejor visibilidad
            
            # Calcular voltajes sinusoidales
            voltaje_v = amplitud_base * math.sin(2 * math.pi * freq_v * tiempo + fase_v)
            voltaje_h = amplitud_base * math.sin(2 * math.pi * freq_h * tiempo + fase_h)
            
            return voltaje_v, voltaje_h
        else:
            return valores["voltaje_vertical"], valores["voltaje_horizontal"]

    def get_limpiar_signal(self):
        """Retorna True si se debe limpiar la pantalla (implementar según necesidad)"""
        return False
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