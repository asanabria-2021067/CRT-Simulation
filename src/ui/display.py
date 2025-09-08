import tkinter as tk
import math
import time
from collections import deque

class Display:
    def __init__(self, root, width=1000, height=700):
        # Frame principal con diseño cyberpunk
        self.frame_principal = tk.Frame(root, bg="#000000", relief=tk.RAISED, bd=3)
        self.frame_principal.pack(side=tk.LEFT, padx=15, pady=15, fill=tk.BOTH, expand=True)
        
        # Canvas principal con efectos visuales
        self.canvas = tk.Canvas(self.frame_principal, width=width, height=height, 
                               bg="#0a0f1c", highlightthickness=2, highlightbackground="#00ffff")
        self.canvas.pack(padx=12, pady=12)
        
        # Dimensiones y configuración
        self.width = width
        self.height = height
        
        # Historial mejorado para persistencia realista
        self.puntos_pantalla = deque(maxlen=3000)  # Más puntos para mejor calidad
        self.puntos_lissajous = deque(maxlen=2000)  # Específico para Lissajous
        self.tiempo_inicio = time.time()
        self.ultimo_tiempo_limpiar = 0
        
        # Variables para física realista del CRT
        self.constantes_fisicas = {
            'e': 1.602e-19,  # Carga del electrón (C)
            'm': 9.109e-31,  # Masa del electrón (kg)
            'longitud_placas_v': 0.05,  # 5 cm
            'longitud_placas_h': 0.04,  # 4 cm
            'separacion_placas': 0.02,  # 2 cm
            'distancia_placas_v_pantalla': 0.25,  # 25 cm
            'distancia_placas_h_pantalla': 0.20,  # 20 cm
            'distancia_entre_placas': 0.08  # 8 cm entre placas V y H
        }
        
        # Configurar áreas optimizadas
        self._configurar_areas_mejoradas()
        self._dibujar_estructura_avanzada()

    def _configurar_areas_mejoradas(self):
        """Define las áreas con diseño mejorado y proporciones optimizadas"""
        # Vista Lateral (más detallada)
        self.vista_lateral = {
            'x': 40, 'y': 90, 'width': 280, 'height': 200,
            'titulo': '⚡ VISTA LATERAL - DEFLEXIÓN Y'
        }
        
        # Vista Superior (más detallada)
        self.vista_superior = {
            'x': 340, 'y': 90, 'width': 280, 'height': 200,
            'titulo': '⚡ VISTA SUPERIOR - DEFLEXIÓN X'
        }
        
        # Pantalla CRT (más grande y realista)
        self.pantalla = {
            'x': 650, 'y': 95, 'width': 320, 'height': 320,
            'titulo': '📺 PANTALLA CRT'
        }
        
        # Área de información (nueva)
        self.info_area = {
            'x': 40, 'y': 320, 'width': 580, 'height': 120,
            'titulo': '📊 INFORMACIÓN DEL SISTEMA'
        }

    def _dibujar_estructura_avanzada(self):
        """Dibuja la estructura con diseño futurista mejorado"""
        # Título principal con estilo cyberpunk
        self.canvas.create_text(self.width//2, 35, 
                               text="⚡ SIMULACIÓN CRT - TUBO DE RAYOS CATÓDICOS ⚡",
                               font=("Consolas", 18, "bold"), fill="#00ffff")
        
        # Línea decorativa superior
        self.canvas.create_line(50, 55, self.width-50, 55, fill="#00ffff", width=2)
        self.canvas.create_line(50, 57, self.width-50, 57, fill="#0080ff", width=1)
        
        # Dibujar cada vista mejorada
        self._dibujar_vista_lateral_avanzada()
        self._dibujar_vista_superior_avanzada() 
        self._dibujar_pantalla_avanzada()
        self._dibujar_area_informacion()

    def _dibujar_vista_lateral_avanzada(self):
        """Vista lateral con mayor detalle técnico y efectos visuales"""
        v = self.vista_lateral
        
        # Marco con efecto de profundidad
        self.canvas.create_rectangle(v['x']-2, v['y']-2, v['x']+v['width']+2, v['y']+v['height']+2,
                                   outline="#004080", fill="#001122", width=2)
        self.canvas.create_rectangle(v['x'], v['y'], v['x']+v['width'], v['y']+v['height'],
                                   outline="#00aaff", width=2)
        
        # Título con estilo
        self.canvas.create_text(v['x']+v['width']//2, v['y']-18, text=v['titulo'],
                               font=("Consolas", 12, "bold"), fill="#ffff00")
        
        centro_y = v['y'] + v['height']//2
        
        # 1. Cátodo mejorado con efectos
        catodo_x = v['x'] + 20
        self.canvas.create_rectangle(catodo_x-3, centro_y-10, catodo_x+3, centro_y+10,
                                   outline="#ff6600", fill="#ff4400", width=2)
        # Efecto de calor
        for i in range(3):
            self.canvas.create_line(catodo_x-8-i*2, centro_y-5+i*2, catodo_x-8-i*2, centro_y+5-i*2,
                                   fill="#ff6600", width=1, dash=(1,1))
        self.canvas.create_text(catodo_x, centro_y-18, text="CÁTODO", 
                               font=("Consolas", 8, "bold"), fill="#ff6600")
        
        # 2. Ánodo acelerador más realista
        anodo_x = v['x'] + 45
        self.canvas.create_rectangle(anodo_x-8, centro_y-15, anodo_x+12, centro_y+15,
                                   outline="#888888", fill="#555555")
        # Orificio del ánodo
        self.canvas.create_oval(anodo_x+4, centro_y-3, anodo_x+8, centro_y+3,
                               outline="#aaaaaa", fill="#333333")
        self.canvas.create_text(anodo_x+2, centro_y-22, text="ÁNODO", 
                               font=("Consolas", 8, "bold"), fill="#aaaaaa")
        
        # 3. Estructura del tubo con más detalle
        tubo_inicio_x = v['x'] + 30
        placa_v_x = v['x'] + 95
        
        # Paredes del tubo
        self.canvas.create_line(tubo_inicio_x, centro_y-18, placa_v_x-10, centro_y-18,
                               fill="#ffffff", width=2)
        self.canvas.create_line(tubo_inicio_x, centro_y+18, placa_v_x-10, centro_y+18,
                               fill="#ffffff", width=2)
        
        # 4. Placas de deflexión vertical mejoradas
        placa_largo = 40
        separacion = 28
        
        # Placa superior con detalle
        self.canvas.create_rectangle(placa_v_x, centro_y-separacion-3, 
                                   placa_v_x+placa_largo, centro_y-separacion+3,
                                   outline="#ffff00", fill="#cccc00", width=2)
        self.canvas.create_text(placa_v_x+placa_largo//2, centro_y-separacion-12, text="Y+", 
                               font=("Consolas", 12, "bold"), fill="#ffff00")
        
        # Placa inferior con detalle
        self.canvas.create_rectangle(placa_v_x, centro_y+separacion-3, 
                                   placa_v_x+placa_largo, centro_y+separacion+3,
                                   outline="#ffff00", fill="#cccc00", width=2)
        self.canvas.create_text(placa_v_x+placa_largo//2, centro_y+separacion+12, text="Y-", 
                               font=("Consolas", 12, "bold"), fill="#ffff00")
        
        # Conexiones eléctricas
        self.canvas.create_line(placa_v_x-12, centro_y-separacion, placa_v_x, centro_y-separacion,
                               fill="#ffff00", width=3)
        self.canvas.create_line(placa_v_x-12, centro_y+separacion, placa_v_x, centro_y+separacion,
                               fill="#ffff00", width=3)
        
        # 5. Placas de deflexión horizontal (vista lateral)
        placa_h_x = v['x'] + 160
        # Solo se ven los bordes desde esta vista
        self.canvas.create_line(placa_h_x, centro_y-25, placa_h_x, centro_y-15,
                               fill="#ff8800", width=3)
        self.canvas.create_line(placa_h_x, centro_y+15, placa_h_x, centro_y+25,
                               fill="#ff8800", width=3)
        self.canvas.create_text(placa_h_x, centro_y-30, text="PLACAS X", 
                               font=("Consolas", 8), fill="#ff8800")
        
        # 6. Expansión del tubo
        expansion_x = placa_h_x + 20
        pantalla_x = v['x'] + v['width'] - 30
        
        # Líneas divergentes con curvatura
        puntos_sup = [expansion_x, centro_y-18, expansion_x+30, centro_y-35, pantalla_x, centro_y-50]
        puntos_inf = [expansion_x, centro_y+18, expansion_x+30, centro_y+35, pantalla_x, centro_y+50]
        
        self.canvas.create_line(puntos_sup, fill="#ffffff", width=2, smooth=True)
        self.canvas.create_line(puntos_inf, fill="#ffffff", width=2, smooth=True)
        
        # 7. Pantalla curva más realista
        self.canvas.create_arc(pantalla_x-20, centro_y-60, pantalla_x+20, centro_y+60,
                              start=60, extent=240, outline="#00ff00", width=4, style="arc")
        # Revestimiento fosforescente
        self.canvas.create_arc(pantalla_x-18, centro_y-58, pantalla_x+18, centro_y+58,
                              start=60, extent=240, outline="#44ff44", width=2, style="arc")
        
        self.canvas.create_text(pantalla_x+5, centro_y+70, text="FÓSFORO", 
                               font=("Consolas", 8, "bold"), fill="#00ff00")

    def _dibujar_vista_superior_avanzada(self):
        """Vista superior con mayor detalle técnico"""
        v = self.vista_superior
        
        # Marco con efecto de profundidad
        self.canvas.create_rectangle(v['x']-2, v['y']-2, v['x']+v['width']+2, v['y']+v['height']+2,
                                   outline="#804000", fill="#221100", width=2)
        self.canvas.create_rectangle(v['x'], v['y'], v['x']+v['width'], v['y']+v['height'],
                                   outline="#ffaa00", width=2)
        
        # Título
        self.canvas.create_text(v['x']+v['width']//2, v['y']-18, text=v['titulo'],
                               font=("Consolas", 12, "bold"), fill="#ffff00")
        
        centro_y = v['y'] + v['height']//2
        
        # 1. Cátodo (vista superior - punto)
        catodo_x = v['x'] + 20
        self.canvas.create_oval(catodo_x-4, centro_y-4, catodo_x+4, centro_y+4,
                               fill="#ff4400", outline="#ff6600", width=2)
        self.canvas.create_text(catodo_x, centro_y-15, text="CÁTODO", 
                               font=("Consolas", 8, "bold"), fill="#ff6600")
        
        # 2. Ánodo (circular desde arriba)
        anodo_x = v['x'] + 45
        self.canvas.create_oval(anodo_x-10, centro_y-10, anodo_x+10, centro_y+10,
                               outline="#888888", fill="#555555")
        self.canvas.create_oval(anodo_x-3, centro_y-3, anodo_x+3, centro_y+3,
                               outline="#aaaaaa", fill="#333333")
        self.canvas.create_text(anodo_x, centro_y-18, text="ÁNODO", 
                               font=("Consolas", 8, "bold"), fill="#aaaaaa")
        
        # 3. Contorno del tubo
        tubo_inicio_x = v['x'] + 30
        placa_v_x = v['x'] + 95
        placa_h_x = v['x'] + 160
        
        # Sección antes de placas verticales
        self.canvas.create_line(tubo_inicio_x, centro_y-12, placa_v_x, centro_y-12,
                               fill="#ffffff", width=2)
        self.canvas.create_line(tubo_inicio_x, centro_y+12, placa_v_x, centro_y+12,
                               fill="#ffffff", width=2)
        
        # 4. Placas verticales (vista desde arriba - solo bordes)
        self.canvas.create_line(placa_v_x+10, centro_y-15, placa_v_x+30, centro_y-15,
                               fill="#ffff00", width=2)
        self.canvas.create_line(placa_v_x+10, centro_y+15, placa_v_x+30, centro_y+15,
                               fill="#ffff00", width=2)
        self.canvas.create_text(placa_v_x+20, centro_y-20, text="Y", 
                               font=("Consolas", 8), fill="#ffff00")
        
        # Continuar tubo hasta placas horizontales
        self.canvas.create_line(placa_v_x+40, centro_y-12, placa_h_x-20, centro_y-12,
                               fill="#ffffff", width=2)
        self.canvas.create_line(placa_v_x+40, centro_y+12, placa_h_x-20, centro_y+12,
                               fill="#ffffff", width=2)
        
        # 5. Placas de deflexión horizontal (principales en esta vista)
        separacion_h = 25
        placa_h_largo = 35
        
        # Placa izquierda
        self.canvas.create_rectangle(placa_h_x-separacion_h-3, centro_y-placa_h_largo//2, 
                                   placa_h_x-separacion_h+3, centro_y+placa_h_largo//2,
                                   outline="#ff8800", fill="#cc6600", width=2)
        self.canvas.create_text(placa_h_x-separacion_h-15, centro_y, text="X-", 
                               font=("Consolas", 12, "bold"), fill="#ff8800")
        
        # Placa derecha
        self.canvas.create_rectangle(placa_h_x+separacion_h-3, centro_y-placa_h_largo//2, 
                                   placa_h_x+separacion_h+3, centro_y+placa_h_largo//2,
                                   outline="#ff8800", fill="#cc6600", width=2)
        self.canvas.create_text(placa_h_x+separacion_h+15, centro_y, text="X+", 
                               font=("Consolas", 12, "bold"), fill="#ff8800")
        
        # Conexiones eléctricas horizontales
        self.canvas.create_line(placa_h_x-separacion_h, centro_y-25, 
                               placa_h_x-separacion_h, centro_y-placa_h_largo//2,
                               fill="#ff8800", width=3)
        self.canvas.create_line(placa_h_x+separacion_h, centro_y-25, 
                               placa_h_x+separacion_h, centro_y-placa_h_largo//2,
                               fill="#ff8800", width=3)
        
        # 6. Expansión final del tubo
        pantalla_x = v['x'] + v['width'] - 30
        expansion_x = placa_h_x + 30
        
        # Líneas de expansión lateral
        puntos_izq = [expansion_x, centro_y-12, expansion_x+20, centro_y-20, pantalla_x, centro_y-35]
        puntos_der = [expansion_x, centro_y+12, expansion_x+20, centro_y+20, pantalla_x, centro_y+35]
        
        self.canvas.create_line(puntos_izq, fill="#ffffff", width=2, smooth=True)
        self.canvas.create_line(puntos_der, fill="#ffffff", width=2, smooth=True)
        
        # 7. Pantalla (vista frontal)
        self.canvas.create_line(pantalla_x, centro_y-40, pantalla_x, centro_y+40,
                               fill="#00ff00", width=6)
        self.canvas.create_line(pantalla_x-2, centro_y-38, pantalla_x-2, centro_y+38,
                               fill="#44ff44", width=2)
        self.canvas.create_text(pantalla_x+5, centro_y+55, text="FÓSFORO", 
                               font=("Consolas", 8, "bold"), fill="#00ff00")

    def _dibujar_pantalla_avanzada(self):
        """Pantalla CRT con efectos realistas mejorados"""
        p = self.pantalla
        
        # Marco exterior con efectos
        self.canvas.create_rectangle(p['x']-3, p['y']-3, p['x']+p['width']+3, p['y']+p['height']+3,
                                   outline="#333333", fill="#111111", width=3)
        self.canvas.create_rectangle(p['x'], p['y'], p['x']+p['width'], p['y']+p['height'],
                                   outline="#00ff00", width=2)
        
        # Título con estilo
        self.canvas.create_text(p['x']+p['width']//2, p['y']-20, text=p['titulo'],
                               font=("Consolas", 14, "bold"), fill="#00ff00")
        
        # Área activa de la pantalla (con curvatura simulada)
        margen = 25
        self.pantalla_activa = {
            'x': p['x'] + margen,
            'y': p['y'] + margen,
            'width': p['width'] - 2*margen,
            'height': p['height'] - 2*margen
        }
        
        # Fondo de pantalla CRT con gradiente simulado
        centro_px = self.pantalla_activa['x'] + self.pantalla_activa['width'] // 2
        centro_py = self.pantalla_activa['y'] + self.pantalla_activa['height'] // 2
        
        # Múltiples rectángulos para simular gradiente
        for i in range(8):
            offset = i * 3
            intensidad = 15 - i
            color = f"#{intensidad:02x}{intensidad:02x}{intensidad:02x}"
            self.canvas.create_rectangle(
                self.pantalla_activa['x'] + offset, self.pantalla_activa['y'] + offset,
                self.pantalla_activa['x'] + self.pantalla_activa['width'] - offset,
                self.pantalla_activa['y'] + self.pantalla_activa['height'] - offset,
                outline="", fill=color
            )
        
        # Rejilla de referencia mejorada
        # Líneas principales
        self.canvas.create_line(centro_px, self.pantalla_activa['y'],
                               centro_px, self.pantalla_activa['y'] + self.pantalla_activa['height'],
                               fill="#003300", width=1, dash=(3, 3))
        self.canvas.create_line(self.pantalla_activa['x'], centro_py,
                               self.pantalla_activa['x'] + self.pantalla_activa['width'], centro_py,
                               fill="#003300", width=1, dash=(3, 3))
        
        # Rejilla fina
        for i in range(1, 8):
            x = self.pantalla_activa['x'] + (self.pantalla_activa['width'] * i) // 8
            y = self.pantalla_activa['y'] + (self.pantalla_activa['height'] * i) // 8
            
            if i != 4:  # No sobre la línea central
                self.canvas.create_line(x, self.pantalla_activa['y'],
                                       x, self.pantalla_activa['y'] + self.pantalla_activa['height'],
                                       fill="#002200", width=1, dash=(1, 4))
                self.canvas.create_line(self.pantalla_activa['x'], y,
                                       self.pantalla_activa['x'] + self.pantalla_activa['width'], y,
                                       fill="#002200", width=1, dash=(1, 4))
        
        # Marcadores de calibración
        marca_size = 5
        for i in [-1, 1]:
            for j in [-1, 1]:
                mx = centro_px + i * self.pantalla_activa['width'] // 4
                my = centro_py + j * self.pantalla_activa['height'] // 4
                self.canvas.create_line(mx-marca_size, my, mx+marca_size, my, fill="#006600", width=2)
                self.canvas.create_line(mx, my-marca_size, mx, my+marca_size, fill="#006600", width=2)
        
        # Indicadores de escala
        self.canvas.create_text(self.pantalla_activa['x'] - 15, centro_py, text="0V",
                               font=("Consolas", 8), fill="#666666", angle=90)
        self.canvas.create_text(centro_px, self.pantalla_activa['y'] + self.pantalla_activa['height'] + 15,
                               text="0V", font=("Consolas", 8), fill="#666666")

    def _dibujar_area_informacion(self):
        """Área de información del sistema con datos técnicos"""
        info = self.info_area
        
        # Marco
        self.canvas.create_rectangle(info['x'], info['y'], info['x']+info['width'], info['y']+info['height'],
                                   outline="#666666", fill="#0a0a0a", width=1)
        self.canvas.create_text(info['x']+10, info['y']+10, text=info['titulo'],
                               font=("Consolas", 10, "bold"), fill="#666666", anchor="w")
        
        # Línea separadora
        self.canvas.create_line(info['x']+10, info['y']+25, info['x']+info['width']-10, info['y']+25,
                               fill="#444444", width=1)

    def _calcular_posicion_realista(self, voltaje_v, voltaje_h, voltaje_aceleracion):
        """Cálculo físico realista mejorado con trayectoria por tramos"""
        c = self.constantes_fisicas
        
        # Velocidad inicial del electrón (energía cinética)
        if voltaje_aceleracion <= 0:
            return 0, 0
            
        v0 = math.sqrt(2 * c['e'] * abs(voltaje_aceleracion) / c['m'])
        
        # === TRAMO 1: Deflexión vertical ===
        campo_v = voltaje_v / c['separacion_placas'] if c['separacion_placas'] > 0 else 0
        aceleracion_v = -c['e'] * campo_v / c['m']  # Negativo porque el electrón tiene carga negativa
        
        tiempo_placas_v = c['longitud_placas_v'] / v0
        
        # Velocidad vertical al salir de las placas
        vy_salida = aceleracion_v * tiempo_placas_v
        # Desplazamiento vertical dentro de las placas
        y_en_placas_v = 0.5 * aceleracion_v * tiempo_placas_v**2
        
        # === TRAMO 2: Entre placas verticales y horizontales ===
        tiempo_entre_placas = c['distancia_entre_placas'] / v0
        y_entre_placas = vy_salida * tiempo_entre_placas
        
        # === TRAMO 3: Deflexión horizontal ===
        campo_h = voltaje_h / c['separacion_placas'] if c['separacion_placas'] > 0 else 0
        aceleracion_h = c['e'] * campo_h / c['m']  # Positivo para deflexión hacia la derecha
        
        tiempo_placas_h = c['longitud_placas_h'] / v0
        
        # Velocidad horizontal al salir de las placas
        vx_salida = aceleracion_h * tiempo_placas_h
        # Desplazamiento horizontal dentro de las placas
        x_en_placas_h = 0.5 * aceleracion_h * tiempo_placas_h**2
        
        # === TRAMO 4: Trayectoria libre hasta la pantalla ===
        # Tiempo para llegar a la pantalla desde las placas horizontales
        tiempo_a_pantalla = c['distancia_placas_h_pantalla'] / v0
        
        # Desplazamientos finales
        y_libre = vy_salida * tiempo_a_pantalla
        x_libre = vx_salida * tiempo_a_pantalla
        
        # === Posición total ===
        y_total = y_en_placas_v + y_entre_placas + y_libre
        x_total = x_en_placas_h + x_libre
        
        # Escalar a píxeles con factor de calibración realista
        escala = 800  # Factor ajustado para buena visualización
        pixel_x = x_total * escala
        pixel_y = y_total * escala
        
        return pixel_x, pixel_y

    def handle_draw(self, valores, tiempo_actual=None):
        """Actualización principal con física mejorada"""
        if tiempo_actual is None:
            tiempo_actual = time.time() - self.tiempo_inicio
        
        # Limpiar elementos dinámicos
        self.canvas.delete("dinamico")
        self.canvas.delete("haz")
        self.canvas.delete("punto")
        
        # Obtener voltajes
        voltaje_aceleracion = valores.get("voltaje_aceleracion", 2000)
        
        if valores.get("modo_sinusoidal", False):
            # Calcular voltajes sinusoidales para Lissajous
            freq_v = valores.get("frecuencia_vertical", 1.0)
            fase_v = math.radians(valores.get("fase_vertical", 0))
            freq_h = valores.get("frecuencia_horizontal", 1.0) 
            fase_h = math.radians(valores.get("fase_horizontal", 0))
            
            # Amplitud proporcional al voltaje de aceleración
            amplitud_base = min(500, max(200, voltaje_aceleracion / 8))
            
            voltaje_v = amplitud_base * math.sin(2 * math.pi * freq_v * tiempo_actual + fase_v)
            voltaje_h = amplitud_base * math.sin(2 * math.pi * freq_h * tiempo_actual + fase_h)
            
            # Generar Lissajous completa
            self._generar_lissajous_mejorada(freq_v, freq_h, fase_v, fase_h, amplitud_base, 
                                           tiempo_actual, valores.get("persistencia", 1.5),
                                           voltaje_aceleracion)
        else:
            voltaje_v = valores.get("voltaje_vertical", 0)
            voltaje_h = valores.get("voltaje_horizontal", 0)
        
        # Dibujar haces en las vistas
        self._dibujar_haz_lateral_mejorado(voltaje_v, voltaje_aceleracion)
        self._dibujar_haz_superior_mejorado(voltaje_h, voltaje_aceleracion)
        
        # Calcular posición en pantalla
        pixel_x, pixel_y = self._calcular_posicion_realista(voltaje_v, voltaje_h, voltaje_aceleracion)
        
        # Dibujar en pantalla
        if valores.get("modo_sinusoidal", False):
            self._dibujar_lissajous_pantalla_mejorada(valores.get("persistencia", 1.5), tiempo_actual)
        else:
            self._dibujar_punto_pantalla_mejorado(pixel_x, pixel_y, voltaje_aceleracion, 
                                                valores.get("persistencia", 1.5), tiempo_actual, 
                                                valores.get("brillo", 1.0))
        
        # Actualizar información del sistema
        self._actualizar_informacion_sistema(valores, tiempo_actual, pixel_x, pixel_y)

    def _dibujar_haz_lateral_mejorado(self, voltaje_v, voltaje_aceleracion):
        """Haz de electrones en vista lateral con efectos realistas"""
        v = self.vista_lateral
        
        # Puntos clave mejorados
        catodo_x = v['x'] + 20
        anodo_x = v['x'] + 45
        placas_v_inicio = v['x'] + 95
        placas_v_fin = v['x'] + 135
        placas_h_x = v['x'] + 160
        pantalla_x = v['x'] + v['width'] - 30
        centro_y = v['y'] + v['height']//2
        
        # Intensidad del haz basada en voltaje de aceleración
        intensidad_haz = min(voltaje_aceleracion / 5000.0, 1.0)
        color_haz = f"#00{int(255*intensidad_haz):02x}{int(255*intensidad_haz):02x}"
        ancho_haz = max(1, int(3 * intensidad_haz))
        
        # 1. Tramo inicial (cátodo a ánodo)
        self.canvas.create_line(catodo_x+3, centro_y, anodo_x-8, centro_y,
                               fill=color_haz, width=ancho_haz, tags="haz")
        
        # Efecto de aceleración (líneas convergentes)
        for i in range(3):
            offset = (i-1) * 2
            self.canvas.create_line(catodo_x+3, centro_y+offset, anodo_x-8, centro_y+offset//2,
                                   fill=color_haz, width=1, tags="haz")
        
        # 2. Tramo rectilíneo (ánodo a placas verticales)
        self.canvas.create_line(anodo_x+12, centro_y, placas_v_inicio, centro_y,
                               fill=color_haz, width=ancho_haz, tags="haz")
        
        # 3. Deflexión en placas verticales
        deflexion_max = 35
        deflexion = max(-deflexion_max, min(deflexion_max, voltaje_v / 15))
        
        # Trayectoria parabólica dentro de las placas
        puntos_deflexion = []
        num_segmentos = 12
        for i in range(num_segmentos + 1):
            t = i / num_segmentos
            x = placas_v_inicio + (placas_v_fin - placas_v_inicio) * t
            # Deflexión parabólica (aceleración constante)
            y = centro_y + deflexion * (t**2)
            puntos_deflexion.extend([x, y])
        
        if len(puntos_deflexion) >= 4:
            self.canvas.create_line(puntos_deflexion, fill=color_haz, width=ancho_haz, 
                                   smooth=True, tags="haz")
        
        # 4. Tramo entre placas
        y_salida_v = centro_y + deflexion
        self.canvas.create_line(placas_v_fin, y_salida_v, placas_h_x, y_salida_v,
                               fill=color_haz, width=ancho_haz, tags="haz")
        
        # 5. Tramo final (placas horizontales a pantalla)
        # La deflexión vertical se mantiene
        y_pantalla = y_salida_v
        self.canvas.create_line(placas_h_x+20, y_salida_v, pantalla_x, y_pantalla,
                               fill=color_haz, width=ancho_haz, tags="haz")
        
        # 6. Punto de impacto en la pantalla lateral
        impact_size = max(2, int(4 * intensidad_haz))
        self.canvas.create_oval(pantalla_x-impact_size, y_pantalla-impact_size,
                               pantalla_x+impact_size, y_pantalla+impact_size,
                               fill="#ffffff", outline=color_haz, width=2, tags="punto")
        
        # 7. Líneas de campo eléctrico vertical
        if abs(voltaje_v) > 10:
            self._dibujar_campo_electrico_v(placas_v_inicio, placas_v_fin, centro_y, voltaje_v)

    def _dibujar_haz_superior_mejorado(self, voltaje_h, voltaje_aceleracion):
        """Haz de electrones en vista superior con efectos realistas"""
        v = self.vista_superior
        
        # Puntos clave
        catodo_x = v['x'] + 20
        anodo_x = v['x'] + 45
        placas_v_x = v['x'] + 115
        placas_h_inicio = v['x'] + 140
        placas_h_fin = v['x'] + 175
        pantalla_x = v['x'] + v['width'] - 30
        centro_y = v['y'] + v['height']//2
        
        # Intensidad del haz
        intensidad_haz = min(voltaje_aceleracion / 5000.0, 1.0)
        color_haz = f"#{int(255*intensidad_haz):02x}{int(180*intensidad_haz):02x}00"
        ancho_haz = max(1, int(3 * intensidad_haz))
        
        # 1. Tramo inicial
        self.canvas.create_line(catodo_x, centro_y, anodo_x-10, centro_y,
                               fill=color_haz, width=ancho_haz, tags="haz")
        
        # 2. Tramo rectilíneo hasta placas verticales
        self.canvas.create_line(anodo_x+10, centro_y, placas_v_x, centro_y,
                               fill=color_haz, width=ancho_haz, tags="haz")
        
        # 3. A través de las placas verticales (sin deflexión horizontal aquí)
        self.canvas.create_line(placas_v_x, centro_y, placas_h_inicio, centro_y,
                               fill=color_haz, width=ancho_haz, tags="haz")
        
        # 4. Deflexión en placas horizontales
        deflexion_h_max = 25
        deflexion_h = max(-deflexion_h_max, min(deflexion_h_max, voltaje_h / 20))
        
        # Trayectoria parabólica en placas horizontales
        puntos_deflexion_h = []
        num_segmentos = 8
        for i in range(num_segmentos + 1):
            t = i / num_segmentos
            x = placas_h_inicio + (placas_h_fin - placas_h_inicio) * t
            y = centro_y + deflexion_h * (t**2)
            puntos_deflexion_h.extend([x, y])
        
        if len(puntos_deflexion_h) >= 4:
            self.canvas.create_line(puntos_deflexion_h, fill=color_haz, width=ancho_haz,
                                   smooth=True, tags="haz")
        
        # 5. Tramo final a pantalla
        y_salida_h = centro_y + deflexion_h
        y_pantalla_final = centro_y + deflexion_h * 1.3  # Amplificación por distancia
        
        self.canvas.create_line(placas_h_fin, y_salida_h, pantalla_x, y_pantalla_final,
                               fill=color_haz, width=ancho_haz, tags="haz")
        
        # 6. Punto de impacto
        impact_size = max(2, int(4 * intensidad_haz))
        self.canvas.create_oval(pantalla_x-impact_size, y_pantalla_final-impact_size,
                               pantalla_x+impact_size, y_pantalla_final+impact_size,
                               fill="#ffffff", outline=color_haz, width=2, tags="punto")
        
        # 7. Campo eléctrico horizontal
        if abs(voltaje_h) > 10:
            self._dibujar_campo_electrico_h(placas_h_inicio, placas_h_fin, centro_y, voltaje_h)

    def _dibujar_campo_electrico_v(self, x_inicio, x_fin, centro_y, voltaje):
        """Dibuja líneas de campo eléctrico vertical"""
        num_lineas = min(int(abs(voltaje) / 50), 6)
        direccion = 1 if voltaje > 0 else -1
        
        for i in range(num_lineas):
            x = x_inicio + 5 + i * 5
            if x < x_fin:
                # Líneas de campo
                y1 = centro_y - 20 * direccion
                y2 = centro_y + 20 * direccion
                self.canvas.create_line(x, y1, x, y2, fill="#ffff00", width=1, 
                                       tags="haz", dash=(2, 3))
                # Flechas indicando dirección
                if i % 2 == 0:
                    arrow_y = centro_y + 10 * direccion
                    self.canvas.create_line(x, arrow_y, x-2, arrow_y-3*direccion, 
                                           fill="#ffff00", width=1, tags="haz")
                    self.canvas.create_line(x, arrow_y, x+2, arrow_y-3*direccion, 
                                           fill="#ffff00", width=1, tags="haz")

    def _dibujar_campo_electrico_h(self, x_inicio, x_fin, centro_y, voltaje):
        """Dibuja líneas de campo eléctrico horizontal"""
        num_lineas = min(int(abs(voltaje) / 60), 4)
        direccion = 1 if voltaje > 0 else -1
        
        x_medio = (x_inicio + x_fin) // 2
        for i in range(num_lineas):
            y = centro_y - 15 + i * 8
            # Líneas horizontales de campo
            x1 = x_medio - 15 * direccion
            x2 = x_medio + 15 * direccion
            self.canvas.create_line(x1, y, x2, y, fill="#ff8800", width=1,
                                   tags="haz", dash=(3, 2))
            # Flechas
            if i % 2 == 0:
                arrow_x = x_medio + 8 * direccion
                self.canvas.create_line(arrow_x, y, arrow_x-3*direccion, y-2,
                                       fill="#ff8800", width=1, tags="haz")
                self.canvas.create_line(arrow_x, y, arrow_x-3*direccion, y+2,
                                       fill="#ff8800", width=1, tags="haz")

    def _generar_lissajous_mejorada(self, freq_v, freq_h, fase_v, fase_h, amplitud, tiempo_actual, persistencia, voltaje_aceleracion):
        """Genera figuras de Lissajous con mayor precisión y efectos"""
        # Limpiar puntos antiguos periódicamente
        if tiempo_actual - self.ultimo_tiempo_limpiar > persistencia * 1.2:
            # Solo limpiar puntos muy antiguos
            puntos_validos = []
            for punto in self.puntos_lissajous:
                if tiempo_actual - punto['tiempo'] <= persistencia:
                    puntos_validos.append(punto)
            self.puntos_lissajous.clear()
            self.puntos_lissajous.extend(puntos_validos)
            self.ultimo_tiempo_limpiar = tiempo_actual
        
        # Parámetros de generación adaptivos
        dt = 0.008  # Mayor frecuencia de muestreo para suavidad
        puntos_por_ciclo = max(100, int(500 / max(freq_v, freq_h)))
        
        # Generar puntos recientes
        for i in range(15):  # Menos puntos por frame para mejor rendimiento
            t = tiempo_actual - i * dt
            if t < 0:
                continue
            
            # Calcular voltajes con física realista
            voltaje_v = amplitud * math.sin(2 * math.pi * freq_v * t + fase_v)
            voltaje_h = amplitud * math.sin(2 * math.pi * freq_h * t + fase_h)
            
            # Usar la física realista del CRT
            pixel_x, pixel_y = self._calcular_posicion_realista(voltaje_v, voltaje_h, voltaje_aceleracion)
            
            # Convertir a coordenadas de pantalla
            centro_x = self.pantalla_activa['x'] + self.pantalla_activa['width'] // 2
            centro_y = self.pantalla_activa['y'] + self.pantalla_activa['height'] // 2
            
            pos_x = centro_x - pixel_x
            pos_y = centro_y - pixel_y  # Invertir Y
            
            # Verificar límites
            if (self.pantalla_activa['x'] <= pos_x <= self.pantalla_activa['x'] + self.pantalla_activa['width'] and
                self.pantalla_activa['y'] <= pos_y <= self.pantalla_activa['y'] + self.pantalla_activa['height']):
                
                # Intensidad basada en velocidad y edad
                edad = tiempo_actual - t
                intensidad = max(0, 1.0 - edad / persistencia)
                
                # Factor de brillo basado en voltaje de aceleración
                brillo = min(voltaje_aceleracion / 3000.0, 1.2)
                intensidad *= brillo
                
                self.puntos_lissajous.append({
                    'x': pos_x,
                    'y': pos_y,
                    'tiempo': t,
                    'intensidad': intensidad,
                    'freq_v': freq_v,
                    'freq_h': freq_h
                })

    def _dibujar_lissajous_pantalla_mejorada(self, persistencia, tiempo_actual):
        """Dibuja Lissajous con efectos de CRT realistas"""
        puntos_validos = []
        
        # Procesar puntos por intensidad para dibujar los más brillantes encima
        puntos_por_intensidad = {}
        
        for punto in self.puntos_lissajous:
            edad = tiempo_actual - punto['tiempo']
            if edad <= persistencia:
                # Recalcular intensidad con decay exponencial más realista
                alpha = math.exp(-edad / (persistencia * 0.7))
                punto['intensidad'] = alpha * punto.get('intensidad', 1.0)
                
                # Categorizar por intensidad
                categoria = int(punto['intensidad'] * 10)
                if categoria not in puntos_por_intensidad:
                    puntos_por_intensidad[categoria] = []
                puntos_por_intensidad[categoria].append(punto)
                
                puntos_validos.append(punto)
        
        # Actualizar lista
        self.puntos_lissajous.clear()
        self.puntos_lissajous.extend(puntos_validos)
        
        # Dibujar por categorías de intensidad (menos intensos primero)
        for categoria in sorted(puntos_por_intensidad.keys()):
            puntos_categoria = puntos_por_intensidad[categoria]
            
            for punto in puntos_categoria:
                intensidad = punto['intensidad']
                
                if intensidad < 0.05:
                    continue
                
                # Color con efecto CRT (verde con toque azul)
                verde = min(255, int(255 * intensidad))
                azul = min(180, int(120 * intensidad))
                rojo = min(100, int(50 * intensidad))
                color = f"#{rojo:02x}{verde:02x}{azul:02x}"
                
                # Tamaño del punto basado en intensidad
                if intensidad > 0.8:
                    size = 2.5
                    # Halo para puntos muy brillantes
                    halo_color = f"#{int(rojo*0.3):02x}{int(verde*0.3):02x}{int(azul*0.3):02x}"
                    self.canvas.create_oval(punto['x']-4, punto['y']-4,
                                           punto['x']+4, punto['y']+4,
                                           fill=halo_color, outline="", tags="punto")
                elif intensidad > 0.5:
                    size = 1.8
                elif intensidad > 0.2:
                    size = 1.2
                else:
                    size = 0.8
                
                # Punto principal
                self.canvas.create_oval(punto['x']-size, punto['y']-size,
                                       punto['x']+size, punto['y']+size,
                                       fill=color, outline="", tags="punto")
        
        # Opcional: líneas conectoras para figuras complejas
        if len(puntos_validos) > 1 and any(p['intensidad'] > 0.3 for p in puntos_validos):
            self._dibujar_conectores_lissajous(puntos_validos)

    def _dibujar_punto_pantalla_mejorado(self, pixel_x, pixel_y, voltaje_aceleracion, persistencia, tiempo_actual, brillo):
        """Dibuja punto único con persistencia mejorada"""
        centro_x = self.pantalla_activa['x'] + self.pantalla_activa['width'] // 2
        centro_y = self.pantalla_activa['y'] + self.pantalla_activa['height'] // 2
        
        pos_x = centro_x + pixel_x
        pos_y = centro_y - pixel_y
        
        # Verificar límites
        if (self.pantalla_activa['x'] <= pos_x <= self.pantalla_activa['x'] + self.pantalla_activa['width'] and
            self.pantalla_activa['y'] <= pos_y <= self.pantalla_activa['y'] + self.pantalla_activa['height']):
            
            # Intensidad basada en voltaje de aceleración y brillo
            intensidad = min(voltaje_aceleracion / 3000.0 * brillo, 1.5)
            
            self.puntos_pantalla.append({
                'x': pos_x, 'y': pos_y, 'tiempo': tiempo_actual, 
                'intensidad': intensidad
            })
            
            # Dibujar puntos con fade out
            puntos_validos = []
            for punto in self.puntos_pantalla:
                edad = tiempo_actual - punto['tiempo']
                if edad <= persistencia:
                    alpha = max(0, 1.0 - edad / persistencia)
                    intensidad_actual = punto['intensidad'] * alpha
                    
                    if intensidad_actual > 0.05:
                        verde = min(255, int(255 * intensidad_actual))
                        azul = min(150, int(100 * intensidad_actual))
                        color = f"#{0:02x}{verde:02x}{azul:02x}"
                        
                        size = max(1, int(3 * intensidad_actual))
                        
                        # Halo para puntos brillantes
                        if intensidad_actual > 0.7:
                            halo_color = f"#{0:02x}{int(verde*0.3):02x}{int(azul*0.3):02x}"
                            self.canvas.create_oval(punto['x']-size*2, punto['y']-size*2,
                                                   punto['x']+size*2, punto['y']+size*2,
                                                   fill=halo_color, outline="", tags="punto")
                        
                        self.canvas.create_oval(punto['x']-size, punto['y']-size,
                                               punto['x']+size, punto['y']+size,
                                               fill=color, outline="", tags="punto")
                    
                    puntos_validos.append(punto)
            
            # Actualizar lista
            self.puntos_pantalla.clear()
            self.puntos_pantalla.extend(puntos_validos)

    def _dibujar_conectores_lissajous(self, puntos):
        """Dibuja líneas conectoras sutiles para figuras de Lissajous"""
        puntos_ordenados = sorted([p for p in puntos if p['intensidad'] > 0.2], 
                                 key=lambda p: p['tiempo'])
        
        for i in range(len(puntos_ordenados) - 1):
            p1 = puntos_ordenados[i]
            p2 = puntos_ordenados[i + 1]
            
            # Solo conectar puntos muy cercanos en tiempo
            if p2['tiempo'] - p1['tiempo'] < 0.05:
                intensidad_linea = min(p1['intensidad'], p2['intensidad']) * 0.15
                if intensidad_linea > 0.03:
                    verde = int(120 * intensidad_linea)
                    azul = int(80 * intensidad_linea)
                    color_linea = f"#{0:02x}{verde:02x}{azul:02x}"
                    
                    self.canvas.create_line(p1['x'], p1['y'], p2['x'], p2['y'],
                                           fill=color_linea, width=1, tags="punto")

    def _actualizar_informacion_sistema(self, valores, tiempo_actual, pixel_x, pixel_y):
        """Actualiza el área de información con datos del sistema"""
        info = self.info_area
        
        # Limpiar área de información
        self.canvas.delete("info")
        
        # Información básica
        col1_x = info['x'] + 15
        col2_x = info['x'] + 200
        col3_x = info['x'] + 400
        y_start = info['y'] + 35
        
        # Columna 1: Voltajes
        self.canvas.create_text(col1_x, y_start, text="VOLTAJES:", 
                               font=("Consolas", 9, "bold"), fill="#00ffff", anchor="w", tags="info")
        
        voltaje_aceleracion = valores.get("voltaje_aceleracion", 0)
        self.canvas.create_text(col1_x, y_start + 15, 
                               text=f"Aceleración: {voltaje_aceleracion:.0f} V",
                               font=("Consolas", 8), fill="#ffffff", anchor="w", tags="info")
        
        if valores.get("modo_sinusoidal", False):
            freq_v = valores.get("frecuencia_vertical", 0)
            freq_h = valores.get("frecuencia_horizontal", 0)
            self.canvas.create_text(col1_x, y_start + 30,
                                   text=f"Modo: Sinusoidal {freq_v:.1f}:{freq_h:.1f} Hz",
                                   font=("Consolas", 8), fill="#ffff00", anchor="w", tags="info")
            
            # Identificar tipo de figura
            tipo_figura = self._identificar_figura_lissajous(freq_v, freq_h, 
                                                            valores.get("fase_vertical", 0),
                                                            valores.get("fase_horizontal", 0))
            self.canvas.create_text(col1_x, y_start + 45,
                                   text=f"Figura: {tipo_figura}",
                                   font=("Consolas", 8), fill="#00ff00", anchor="w", tags="info")
        else:
            voltaje_v = valores.get("voltaje_vertical", 0)
            voltaje_h = valores.get("voltaje_horizontal", 0)
            self.canvas.create_text(col1_x, y_start + 30,
                                   text=f"Vertical: {voltaje_v:.0f} V",
                                   font=("Consolas", 8), fill="#ffff00", anchor="w", tags="info")
            self.canvas.create_text(col1_x, y_start + 45,
                                   text=f"Horizontal: {voltaje_h:.0f} V",
                                   font=("Consolas", 8), fill="#ff8800", anchor="w", tags="info")
        
        # Columna 2: Física
        self.canvas.create_text(col2_x, y_start, text="FÍSICA:",
                               font=("Consolas", 9, "bold"), fill="#00ffff", anchor="w", tags="info")
        
        # Calcular velocidad inicial
        if voltaje_aceleracion > 0:
            v0 = math.sqrt(2 * 1.602e-19 * voltaje_aceleracion / 9.109e-31)
            self.canvas.create_text(col2_x, y_start + 15,
                                   text=f"Velocidad: {v0/1e6:.1f} Mm/s",
                                   font=("Consolas", 8), fill="#ffffff", anchor="w", tags="info")
        
        # Posición en pantalla
        self.canvas.create_text(col2_x, y_start + 30,
                               text=f"Deflexión X: {pixel_x:.1f} px",
                               font=("Consolas", 8), fill="#ff8800", anchor="w", tags="info")
        self.canvas.create_text(col2_x, y_start + 45,
                               text=f"Deflexión Y: {-pixel_y:.1f} px",
                               font=("Consolas", 8), fill="#ffff00", anchor="w", tags="info")
        
        # Columna 3: Sistema
        self.canvas.create_text(col3_x, y_start, text="SISTEMA:",
                               font=("Consolas", 9, "bold"), fill="#00ffff", anchor="w", tags="info")
        
        persistencia = valores.get("persistencia", 1.0)
        self.canvas.create_text(col3_x, y_start + 15,
                               text=f"Persistencia: {persistencia:.2f} s",
                               font=("Consolas", 8), fill="#ffffff", anchor="w", tags="info")
        
        brillo = valores.get("brillo", 1.0)
        self.canvas.create_text(col3_x, y_start + 30,
                               text=f"Brillo: {brillo:.1f}x",
                               font=("Consolas", 8), fill="#ffffff", anchor="w", tags="info")
        
        # Número de puntos activos
        num_puntos = len([p for p in self.puntos_lissajous if p.get('intensidad', 0) > 0.1]) if valores.get("modo_sinusoidal") else len(self.puntos_pantalla)
        self.canvas.create_text(col3_x, y_start + 45,
                               text=f"Puntos: {num_puntos}",
                               font=("Consolas", 8), fill="#00ff00", anchor="w", tags="info")

    def _identificar_figura_lissajous(self, freq_v, freq_h, fase_v, fase_h):
        """Identifica el tipo de figura de Lissajous"""
        # Simplificar ratio de frecuencias
        from fractions import Fraction
        try:
            ratio = Fraction(freq_v / freq_h).limit_denominator(10)
            ratio_str = f"{ratio.numerator}:{ratio.denominator}"
        except:
            ratio_str = "1:1"
        
        # Diferencia de fase
        diff_fase = abs(fase_v - fase_h) % 360
        
        # Clasificación basada en la imagen de referencia
        if freq_v == freq_h:  # 1:1
            if diff_fase < 15 or abs(diff_fase - 180) < 15:
                return "Línea diagonal"
            elif abs(diff_fase - 90) < 15 or abs(diff_fase - 270) < 15:
                return "Círculo"
            else:
                return "Elipse"
        elif abs(freq_v - 2*freq_h) < 0.1 or abs(2*freq_v - freq_h) < 0.1:
            return "Figura 8"
        elif abs(freq_v - 3*freq_h) < 0.1 or abs(3*freq_v - freq_h) < 0.1:
            return "Trébol 3 hojas"
        else:
            return f"Lissajous {ratio_str}"

    def limpiar_pantalla(self):
        """Limpia todos los puntos de la pantalla"""
        self.puntos_pantalla.clear()
        self.puntos_lissajous.clear()
        self.canvas.delete("punto")