import tkinter as tk
import math
import time
from collections import deque

class Display:
    def __init__(self, root, width=900, height=600):
        # Frame principal para el display
        self.frame_principal = tk.Frame(root, bg="#1a1a1a", relief=tk.SUNKEN, bd=2)
        self.frame_principal.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Canvas principal
        self.canvas = tk.Canvas(self.frame_principal, width=width, height=height, 
                               bg="#0d1117", highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)
        
        # Dimensiones y posiciones
        self.width = width
        self.height = height
        
        # Historial de puntos para persistencia y Lissajous
        self.puntos_pantalla = deque(maxlen=2000)  # Aumentamos para Lissajous
        self.puntos_lissajous = deque(maxlen=1000)  # Puntos específicos para Lissajous
        self.tiempo_inicio = time.time()
        self.ultimo_tiempo_lissajous = 0
        
        # Configurar áreas de las vistas
        self._configurar_areas()
        self._dibujar_estructura_fija()

    def _configurar_areas(self):
        """Define las áreas para cada vista"""
        # Vista Lateral (izquierda)
        self.vista_lateral = {
            'x': 50, 'y': 80, 'width': 250, 'height': 180,
            'titulo': 'VISTA LATERAL'
        }
        
        # Vista Superior (centro)
        self.vista_superior = {
            'x': 320, 'y': 80, 'width': 250, 'height': 180,
            'titulo': 'VISTA SUPERIOR'
        }
        
        # Pantalla (derecha, más grande)
        self.pantalla = {
            'x': 590, 'y': 80, 'width': 280, 'height': 280,
            'titulo': 'PANTALLA'
        }

    def _dibujar_estructura_fija(self):
        """Dibuja la estructura fija del CRT"""
        # Título principal
        self.canvas.create_text(self.width//2, 30, text="SIMULACIÓN CRT - TUBO DE RAYOS CATÓDICOS",
                               font=("Arial", 16, "bold"), fill="white")
        
        # Dibujar cada vista
        self._dibujar_vista_lateral()
        self._dibujar_vista_superior()
        self._dibujar_pantalla()

    def _dibujar_vista_lateral(self):
        """Dibuja la vista lateral del CRT similar al diagrama técnico"""
        v = self.vista_lateral
        
        # Marco y título
        self.canvas.create_rectangle(v['x'], v['y'], v['x']+v['width'], v['y']+v['height'],
                                   outline="white", width=2)
        self.canvas.create_text(v['x']+v['width']//2, v['y']-15, text=v['titulo'],
                               font=("Arial", 12, "bold"), fill="cyan")
        
        # Centro vertical
        centro_y = v['y'] + v['height']//2
        
        # 1. Cátodo/Filamento (extremo izquierdo)
        catodo_x = v['x'] + 15
        self.canvas.create_line(catodo_x, centro_y-8, catodo_x, centro_y+8,
                               fill="orange", width=3)
        self.canvas.create_text(catodo_x, centro_y-15, text="Cátodo", 
                               font=("Arial", 7), fill="orange")
        
        # 2. Ánodo acelerador (cilindro)
        anodo_x = v['x'] + 35
        self.canvas.create_rectangle(anodo_x-5, centro_y-12, anodo_x+15, centro_y+12,
                                   outline="gray", fill="#34495e")
        self.canvas.create_text(anodo_x+5, centro_y-20, text="Ánodo", 
                               font=("Arial", 7), fill="gray")
        
        # 3. Estructura del tubo (contorno exterior)
        tubo_inicio_x = v['x'] + 25
        tubo_fin_x = v['x'] + v['width'] - 25
        
        # Parte estrecha del tubo
        self.canvas.create_line(tubo_inicio_x, centro_y-15, anodo_x+15, centro_y-15,
                               fill="white", width=1)
        self.canvas.create_line(tubo_inicio_x, centro_y+15, anodo_x+15, centro_y+15,
                               fill="white", width=1)
        
        # 4. Placas de deflexión vertical
        placa_x = v['x'] + 80
        placa_largo = 35
        separacion = 25
        
        # Placa superior
        self.canvas.create_rectangle(placa_x, centro_y-separacion, 
                                   placa_x+placa_largo, centro_y-separacion+5,
                                   outline="yellow", fill="#f39c12", width=2)
        self.canvas.create_text(placa_x+placa_largo//2, centro_y-separacion-8, text="+", 
                               font=("Arial", 10, "bold"), fill="yellow")
        
        # Placa inferior  
        self.canvas.create_rectangle(placa_x, centro_y+separacion-5, 
                                   placa_x+placa_largo, centro_y+separacion,
                                   outline="yellow", fill="#f39c12", width=2)
        self.canvas.create_text(placa_x+placa_largo//2, centro_y+separacion+12, text="-", 
                               font=("Arial", 10, "bold"), fill="yellow")
        
        # Etiqueta de placas
        self.canvas.create_text(placa_x+placa_largo//2, centro_y-35, text="Placas Y", 
                               font=("Arial", 8, "bold"), fill="yellow")
        
        # 5. Expansión del tubo después de las placas
        expansion_inicio_x = placa_x + placa_largo + 10
        # Líneas divergentes del tubo
        self.canvas.create_line(expansion_inicio_x, centro_y-separacion, 
                               tubo_fin_x, centro_y-40, fill="white", width=1)
        self.canvas.create_line(expansion_inicio_x, centro_y+separacion, 
                               tubo_fin_x, centro_y+40, fill="white", width=1)
        
        # 6. Pantalla (curva)
        pantalla_x = tubo_fin_x
        # Pantalla curvada
        self.canvas.create_arc(pantalla_x-15, centro_y-50, pantalla_x+15, centro_y+50,
                              start=90, extent=180, outline="lime", width=3, style="arc")
        self.canvas.create_text(pantalla_x+10, centro_y+55, text="Pantalla", 
                               font=("Arial", 8), fill="lime")
        
        # 7. Líneas de conexión eléctrica a las placas
        self.canvas.create_line(placa_x-10, centro_y-separacion+2, placa_x, centro_y-separacion+2,
                               fill="yellow", width=2)
        self.canvas.create_line(placa_x-10, centro_y+separacion-2, placa_x, centro_y+separacion-2,
                               fill="yellow", width=2)

    def _dibujar_vista_superior(self):
        """Dibuja la vista superior del CRT similar al diagrama técnico"""
        v = self.vista_superior
        
        # Marco y título
        self.canvas.create_rectangle(v['x'], v['y'], v['x']+v['width'], v['y']+v['height'],
                                   outline="white", width=2)
        self.canvas.create_text(v['x']+v['width']//2, v['y']-15, text=v['titulo'],
                               font=("Arial", 12, "bold"), fill="cyan")
        
        # Centro vertical
        centro_y = v['y'] + v['height']//2
        
        # 1. Cátodo/Filamento (extremo izquierdo)
        catodo_x = v['x'] + 15
        self.canvas.create_oval(catodo_x-2, centro_y-2, catodo_x+2, centro_y+2,
                               fill="orange", outline="orange")
        self.canvas.create_text(catodo_x, centro_y-12, text="Cátodo", 
                               font=("Arial", 7), fill="orange")
        
        # 2. Ánodo acelerador (vista desde arriba - circular)
        anodo_x = v['x'] + 35
        self.canvas.create_oval(anodo_x-8, centro_y-8, anodo_x+8, centro_y+8,
                               outline="gray", fill="#34495e")
        self.canvas.create_text(anodo_x, centro_y-18, text="Ánodo", 
                               font=("Arial", 7), fill="gray")
        
        # 3. Contorno del tubo (vista superior - más estrecho)
        tubo_inicio_x = v['x'] + 25
        tubo_medio_x = v['x'] + 90  # Donde están las placas verticales
        
        # Parte estrecha inicial
        self.canvas.create_line(tubo_inicio_x, centro_y-8, tubo_medio_x, centro_y-8,
                               fill="white", width=1)
        self.canvas.create_line(tubo_inicio_x, centro_y+8, tubo_medio_x, centro_y+8,
                               fill="white", width=1)
        
        # 4. Placas de deflexión horizontal (vista desde arriba)
        placa_x = v['x'] + 130
        placa_largo = 35
        separacion = 20
        
        # Placa izquierda
        self.canvas.create_rectangle(placa_x-separacion, centro_y-placa_largo//2, 
                                   placa_x-separacion+5, centro_y+placa_largo//2,
                                   outline="orange", fill="#e67e22", width=2)
        self.canvas.create_text(placa_x-separacion-12, centro_y, text="-", 
                               font=("Arial", 10, "bold"), fill="orange")
        
        # Placa derecha
        self.canvas.create_rectangle(placa_x+separacion-5, centro_y-placa_largo//2, 
                                   placa_x+separacion, centro_y+placa_largo//2,
                                   outline="orange", fill="#e67e22", width=2)
        self.canvas.create_text(placa_x+separacion+12, centro_y, text="+", 
                               font=("Arial", 10, "bold"), fill="orange")
        
        # Etiqueta de placas
        self.canvas.create_text(placa_x, centro_y-30, text="Placas X", 
                               font=("Arial", 8, "bold"), fill="orange")
        
        # 5. Expansión del tubo después de las placas horizontales
        tubo_fin_x = v['x'] + v['width'] - 25
        expansion_inicio_x = placa_x + separacion + 10
        
        # Expansión gradual
        self.canvas.create_line(tubo_medio_x, centro_y-8, expansion_inicio_x, centro_y-12,
                               fill="white", width=1)
        self.canvas.create_line(tubo_medio_x, centro_y+8, expansion_inicio_x, centro_y+12,
                               fill="white", width=1)
        
        # Parte final expandida
        self.canvas.create_line(expansion_inicio_x, centro_y-12, tubo_fin_x, centro_y-25,
                               fill="white", width=1)
        self.canvas.create_line(expansion_inicio_x, centro_y+12, tubo_fin_x, centro_y+25,
                               fill="white", width=1)
        
        # 6. Pantalla (vista desde arriba - línea gruesa)
        pantalla_x = tubo_fin_x
        self.canvas.create_line(pantalla_x, centro_y-30, pantalla_x, centro_y+30,
                               fill="lime", width=4)
        self.canvas.create_text(pantalla_x+10, centro_y+35, text="Pantalla", 
                               font=("Arial", 8), fill="lime")
        
        # 7. Líneas de conexión a las placas horizontales
        self.canvas.create_line(placa_x-separacion+2, centro_y-25, placa_x-separacion+2, centro_y-placa_largo//2,
                               fill="orange", width=2)
        self.canvas.create_line(placa_x+separacion-2, centro_y-25, placa_x+separacion-2, centro_y-placa_largo//2,
                               fill="orange", width=2)

    def _dibujar_pantalla(self):
        """Dibuja el área de la pantalla"""
        p = self.pantalla
        
        # Marco principal
        self.canvas.create_rectangle(p['x'], p['y'], p['x']+p['width'], p['y']+p['height'],
                                   outline="white", width=2)
        self.canvas.create_text(p['x']+p['width']//2, p['y']-15, text=p['titulo'],
                               font=("Arial", 12, "bold"), fill="lime")
        
        # Área activa de la pantalla (más pequeña que el marco)
        self.pantalla_activa = {
            'x': p['x'] + 20,
            'y': p['y'] + 20,
            'width': p['width'] - 40,
            'height': p['height'] - 40
        }
        
        # Fondo de la pantalla (como un CRT real)
        self.canvas.create_rectangle(self.pantalla_activa['x'], self.pantalla_activa['y'],
                                   self.pantalla_activa['x'] + self.pantalla_activa['width'],
                                   self.pantalla_activa['y'] + self.pantalla_activa['height'],
                                   outline="gray", fill="#001100", width=1)
        
        # Rejilla de referencia
        centro_x = self.pantalla_activa['x'] + self.pantalla_activa['width'] // 2
        centro_y = self.pantalla_activa['y'] + self.pantalla_activa['height'] // 2
        
        # Líneas de referencia
        self.canvas.create_line(centro_x, self.pantalla_activa['y'],
                               centro_x, self.pantalla_activa['y'] + self.pantalla_activa['height'],
                               fill="#003300", width=1, dash=(2, 2))
        self.canvas.create_line(self.pantalla_activa['x'], centro_y,
                               self.pantalla_activa['x'] + self.pantalla_activa['width'], centro_y,
                               fill="#003300", width=1, dash=(2, 2))

    def _calcular_posicion_electron(self, voltaje_v, voltaje_h, voltaje_aceleracion):
        """Calcula la posición del electrón en la pantalla"""
        # Parámetros físicos del CRT (valores realistas)
        longitud_placas = 0.05  # 5 cm
        separacion_placas = 0.02  # 2 cm
        distancia_placas_pantalla = 0.20  # 20 cm
        
        # Constantes físicas
        e = 1.602e-19  # Carga del electrón
        m = 9.109e-31  # Masa del electrón
        
        # Velocidad inicial del electrón
        v0 = math.sqrt(2 * e * abs(voltaje_aceleracion) / m) if voltaje_aceleracion > 0 else 1e6
        
        # Deflexión vertical
        campo_v = voltaje_v / separacion_placas if separacion_placas > 0 else 0
        aceleracion_v = -e * campo_v / m
        tiempo_en_placas = longitud_placas / v0
        
        # Velocidad vertical al salir de las placas
        vy = aceleracion_v * tiempo_en_placas
        # Desplazamiento vertical en las placas
        y_en_placas = 0.5 * aceleracion_v * tiempo_en_placas**2
        
        # Tiempo para llegar a la pantalla después de salir de las placas
        tiempo_a_pantalla = distancia_placas_pantalla / v0
        
        # Desplazamiento vertical total
        y_total = y_en_placas + vy * tiempo_a_pantalla
        
        # Lo mismo para horizontal
        campo_h = voltaje_h / separacion_placas if separacion_placas > 0 else 0
        aceleracion_h = e * campo_h / m
        vx = aceleracion_h * tiempo_en_placas
        x_en_placas = 0.5 * aceleracion_h * tiempo_en_placas**2
        x_total = x_en_placas + vx * tiempo_a_pantalla
        
        # Escalar a píxeles (ajustar sensibilidad)
        escala = 100  # Factor de escala para visualización
        pixel_x = x_total * escala
        pixel_y = y_total * escala
        
        return pixel_x, pixel_y

    def handle_draw(self, valores, tiempo_actual=None):
        """Actualiza la visualización completa"""
        if tiempo_actual is None:
            tiempo_actual = time.time() - self.tiempo_inicio
        
        # Limpiar elementos dinámicos
        self.canvas.delete("dinamico")
        
        # Obtener voltajes actuales
        if valores.get("modo_sinusoidal", False):
            # Modo sinusoidal - calcular voltajes para Lissajous
            freq_v = valores["frecuencia_vertical"]
            fase_v = math.radians(valores["fase_vertical"])
            freq_h = valores["frecuencia_horizontal"]
            fase_h = math.radians(valores["fase_horizontal"])
            
            # Amplitud ajustable (podemos hacerla proporcional al voltaje de aceleración)
            amplitud = min(300, valores["voltaje_aceleracion"] / 10)
            
            voltaje_v = amplitud * math.sin(2 * math.pi * freq_v * tiempo_actual + fase_v)
            voltaje_h = amplitud * math.sin(2 * math.pi * freq_h * tiempo_actual + fase_h)
            
            # Generar trayectoria completa de Lissajous
            self._generar_lissajous(freq_v, freq_h, fase_v, fase_h, amplitud, tiempo_actual, valores["persistencia"])
            
        else:
            voltaje_v = valores["voltaje_vertical"]
            voltaje_h = valores["voltaje_horizontal"]
        
        voltaje_aceleracion = valores["voltaje_aceleracion"]
        persistencia = valores["persistencia"]
        
        # Dibujar haz en vistas laterales
        self._dibujar_haz_lateral(voltaje_v)
        self._dibujar_haz_superior(voltaje_h)
        
        # Calcular posición en pantalla
        pixel_x, pixel_y = self._calcular_posicion_electron(voltaje_v, voltaje_h, voltaje_aceleracion)
        
        # Dibujar en pantalla
        if valores.get("modo_sinusoidal", False):
            self._dibujar_lissajous_pantalla(persistencia, tiempo_actual)
        else:
            self._dibujar_punto_pantalla(pixel_x, pixel_y, voltaje_aceleracion, persistencia, tiempo_actual)

    def _dibujar_haz_lateral(self, voltaje_v):
        """Dibuja el haz de electrones en vista lateral con trayectoria realista"""
        v = self.vista_lateral
        
        # Puntos clave del recorrido
        inicio_x = v['x'] + 35  # Desde el ánodo
        placa_inicio_x = v['x'] + 80
        placa_fin_x = v['x'] + 115
        pantalla_x = v['x'] + v['width'] - 25
        centro_y = v['y'] + v['height']//2
        
        # 1. Tramo recto inicial (desde ánodo hasta placas)
        self.canvas.create_line(inicio_x, centro_y, placa_inicio_x, centro_y,
                               fill="cyan", width=2, tags="dinamico")
        
        # 2. Deflexión en las placas (proporcional al voltaje)
        deflexion_max = 20  # Máxima deflexión en píxeles
        deflexion = min(max(voltaje_v / 25, -deflexion_max), deflexion_max)
        
        # Trayectoria curva dentro de las placas (aproximación parabólica)
        puntos_placa = []
        for i in range(8):
            x = placa_inicio_x + (placa_fin_x - placa_inicio_x) * i / 7
            # Deflexión parabólica dentro de las placas
            factor = (i / 7) ** 2  # Aceleración constante
            y_deflexion = centro_y + deflexion * factor
            puntos_placa.extend([x, y_deflexion])
        
        if len(puntos_placa) >= 4:
            self.canvas.create_line(puntos_placa, fill="cyan", width=2, 
                                   smooth=True, tags="dinamico")
        
        # 3. Trayectoria recta desde las placas hasta la pantalla
        y_salida_placas = centro_y + deflexion
        y_pantalla = centro_y + deflexion * 1.8  # Amplificación por distancia
        
        self.canvas.create_line(placa_fin_x, y_salida_placas, 
                               pantalla_x, y_pantalla,
                               fill="cyan", width=2, tags="dinamico")
        
        # 4. Punto del electrón en movimiento
        self.canvas.create_oval(pantalla_x-3, y_pantalla-3, 
                               pantalla_x+3, y_pantalla+3,
                               fill="cyan", outline="white", tags="dinamico")
        
        # 5. Indicador de intensidad de campo (líneas de fuerza)
        if abs(voltaje_v) > 10:  # Solo mostrar si hay voltaje significativo
            intensidad = min(abs(voltaje_v) / 100, 3)
            for i in range(int(intensidad)):
                offset = 5 + i * 3
                if voltaje_v > 0:  # Campo hacia abajo
                    self.canvas.create_line(placa_inicio_x + 10 + i*8, centro_y - 20,
                                           placa_inicio_x + 10 + i*8, centro_y + 20,
                                           fill="yellow", width=1, tags="dinamico",
                                           dash=(2, 2))
                else:  # Campo hacia arriba
                    self.canvas.create_line(placa_inicio_x + 10 + i*8, centro_y + 20,
                                           placa_inicio_x + 10 + i*8, centro_y - 20,
                                           fill="yellow", width=1, tags="dinamico",
                                           dash=(2, 2))

    def _dibujar_haz_superior(self, voltaje_h):
        """Dibuja el haz de electrones en vista superior con trayectoria realista"""
        v = self.vista_superior
        
        # Puntos clave del recorrido
        inicio_x = v['x'] + 35  # Desde el ánodo
        placas_inicio_x = v['x'] + 130 - 20  # Inicio de placas horizontales
        placas_fin_x = v['x'] + 130 + 20     # Fin de placas horizontales
        pantalla_x = v['x'] + v['width'] - 25
        centro_y = v['y'] + v['height']//2
        
        # 1. Tramo recto inicial (desde ánodo hasta placas horizontales)
        self.canvas.create_line(inicio_x, centro_y, placas_inicio_x, centro_y,
                               fill="orange", width=2, tags="dinamico")
        
        # 2. Deflexión en las placas horizontales
        deflexion_max = 15  # Máxima deflexión en píxeles
        deflexion = min(max(voltaje_h / 30, -deflexion_max), deflexion_max)
        
        # Trayectoria curva dentro de las placas
        puntos_placa = []
        for i in range(6):
            x = placas_inicio_x + (placas_fin_x - placas_inicio_x) * i / 5
            # Deflexión parabólica
            factor = (i / 5) ** 2
            y_deflexion = centro_y + deflexion * factor
            puntos_placa.extend([x, y_deflexion])
        
        if len(puntos_placa) >= 4:
            self.canvas.create_line(puntos_placa, fill="orange", width=2, 
                                   smooth=True, tags="dinamico")
        
        # 3. Trayectoria desde placas hasta pantalla
        y_salida_placas = centro_y + deflexion
        y_pantalla = centro_y + deflexion * 1.5  # Amplificación por distancia
        
        self.canvas.create_line(placas_fin_x, y_salida_placas, 
                               pantalla_x, y_pantalla,
                               fill="orange", width=2, tags="dinamico")
        
        # 4. Punto del electrón
        self.canvas.create_oval(pantalla_x-3, y_pantalla-3, 
                               pantalla_x+3, y_pantalla+3,
                               fill="orange", outline="white", tags="dinamico")
        
        # 5. Líneas de campo eléctrico horizontal
        if abs(voltaje_h) > 10:
            intensidad = min(abs(voltaje_h) / 100, 2)
            for i in range(int(intensidad)):
                y_offset = 8 + i * 4
                if voltaje_h > 0:  # Campo hacia la derecha
                    self.canvas.create_line(v['x'] + 115, centro_y - y_offset,
                                           v['x'] + 145, centro_y - y_offset,
                                           fill="orange", width=1, tags="dinamico",
                                           dash=(3, 3))
                    self.canvas.create_line(v['x'] + 115, centro_y + y_offset,
                                           v['x'] + 145, centro_y + y_offset,
                                           fill="orange", width=1, tags="dinamico",
                                           dash=(3, 3))
                else:  # Campo hacia la izquierda
                    self.canvas.create_line(v['x'] + 145, centro_y - y_offset,
                                           v['x'] + 115, centro_y - y_offset,
                                           fill="orange", width=1, tags="dinamico",
                                           dash=(3, 3))
                    self.canvas.create_line(v['x'] + 145, centro_y + y_offset,
                                           v['x'] + 115, centro_y + y_offset,
                                           fill="orange", width=1, tags="dinamico",
                                           dash=(3, 3))

    def _dibujar_punto_pantalla(self, pixel_x, pixel_y, voltaje_aceleracion, persistencia, tiempo_actual):
        """Dibuja el punto en la pantalla con persistencia"""
        centro_x = self.pantalla_activa['x'] + self.pantalla_activa['width'] // 2
        centro_y = self.pantalla_activa['y'] + self.pantalla_activa['height'] // 2
        
        # Posición final en píxeles
        pos_x = centro_x + pixel_x
        pos_y = centro_y - pixel_y  # Invertir Y para que positivo sea hacia arriba
        
        # Verificar que está dentro de los límites
        if (self.pantalla_activa['x'] <= pos_x <= self.pantalla_activa['x'] + self.pantalla_activa['width'] and
            self.pantalla_activa['y'] <= pos_y <= self.pantalla_activa['y'] + self.pantalla_activa['height']):
            
            # Agregar punto al historial
            intensidad = min(voltaje_aceleracion / 3000.0, 1.0)  # Normalizar intensidad
            self.puntos_pantalla.append({
                'x': pos_x, 'y': pos_y, 'tiempo': tiempo_actual, 
                'intensidad': intensidad
            })
            
            # Dibujar puntos con fade out
            self._dibujar_puntos_persistentes(persistencia, tiempo_actual)

    def _dibujar_puntos_persistentes(self, persistencia, tiempo_actual):
        """Dibuja todos los puntos con efecto de persistencia"""
        puntos_validos = []
        
        for punto in self.puntos_pantalla:
            edad = tiempo_actual - punto['tiempo']
            if edad <= persistencia:
                # Calcular alpha basado en la edad
                alpha = 1.0 - (edad / persistencia)
                intensidad = punto['intensidad'] * alpha
                
                # Color basado en intensidad
                verde = int(255 * intensidad)
                color = f"#{0:02x}{verde:02x}{0:02x}"
                
                # Tamaño del punto basado en intensidad
                size = max(1, int(3 * intensidad))
                
                self.canvas.create_oval(punto['x']-size, punto['y']-size,
                                       punto['x']+size, punto['y']+size,
                                       fill=color, outline="", tags="dinamico")
                
                puntos_validos.append(punto)
        
    def _generar_lissajous(self, freq_v, freq_h, fase_v, fase_h, amplitud, tiempo_actual, persistencia):
        """Genera los puntos para las figuras de Lissajous"""
        # Limpiar puntos antiguos periódicamente
        if tiempo_actual - self.ultimo_tiempo_lissajous > persistencia:
            self.puntos_lissajous.clear()
            self.ultimo_tiempo_lissajous = tiempo_actual
        
        # Generar múltiples puntos para crear una curva suave
        dt = 0.016  # Aproximadamente 60 FPS
        num_puntos = max(int(persistencia / dt), 50)  # Asegurar suficientes puntos
        
        for i in range(num_puntos):
            t = tiempo_actual - (num_puntos - i) * dt
            if t < 0:
                continue
                
            # Calcular posición Lissajous
            x = amplitud * math.sin(2 * math.pi * freq_h * t + fase_h)
            y = amplitud * math.sin(2 * math.pi * freq_v * t + fase_v)
            
            # Convertir a coordenadas de pantalla
            centro_x = self.pantalla_activa['x'] + self.pantalla_activa['width'] // 2
            centro_y = self.pantalla_activa['y'] + self.pantalla_activa['height'] // 2
            
            # Escalar apropiadamente para que quepa en la pantalla
            escala = min(self.pantalla_activa['width'], self.pantalla_activa['height']) * 0.35
            pixel_x = centro_x + x * escala / amplitud if amplitud > 0 else centro_x
            pixel_y = centro_y - y * escala / amplitud if amplitud > 0 else centro_y
            
            # Verificar límites
            if (self.pantalla_activa['x'] <= pixel_x <= self.pantalla_activa['x'] + self.pantalla_activa['width'] and
                self.pantalla_activa['y'] <= pixel_y <= self.pantalla_activa['y'] + self.pantalla_activa['height']):
                
                # Calcular intensidad basada en la edad del punto
                edad = tiempo_actual - t
                intensidad = max(0, 1.0 - edad / persistencia)
                
                self.puntos_lissajous.append({
                    'x': pixel_x,
                    'y': pixel_y,
                    'tiempo': t,
                    'intensidad': intensidad
                })

    def _dibujar_lissajous_pantalla(self, persistencia, tiempo_actual):
        """Dibuja la figura de Lissajous completa en la pantalla"""
        # Filtrar y actualizar intensidades
        puntos_validos = []
        
        for punto in self.puntos_lissajous:
            edad = tiempo_actual - punto['tiempo']
            if edad <= persistencia:
                # Recalcular intensidad
                alpha = max(0, 1.0 - edad / persistencia)
                punto['intensidad'] = alpha
                puntos_validos.append(punto)
        
        # Actualizar lista
        self.puntos_lissajous.clear()
        self.puntos_lissajous.extend(puntos_validos)
        
        # Dibujar puntos con diferentes intensidades y tamaños
        for punto in puntos_validos:
            intensidad = punto['intensidad']
            
            # Color basado en intensidad (verde brillante para CRT)
            verde = int(255 * intensidad)
            azul = int(100 * intensidad)  # Un poco de azul para efecto CRT
            color = f"#{0:02x}{verde:02x}{azul:02x}"
            
            # Tamaño variable basado en intensidad
            if intensidad > 0.8:
                size = 2
            elif intensidad > 0.5:
                size = 1.5
            else:
                size = 1
            
            self.canvas.create_oval(punto['x']-size, punto['y']-size,
                                   punto['x']+size, punto['y']+size,
                                   fill=color, outline="", tags="dinamico")
        
        # Dibujar líneas conectoras para mejor visualización (opcional)
        if len(puntos_validos) > 1:
            puntos_ordenados = sorted(puntos_validos, key=lambda p: p['tiempo'])
            for i in range(len(puntos_ordenados) - 1):
                p1 = puntos_ordenados[i]
                p2 = puntos_ordenados[i + 1]
                
                # Solo conectar puntos cercanos en tiempo
                if p2['tiempo'] - p1['tiempo'] < 0.1:
                    intensidad_linea = min(p1['intensidad'], p2['intensidad']) * 0.3
                    if intensidad_linea > 0.1:
                        verde_linea = int(150 * intensidad_linea)
                        color_linea = f"#{0:02x}{verde_linea:02x}{0:02x}"
                        
                        self.canvas.create_line(p1['x'], p1['y'], p2['x'], p2['y'],
                                               fill=color_linea, width=1, tags="dinamico")

    def _obtener_configuracion_lissajous(self, freq_v, freq_h, fase_v_grados, fase_h_grados):
        """Identifica el tipo de figura de Lissajous y retorna información"""
        # Simplificar las frecuencias a una fracción
        from fractions import Fraction
        try:
            ratio = Fraction(freq_v / freq_h).limit_denominator(10)
            ratio_v = ratio.numerator
            ratio_h = ratio.denominator
        except:
            ratio_v, ratio_h = 1, 1
        
        # Diferencia de fase
        diff_fase = abs(fase_v_grados - fase_h_grados) % 360
        
        # Clasificar la figura
        if ratio_v == ratio_h:  # 1:1
            if abs(diff_fase - 0) < 10 or abs(diff_fase - 180) < 10:
                return "Línea diagonal"
            elif abs(diff_fase - 90) < 10 or abs(diff_fase - 270) < 10:
                return "Círculo/Elipse"
            else:
                return "Elipse inclinada"
        elif (ratio_v == 2 and ratio_h == 1) or (ratio_v == 1 and ratio_h == 2):
            return "Figura en 8"
        elif (ratio_v == 3 and ratio_h == 2) or (ratio_v == 2 and ratio_h == 3):
            return "Patrón de pétalos"
        else:
            return f"Lissajous {ratio_v}:{ratio_h}"