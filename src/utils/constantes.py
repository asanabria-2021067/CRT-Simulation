#Constantes físicas y valores predeterminados

#Imports
from dataclasses import dataclass

#Constantes físicas fundamentales
EPSILON_0: float = 8.8541878128e-12 #Permisividad del vacío (F/m)
E_CHARGE: float = 1.602176634e-19 #Carga del electrón (C)
E_MASS: float = 9.1093837015e-31 #Masa del electrón (kg)
PI: float = 3.141592653589793 #Valor de π

#Parámetros de muestreo por defecto
FS_DEF: float = 100_000.0 #Frecuencia de muestreo (Hz)
DUR_DEF: float = 0.050 #Duración (s)

#Valores predeterminados de señales
AMP_DEF: float = 1.0 #Amplitud
FREQ_DEF: float = 1_000.0 #Frecuencia (Hz)
PHASE_DEF: float = 0.0 #Fase (rad)
OFFSET_DEF: float = 0.0 #Desplazamiento DC


@dataclass(frozen = True)
class SignalDefaults: #Valores predeterminados para generación de señales
    fs: float = FS_DEF
    duration: float = DUR_DEF 
    amplitude: float = AMP_DEF
    frequency: float = FREQ_DEF
    phase: float = PHASE_DEF
    offset: float = OFFSET_DEF