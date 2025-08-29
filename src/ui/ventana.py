import tkinter as tk
from tkinter import ttk
import time
from .controles import Controles
from .display import Display

class Ventana:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulación CRT - Tubo de Rayos Catódicos")
        self.root.configure(bg="#1a1a1a")
        
        # Configurar geometría de la ventana
        self.root.geometry("1400x700")
        self.root.minsize(1200, 600)
        
        # Estilo mejorado
        self._configurar_estilo()
        
        # Crear componentes
        self.display = Display(self.root)
        self.controles = Controles(self.root)
        
        # Variables de control
        self.running = True
        self.tiempo_inicio = time.time()
        
        # Crear barra de estado
        self._crear_barra_estado()
        
        # Configurar eventos
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
        
        # Iniciar bucle de actualización
        self.update_loop()

    def _configurar_estilo(self):
        """Configura el estilo visual de la aplicación"""
        style = ttk.Style()
        
        # Configurar tema
        try:
            style.theme_use('clam')
        except:
            pass
        
        # Colores personalizados
        style.configure('TLabel', background='#2c3e50', foreground='white')
        style.configure('TFrame', background='#2c3e50')

    def _crear_barra_estado(self):
        """Crea la barra de estado en la parte inferior"""
        self.barra_estado = tk.Frame(self.root, bg="#34495e", height=30)
        self.barra_estado.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Información de estado
        self.status_label = tk.Label(self.barra_estado, 
                                   text="Estado: Simulación activa | FPS: -- | Modo: Manual",
                                   fg="white", bg="#34495e", font=("Arial", 9))
        self.status_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Información del proyecto
        info_label = tk.Label(self.barra_estado, 
                            text="UVG - Laboratorio de Física 3 - Proyecto CRT 2025",
                            fg="gray", bg="#34495e", font=("Arial", 9))
        info_label.pack(side=tk.RIGHT, padx=10, pady=5)
        
        # Variables para FPS
        self.frame_count = 0
        self.last_fps_time = time.time()
        self.fps = 0

    def update_loop(self):
        """Bucle principal de actualización"""
        if not self.running:
            return
            
        # Obtener valores de los controles
        valores = self.controles.get_valores()
        
        # Calcular tiempo actual
        tiempo_actual = time.time() - self.tiempo_inicio
        
        # Actualizar display
        self.display.handle_draw(valores, tiempo_actual)
        
        # Actualizar FPS y estado
        self._actualizar_fps()
        self._actualizar_estado(valores)
        
        # Programar siguiente actualización (aproximadamente 60 FPS)
        self.root.after(16, self.update_loop)

    def _actualizar_fps(self):
        """Calcula y actualiza el contador de FPS"""
        self.frame_count += 1
        tiempo_actual = time.time()
        
        if tiempo_actual - self.last_fps_time >= 1.0:  # Actualizar cada segundo
            self.fps = self.frame_count / (tiempo_actual - self.last_fps_time)
            self.frame_count = 0
            self.last_fps_time = tiempo_actual

    def _actualizar_estado(self, valores):
        """Actualiza la barra de estado"""
        modo = "Sinusoidal (Lissajous)" if valores.get("modo_sinusoidal", False) else "Manual"
        
        estado_text = f"Estado: Simulación activa | FPS: {self.fps:.1f} | Modo: {modo}"
        
        if valores.get("modo_sinusoidal", False):
            freq_v = valores["frecuencia_vertical"]
            freq_h = valores["frecuencia_horizontal"]
            fase_v = valores["fase_vertical"]
            fase_h = valores["fase_horizontal"]
            
            # Identificar tipo de figura
            if abs(freq_v - freq_h) < 0.1:  # Frecuencias similares
                if abs(abs(fase_v - fase_h) - 90) < 10:
                    tipo_figura = "Círculo"
                elif abs(fase_v - fase_h) < 10 or abs(abs(fase_v - fase_h) - 180) < 10:
                    tipo_figura = "Línea"
                else:
                    tipo_figura = "Elipse"
            elif abs(freq_v - 2*freq_h) < 0.1 or abs(2*freq_v - freq_h) < 0.1:
                tipo_figura = "Figura 8"
            else:
                tipo_figura = "Lissajous"
            
            estado_text += f" | {tipo_figura} | fV:{freq_v:.1f}Hz fH:{freq_h:.1f}Hz"
        else:
            volt_v = valores["voltaje_vertical"]
            volt_h = valores["voltaje_horizontal"]
            estado_text += f" | V:{volt_v:.0f}V H:{volt_h:.0f}V"
        
        self.status_label.config(text=estado_text)

    def _on_closing(self):
        """Maneja el cierre de la ventana"""
        self.running = False
        self.root.destroy()

    def run(self):
        """Ejecuta la aplicación"""
        # Centrar ventana en pantalla
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Mostrar mensaje de bienvenida
        self._mostrar_info_inicial()
        
        # Iniciar bucle principal
        self.root.mainloop()

    def _mostrar_info_inicial(self):
        """Muestra información inicial sobre el uso del programa"""
        info_window = tk.Toplevel(self.root)
        info_window.title("Información - Simulación CRT")
        info_window.geometry("500x400")
        info_window.configure(bg="#2c3e50")
        info_window.resizable(False, False)
        
        # Centrar ventana de info
        info_window.transient(self.root)
        info_window.grab_set()
        
        # Contenido
        frame = tk.Frame(info_window, bg="#2c3e50", padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        titulo = tk.Label(frame, text="SIMULACIÓN CRT", 
                         font=("Arial", 16, "bold"), fg="white", bg="#2c3e50")
        titulo.pack(pady=(0, 20))
        
        texto_info = """
INSTRUCCIONES DE USO:

1. MODO MANUAL:
   • Ajuste los voltajes manualmente con los controles
   • Observe cómo se deflecta el haz en las vistas lateral/superior
   • El punto verde en la pantalla muestra dónde impacta el electrón

2. MODO SINUSOIDAL (Figuras de Lissajous):
   • Active el modo sinusoidal
   • Ajuste frecuencias y fases para ambos canales
   • Observe las figuras de Lissajous en la pantalla

3. CONTROLES PRINCIPALES:
   • Voltaje Aceleración: Controla la velocidad del electrón
   • Voltajes V/H: Deflexión vertical y horizontal
   • Persistencia: Tiempo que permanecen visibles los puntos

4. VISTAS:
   • Vista Lateral: Muestra deflexión vertical
   • Vista Superior: Muestra deflexión horizontal  
   • Pantalla: Resultado final del impacto electrónico
"""
        
        info_label = tk.Label(frame, text=texto_info, 
                             font=("Arial", 10), fg="white", bg="#2c3e50",
                             justify=tk.LEFT, anchor="nw")
        info_label.pack(fill=tk.BOTH, expand=True)
        
        # Botón cerrar
        btn_cerrar = tk.Button(frame, text="Entendido", 
                              command=info_window.destroy,
                              bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                              relief=tk.FLAT, padx=20, pady=5)
        btn_cerrar.pack(pady=(20, 0))