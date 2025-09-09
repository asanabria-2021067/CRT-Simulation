# ventana.py
import tkinter as tk
from tkinter import ttk
import time
import threading
from .controles import Controles
from .display import Display

class Ventana:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("⚡ Simulación CRT - Tubo de Rayos Catódicos | UVG 2025")
        self.root.configure(bg="#0a0f1c")
        
        # Configurar geometría optimizada
        self.root.geometry("1450x750")
        self.root.minsize(1300, 650)
        
        # Variables de control del sistema
        self.running = True
        self.paused = False
        self.tiempo_inicio = time.time()
        self.velocidad_simulacion = 1.0
        
        # Configurar estilo avanzado
        self._configurar_estilo_avanzado()
        
        # Crear barra de menú
        self._crear_menu()
        
        # Crear componentes principales
        self.display = Display(self.root)
        
        # Crear frame para controles con scroll
        controles_frame = tk.Frame(self.root, bg="#1e2a3a")
        controles_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=15, pady=15)
        
        canvas = tk.Canvas(controles_frame, bg="#1e2a3a", width=300)
        scrollbar = tk.Scrollbar(controles_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        inner_frame = tk.Frame(canvas, bg="#1e2a3a")
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        
        self.controles = Controles(inner_frame)
        
        # Actualizar scrollregion después de que se carguen los widgets
        inner_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        
        # Conectar controles con display
        self._conectar_controles()
        
        # Crear barra de estado mejorada
        self._crear_barra_estado_avanzada()
        
        # Variables para rendimiento
        self.frame_count = 0
        self.last_fps_time = time.time()
        self.fps = 0
        self.target_fps = 60
        self.frame_time = 1000 // self.target_fps  # ms
        
        # Configurar eventos
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.root.bind("<Key>", self._on_key_press)
        self.root.focus_set()
        
        # Iniciar bucle de actualización optimizado
        self.update_loop()

    def _configurar_estilo_avanzado(self):
        """Configuración de estilo cyberpunk avanzado"""
        style = ttk.Style()
        
        # Usar tema base
        try:
            style.theme_use('alt')
        except:
            try:
                style.theme_use('clam')
            except:
                pass
        
        # Colores cyberpunk personalizados
        colores = {
            'bg_primary': '#0a0f1c',
            'bg_secondary': '#1e2a3a', 
            'accent_cyan': '#00ffff',
            'accent_yellow': '#ffff00',
            'accent_green': '#00ff00',
            'text_primary': '#ffffff',
            'text_secondary': '#cccccc'
        }
        
        # Configurar estilos TTK
        style.configure('Cyber.TLabel', 
                       background=colores['bg_secondary'], 
                       foreground=colores['text_primary'],
                       font=('Consolas', 9))
        
        style.configure('Cyber.TFrame', 
                       background=colores['bg_primary'],
                       relief='flat')
        
        style.configure('Status.TLabel',
                       background=colores['bg_secondary'],
                       foreground=colores['accent_cyan'],
                       font=('Consolas', 8))

    def _crear_menu(self):
        """Crea menú principal con opciones avanzadas"""
        menubar = tk.Menu(self.root, bg="#1e2a3a", fg="white", font=('Consolas', 9))
        self.root.config(menu=menubar)
        
        # Menú Simulación
        menu_sim = tk.Menu(menubar, tearoff=0, bg="#1e2a3a", fg="white")
        menubar.add_cascade(label="Simulación", menu=menu_sim)
        menu_sim.add_command(label="Pausar/Reanudar", command=self._toggle_pause, accelerator="Espacio")
        menu_sim.add_command(label="Reiniciar", command=self._reiniciar_simulacion, accelerator="R")
        menu_sim.add_separator()
        menu_sim.add_command(label="Limpiar Pantalla", command=self._limpiar_pantalla, accelerator="C")
        menu_sim.add_separator()
        
        # Submenú velocidad
        menu_velocidad = tk.Menu(menu_sim, tearoff=0, bg="#1e2a3a", fg="white")
        menu_sim.add_cascade(label="Velocidad", menu=menu_velocidad)
        for vel, nombre in [(0.25, "0.25x"), (0.5, "0.5x"), (1.0, "Normal"), (2.0, "2x"), (4.0, "4x")]:
            menu_velocidad.add_command(label=nombre, 
                                     command=lambda v=vel: self._cambiar_velocidad(v))
        
        # Menú Presets
        menu_presets = tk.Menu(menubar, tearoff=0, bg="#1e2a3a", fg="white")
        menubar.add_cascade(label="Presets", menu=menu_presets)
        
        # Presets organizados por categoría
        presets_categorias = {
            "Figuras Básicas 1:1": [
                ("Línea Diagonal", lambda: self._aplicar_preset(1, 1, 0, 0)),
                ("Círculo", lambda: self._aplicar_preset(1, 1, 0, 90)),
                ("Elipse 45°", lambda: self._aplicar_preset(1, 1, 45, 90)),
                ("Línea Diagonal Inv", lambda: self._aplicar_preset(1, 1, 180, 0))
            ],
            "Figuras 1:2": [
                ("Figura 8", lambda: self._aplicar_preset(1, 2, 0, 90)),
                ("Infinito", lambda: self._aplicar_preset(1, 2, 90, 0)),
                ("Parabola", lambda: self._aplicar_preset(1, 2, 90, 90)),
                ("8 Rotado", lambda: self._aplicar_preset(1, 2, 180, 90))
            ],
            "Figuras 1:3": [
                ("Trébol 3 Hojas", lambda: self._aplicar_preset(1, 3, 0, 0)),
                ("Ondas", lambda: self._aplicar_preset(1, 3, 0, 90)),
                ("Pétalos", lambda: self._aplicar_preset(1, 3, 90, 0)),
                ("Compleja 1:3", lambda: self._aplicar_preset(1, 3, 90, 90))
            ],
            "Figuras 2:3": [
                ("Estrella", lambda: self._aplicar_preset(2, 3, 0, 0)),
                ("Rosa", lambda: self._aplicar_preset(2, 3, 0, 90)),
                ("Hexágono", lambda: self._aplicar_preset(2, 3, 90, 0)),
                ("Compleja 2:3", lambda: self._aplicar_preset(2, 3, 90, 90))
            ]
        }
        
        for categoria, presets in presets_categorias.items():
            submenu = tk.Menu(menu_presets, tearoff=0, bg="#1e2a3a", fg="white")
            menu_presets.add_cascade(label=categoria, menu=submenu)
            for nombre, comando in presets:
                submenu.add_command(label=nombre, command=comando)
        
        # Menú Ayuda
        menu_ayuda = tk.Menu(menubar, tearoff=0, bg="#1e2a3a", fg="white")
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Manual de Usuario", command=self._mostrar_manual)
        menu_ayuda.add_command(label="Teoría CRT", command=self._mostrar_teoria)
        menu_ayuda.add_command(label="Atajos de Teclado", command=self._mostrar_atajos)
        menu_ayuda.add_separator()
        menu_ayuda.add_command(label="Acerca de", command=self._mostrar_acerca)

    def _conectar_controles(self):
        """Conecta controles con funciones del display"""
        # Conectar botón limpiar
        self.controles._limpiar_pantalla = self.display.limpiar_pantalla
        
        # Conectar eventos de cambio de valores (si es necesario)
        # Aquí podrías agregar callbacks específicos

    def _crear_barra_estado_avanzada(self):
        """Crea barra de estado con información detallada"""
        # Frame principal de estado
        self.frame_estado = tk.Frame(self.root, bg="#1e2a3a", height=35, relief=tk.RAISED, bd=1)
        self.frame_estado.pack(side=tk.BOTTOM, fill=tk.X)
        self.frame_estado.pack_propagate(False)
        
        # Frame izquierdo - Estado de simulación
        frame_izq = tk.Frame(self.frame_estado, bg="#1e2a3a")
        frame_izq.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.status_sim = tk.Label(frame_izq, 
                                  text="⚡ SIMULACIÓN ACTIVA", 
                                  fg="#00ff00", bg="#1e2a3a", 
                                  font=("Consolas", 9, "bold"))
        self.status_sim.pack(side=tk.LEFT)
        
        # Separador
        sep1 = tk.Label(frame_izq, text=" | ", fg="#666666", bg="#1e2a3a", font=("Consolas", 9))
        sep1.pack(side=tk.LEFT)
        
        # FPS
        self.fps_label = tk.Label(frame_izq, 
                                 text="FPS: --", 
                                 fg="#ffff00", bg="#1e2a3a", 
                                 font=("Consolas", 9))
        self.fps_label.pack(side=tk.LEFT)
        
        # Frame central - Información de modo
        frame_centro = tk.Frame(self.frame_estado, bg="#1e2a3a")
        frame_centro.pack(side=tk.LEFT, expand=True, padx=20)
        
        self.modo_label = tk.Label(frame_centro, 
                                  text="MODO: MANUAL", 
                                  fg="#00ffff", bg="#1e2a3a", 
                                  font=("Consolas", 9, "bold"))
        self.modo_label.pack()
        
        # Frame derecho - Información del proyecto
        frame_der = tk.Frame(self.frame_estado, bg="#1e2a3a")
        frame_der.pack(side=tk.RIGHT, padx=10, pady=5)
        
        info_proyecto = tk.Label(frame_der, 
                               text="🎓 UVG - Laboratorio de Física 3 - Proyecto CRT 2025", 
                               fg="#888888", bg="#1e2a3a", 
                               font=("Consolas", 8))
        info_proyecto.pack(side=tk.RIGHT)
        
        # Indicador de velocidad
        self.velocidad_label = tk.Label(frame_der,
                                       text="Velocidad: 1.0x",
                                       fg="#ff8800", bg="#1e2a3a",
                                       font=("Consolas", 8))
        self.velocidad_label.pack(side=tk.RIGHT, padx=(0, 15))

    def update_loop(self):
        """Bucle principal optimizado con control de FPS"""
        if not self.running:
            return
        
        start_time = time.time()
        
        if not self.paused:
            # Obtener valores de controles
            valores = self.controles.get_valores()
            
            # Calcular tiempo de simulación considerando velocidad
            tiempo_actual = (time.time() - self.tiempo_inicio) * self.velocidad_simulacion
            
            # Actualizar display
            self.display.handle_draw(valores, tiempo_actual)
            
            # Actualizar información de estado
            self._actualizar_estado_avanzado(valores, tiempo_actual)
        
        # Calcular FPS
        self._actualizar_fps()
        
        # Controlar velocidad de actualización
        elapsed = (time.time() - start_time) * 1000  # ms
        delay = max(1, int(self.frame_time - elapsed))
        
        # Programar siguiente frame
        self.root.after(delay, self.update_loop)

    def _actualizar_fps(self):
        """Actualización precisa de FPS"""
        self.frame_count += 1
        tiempo_actual = time.time()
        
        if tiempo_actual - self.last_fps_time >= 1.0:
            self.fps = self.frame_count / (tiempo_actual - self.last_fps_time)
            self.frame_count = 0
            self.last_fps_time = tiempo_actual
            
            # Actualizar label con código de color
            if self.fps >= 45:
                color = "#00ff00"  # Verde: buen rendimiento
            elif self.fps >= 25:
                color = "#ffff00"  # Amarillo: rendimiento medio
            else:
                color = "#ff4444"  # Rojo: bajo rendimiento
            
            self.fps_label.config(text=f"FPS: {self.fps:.1f}", fg=color)

    def _actualizar_estado_avanzado(self, valores, tiempo_actual):
        """Actualiza el estado de la simulación"""
        if self.paused:
            self.status_sim.config(text="⏸ SIMULACIÓN PAUSADA", fg="#ffff00")
        else:
            self.status_sim.config(text="⚡ SIMULACIÓN ACTIVA", fg="#00ff00")
        
        modo = "SINUSOIDAL" if valores["modo_sinusoidal"] else "MANUAL"
        self.modo_label.config(text=f"MODO: {modo}")
        
        self.velocidad_label.config(text=f"Velocidad: {self.velocidad_simulacion:.2f}x")

    def _toggle_pause(self):
        """Pausa o reanuda la simulación"""
        self.paused = not self.paused

    def _reiniciar_simulacion(self):
        """Reinicia la simulación"""
        self.tiempo_inicio = time.time()
        self.controles._reset_valores()
        self.display.limpiar_pantalla()

    def _limpiar_pantalla(self):
        """Limpia la pantalla"""
        self.display.limpiar_pantalla()

    def _cambiar_velocidad(self, nueva_velocidad):
        """Cambia la velocidad de simulación"""
        self.velocidad_simulacion = nueva_velocidad

    def _aplicar_preset(self, freq_v, freq_h, fase_v, fase_h):
        """Aplica un preset de Lissajous"""
        self.controles.valores["frecuencia_vertical"].set(freq_v)
        self.controles.valores["frecuencia_horizontal"].set(freq_h)
        self.controles.valores["fase_vertical"].set(fase_v)
        self.controles.valores["fase_horizontal"].set(fase_h)
        
        if not self.controles.modo_sinusoidal.get():
            self.controles.modo_sinusoidal.set(True)
            self.controles._toggle_modo()

    # Eventos de teclado
    def _on_key_press(self, event):
        """Manejo de atajos de teclado"""
        key = event.keysym.lower()
        
        if key == 'space':
            self._toggle_pause()
        elif key == 'r':
            self._reiniciar_simulacion()
        elif key == 'c':
            self._limpiar_pantalla()
        elif key == 'h':
            self._mostrar_atajos()
        elif key == 'escape':
            self._on_closing()
        # Números para velocidad
        elif key in '12345':
            velocidades = {'1': 0.25, '2': 0.5, '3': 1.0, '4': 2.0, '5': 4.0}
            self._cambiar_velocidad(velocidades[key])

    # Ventanas de información
    def _mostrar_manual(self):
        """Muestra el manual de usuario"""
        ventana = self._crear_ventana_info("Manual de Usuario", 600, 500)
        
        texto = """
MANUAL DE USUARIO - SIMULADOR CRT

1. CONTROLES BÁSICOS:
   • Voltaje de Aceleración: Controla la velocidad inicial del electrón
   • Voltajes V/H: Deflexión vertical y horizontal en modo manual
   • Persistencia: Tiempo que permanecen visibles los puntos
   • Brillo: Intensidad de la luminosidad en pantalla

2. MODO MANUAL:
   • Controle directamente los voltajes de deflexión
   • Observe el haz de electrones en las vistas lateral y superior
   • El punto verde muestra el impacto en la pantalla

3. MODO SINUSOIDAL (LISSAJOUS):
   • Active el checkbox "Modo Sinusoidal"
   • Ajuste frecuencias y fases para ambos canales
   • Use los presets para figuras comunes
   • Las figuras aparecen según la relación de frecuencias

4. VISTAS:
   • Vista Lateral: Muestra deflexión vertical (placas Y)
   • Vista Superior: Muestra deflexión horizontal (placas X)
   • Pantalla CRT: Resultado final con persistencia de fósforo

5. PRESETS DISPONIBLES:
   • 1:1 - Líneas, círculos, elipses
   • 1:2 - Figuras en 8, infinito
   • 1:3 - Tréboles, ondas
   • 2:3 - Estrellas, rosas

6. ATAJOS DE TECLADO:
   • Espacio: Pausar/Reanudar
   • R: Reiniciar
   • C: Limpiar pantalla
   • H: Mostrar ayuda
   • ESC: Salir
"""
        
        self._agregar_texto_scroll(ventana, texto)

    def _mostrar_teoria(self):
        """Muestra información teórica del CRT"""
        ventana = self._crear_ventana_info("Teoría del CRT", 650, 550)
        
        texto = """
TEORÍA DEL TUBO DE RAYOS CATÓDICOS

1. PRINCIPIO DE FUNCIONAMIENTO:
   • Los electrones son emitidos por un cátodo caliente
   • Acelerados por un ánodo con voltaje positivo
   • Deflectados por campos eléctricos en placas X e Y
   • Impactan en una pantalla fosforescente

2. FÍSICA INVOLUCRADA:
   • Energía cinética: Ek = eV (donde V es voltaje de aceleración)
   • Velocidad inicial: v₀ = √(2eV/m)
   • Deflexión: proporcional a voltaje de placas
   • Amplificación: por distancia placas-pantalla

3. ECUACIONES DE DEFLEXIÓN:
   • Campo eléctrico: E = V/d (V=voltaje, d=separación)
   • Aceleración: a = eE/m = eV/(md)
   • Deflexión en placas: y₁ = ½at²
   • Deflexión total: y = y₁ + v_y·t_libre

4. FIGURAS DE LISSAJOUS:
   • Resultado de combinar dos señales sinusoidales
   • x(t) = A·sin(ωₓt + φₓ)
   • y(t) = B·sin(ωᵧt + φᵧ)
   • La forma depende de la relación ωₓ:ωᵧ y diferencia de fase

5. APLICACIONES:
   • Osciloscopios analógicos
   • Monitores CRT antiguos
   • Tubos de televisión
   • Instrumentos de medición

6. PARÁMETROS TÍPICOS:
   • Voltaje de aceleración: 1-10 kV
   • Voltaje de deflexión: ±500 V
   • Separación de placas: 1-3 cm
   • Distancia a pantalla: 20-40 cm

CONSTANTES UTILIZADAS:
   • Carga del electrón: e = 1.602×10⁻¹⁹ C
   • Masa del electrón: m = 9.109×10⁻³¹ kg
"""
        
        self._agregar_texto_scroll(ventana, texto)

    def _mostrar_atajos(self):
        """Muestra los atajos de teclado"""
        ventana = self._crear_ventana_info("Atajos de Teclado", 400, 350)
        
        texto = """
ATAJOS DE TECLADO

CONTROL DE SIMULACIÓN:
   • Espacio      - Pausar/Reanudar
   • R            - Reiniciar simulación
   • C            - Limpiar pantalla
   • ESC          - Salir del programa

VELOCIDAD:
   • 1            - Velocidad 0.25x
   • 2            - Velocidad 0.5x
   • 3            - Velocidad normal (1.0x)
   • 4            - Velocidad 2.0x
   • 5            - Velocidad 4.0x

AYUDA:
   • H            - Mostrar esta ventana
   • F1           - Manual completo
   • F2           - Teoría del CRT

CONSEJOS:
   • Use los presets del menú para figuras específicas
   • Ajuste la persistencia para mejor visualización
   • Combine diferentes frecuencias para patrones únicos
   • El brillo afecta la intensidad de los puntos
"""
        
        self._agregar_texto_scroll(ventana, texto)

    def _mostrar_acerca(self):
        """Muestra información sobre el programa"""
        ventana = self._crear_ventana_info("Acerca de", 450, 300)
        
        texto = """
SIMULADOR CRT - TUBO DE RAYOS CATÓDICOS

Versión: 2.0 (2025)
Desarrollado para: Universidad del Valle de Guatemala
Curso: Laboratorio de Física 3

CARACTERÍSTICAS:
   ✓ Simulación física realista del CRT
   ✓ Cálculos de trayectoria por tramos
   • Figuras de Lissajous completas
   ✓ Efectos visuales de persistencia
   ✓ Múltiples vistas del sistema
   ✓ Presets de configuración
   ✓ Control de velocidad de simulación

TECNOLOGÍA:
   • Python 3.x
   • Tkinter para interfaz gráfica
   • Cálculos físicos precisos
   • Renderizado en tiempo real

AUTORES:
   • [Nombre del estudiante]
   • Asesoría académica UVG

Este software es una herramienta educativa para 
comprender el funcionamiento de los tubos de rayos 
catódicos y las figuras de Lissajous.

© 2025 Universidad del Valle de Guatemala
"""
        
        self._agregar_texto_scroll(ventana, texto)

    def _crear_ventana_info(self, titulo, width, height):
        """Crea una ventana de información estándar"""
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.geometry(f"{width}x{height}")
        ventana.configure(bg="#1e2a3a")
        ventana.resizable(False, False)
        
        # Centrar ventana
        ventana.transient(self.root)
        ventana.grab_set()
        
        x = self.root.winfo_x() + (self.root.winfo_width() - width) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - height) // 2
        ventana.geometry(f"{width}x{height}+{x}+{y}")
        
        return ventana

    def _agregar_texto_scroll(self, ventana, texto):
        """Agrega texto con scroll a una ventana"""
        frame = tk.Frame(ventana, bg="#1e2a3a")
        frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Área de texto con scroll
        text_widget = tk.Text(frame, wrap=tk.WORD, bg="#0a0f1c", fg="#ffffff",
                             font=("Consolas", 10), relief=tk.FLAT, bd=0)
        
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)
        
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_widget.insert(tk.END, texto)
        text_widget.configure(state=tk.DISABLED)
        
        # Botón cerrar
        btn_frame = tk.Frame(ventana, bg="#1e2a3a")
        btn_frame.pack(fill=tk.X, padx=15, pady=(0, 15))
        
        btn_cerrar = tk.Button(btn_frame, text="Cerrar", command=ventana.destroy,
                              bg="#3498db", fg="white", font=("Consolas", 10, "bold"),
                              relief=tk.FLAT, padx=20, pady=8)
        btn_cerrar.pack(side=tk.RIGHT)

    def _on_closing(self):
        """Maneja el cierre seguro de la aplicación"""
        self.running = False
        try:
            self.root.destroy()
        except:
            pass

    def run(self):
        """Ejecuta la aplicación con inicialización completa"""
        # Centrar ventana en pantalla
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() - width) // 2
        y = (self.root.winfo_screenheight() - height) // 2
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Mostrar splash screen inicial
        self._mostrar_splash()
        
        # Iniciar loop principal
        self.root.mainloop()

    def _mostrar_splash(self):
        """Muestra pantalla de bienvenida"""
        splash = tk.Toplevel(self.root)
        splash.title("Simulador CRT")
        splash.geometry("500x300")
        splash.configure(bg="#0a0f1c")
        splash.resizable(False, False)
        splash.transient(self.root)
        splash.grab_set()
        
        # Centrar splash
        x = self.root.winfo_x() + (self.root.winfo_width() - 500) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - 300) // 2
        splash.geometry(f"500x300+{x}+{y}")
        
        # Contenido del splash
        frame = tk.Frame(splash, bg="#0a0f1c")
        frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Título principal
        titulo = tk.Label(frame, text="⚡ SIMULADOR CRT ⚡", 
                         font=("Consolas", 20, "bold"), fg="#00ffff", bg="#0a0f1c")
        titulo.pack(pady=20)
        
        # Subtítulo
        subtitulo = tk.Label(frame, text="Tubo de Rayos Catódicos", 
                            font=("Consolas", 12), fg="#ffffff", bg="#0a0f1c")
        subtitulo.pack(pady=5)
        
        # Información del proyecto
        info = tk.Label(frame, text="Universidad del Valle de Guatemala\nLaboratorio de Física 3 - 2025", 
                       font=("Consolas", 10), fg="#888888", bg="#0a0f1c", justify=tk.CENTER)
        info.pack(pady=15)
        
        # Mensaje de bienvenida
        mensaje = tk.Label(frame, 
                          text="Simulador educativo para el estudio de\ntubos de rayos catódicos y figuras de Lissajous",
                          font=("Consolas", 9), fg="#00ff00", bg="#0a0f1c", justify=tk.CENTER)
        mensaje.pack(pady=10)
        
        # Botón continuar
        btn_continuar = tk.Button(frame, text="🚀 INICIAR SIMULACIÓN", 
                                 command=splash.destroy,
                                 bg="#00ff00", fg="#000000", font=("Consolas", 12, "bold"),
                                 relief=tk.FLAT, padx=20, pady=8)
        btn_continuar.pack(pady=20)
        
        # Auto-cerrar después de 3 segundos si no se hace clic
        splash.after(3000, splash.destroy)