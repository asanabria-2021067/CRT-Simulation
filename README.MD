# Simulación de Tubo de Rayos Catódicos (CRT)

## 📋 Descripción

Este proyecto es una simulación educativa del funcionamiento de un Tubo de Rayos Catódicos (CRT), desarrollado como parte del Laboratorio de Física 3 de la Universidad del Valle de Guatemala. La simulación permite visualizar el comportamiento de electrones dentro del tubo y generar patrones conocidos como Figuras de Lissajous.

## 🎯 Objetivos

- Entender a profundidad el funcionamiento de un tubo de rayos catódicos controlado por placas
- Elaborar una simulación que muestre el movimiento de electrones dentro de un CRT con fines didácticos
- Generar Figuras de Lissajous mediante señales sinusoidales controlables por el usuario

## ✨ Características

### Visualización
- **Vista lateral**: Muestra la deflexión vertical del haz de electrones
- **Vista superior**: Muestra la deflexión horizontal del haz de electrones
- **Pantalla frontal**: Visualiza el punto de impacto de los electrones

### Controles del Usuario
- **Voltaje de aceleración**: Controla la velocidad y brillo del haz de electrones
- **Voltaje de placas verticales**: Controla la posición vertical del haz
- **Voltaje de placas horizontales**: Controla la posición horizontal del haz
- **Tiempo de persistencia**: Ajusta la duración de la imagen en pantalla
- **Modo sinusoidal**: Permite aplicar señales sinusoidales para generar Figuras de Lissajous
- **Controles de frecuencia y fase**: Para personalizar las señales sinusoidales

## 🔧 Instalación

```bash
# Clona el repositorio
git clone https://github.com/tu-usuario/simulacion-crt.git

# Navega al directorio del proyecto
cd simulacion-crt

# Instala las dependencias (si aplica)
# npm install
# pip install -r requirements.txt
```

## 🚀 Uso

1. Ejecuta la simulación:
   ```bash
   # Ejemplo para Python
   python main.py
   
   # Ejemplo para web
   # npm start
   ```

2. **Controles básicos**:
   - Ajusta los voltajes usando los controles deslizantes
   - Cambia entre modo manual y modo sinusoidal
   - Modifica el tiempo de persistencia para mejor visualización

3. **Generación de Figuras de Lissajous**:
   - Activa el modo sinusoidal
   - Ajusta las frecuencias y fases de las señales
   - Observa los patrones resultantes en la pantalla

## 📐 Parámetros Físicos

### Fijos (No controlables)
- Tamaño de pantalla: Cuadrada, orden de decenas de centímetros
- Área de placas de deflexión: Campo eléctrico uniforme
- Distancia entre placas: Optimizada para el movimiento libre de electrones
- Distancias internas: Calculadas para impacto preciso en pantalla

### Variables (Controlables)
- Voltaje de aceleración: Rango preestablecido
- Voltajes de deflexión: -VM < V < VM
- Parámetros de señales sinusoidales
- Tiempo de persistencia de imagen

## 📊 Figuras de Lissajous

La simulación genera diferentes patrones según la relación de frecuencias:
- **1:1** - Círculos y elipses
- **1:2** - Figura en forma de 8
- **2:3** - Patrones más complejos
- Variaciones según la fase entre señales

## 🛠️ Tecnologías Utilizadas

- [Especifica el lenguaje/framework usado]
- [Bibliotecas gráficas utilizadas]
- [Herramientas de cálculo físico]

## 📁 Estructura del Proyecto

```
simulacion-crt/
├── src/
│   ├── main.[ext]           # Archivo principal
│   ├── physics/             # Cálculos físicos
│   ├── graphics/            # Visualización
│   └── controls/            # Interfaz de usuario
├── docs/
│   ├── informe.pdf          # Informe completo
│   └── presentation.mp4     # Video presentación
├── assets/                  # Recursos gráficos
├── README.md
└── requirements.[txt/json]  # Dependencias
```

## 📖 Fundamentos Teóricos

El CRT funciona mediante:
1. **Cañón de electrones**: Acelera electrones mediante voltaje
2. **Placas de deflexión**: Controlan la trayectoria del haz
3. **Pantalla fluorescente**: Convierte impactos en luz visible

### Ecuaciones clave:
- Aceleración de electrones: `v = √(2eV/m)`
- Deflexión en placas: `y = (eVd)/(2mv₀²)L`
- Figuras de Lissajous: `x = A₁sin(ω₁t + φ₁)`, `y = A₂sin(ω₂t + φ₂)`

## 🎥 Recursos Adicionales

- [Funcionamiento general de un CRT](https://youtu.be/h6_KQeBUoS8)
- [Aplicación del CRT en calculadoras](https://youtu.be/2BIx2x-Q2fE)

## 👨‍🎓 Autor

**[Tu Nombre]**
- Universidad del Valle de Guatemala
- Laboratorio de Física 3
- Instructor: Ing. Luis Guillermo Mijangos Fuentes

## 📅 Fecha

Agosto 2025

## 📚 Referencias

Young, H., & Freedman, R. (2013). *Sears Zemansky's Física Universitaria* (Vol. 2). Pearson.

## 📄 Licencia

Este proyecto es con fines educativos para la Universidad del Valle de Guatemala.

---

> **Nota**: Este proyecto combina conocimientos de Física 3 con habilidades de programación para crear una herramienta educativa sobre el funcionamiento de tubos de rayos catódicos.