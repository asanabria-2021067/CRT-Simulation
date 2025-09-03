#Funciones matemáticas de apoyo para señales y cálculos auxiliares

#Imports
import math
import numpy as np
from typing import Tuple
from .constantes import PI


def deg2rad(deg: float) -> float: #Grados a radianes
    return deg * (PI / 180.0)


def rad2deg(rad: float) -> float: #Radianes a grados
    return rad * (180.0 / PI)


def clamp(x: float, lo: float, hi: float) -> float: #Restricción de un valor a un rango
    return max(lo, min(hi, x))


def tvector(fs: float, duration: float, endpoint: bool = False) -> np.ndarray: #Vector de tiempo uniformemente muestreado
    if fs <= 0: 
        raise ValueError("fs debe ser > 0.") #Frecuencia de muestreo positiva
    if duration <= 0:
        raise ValueError("duration debe ser > 0.") #Duración positiva

    n = int(round(fs * duration))
    n = max(n, 1)
    return np.linspace(0.0, duration, n + (1 if endpoint else 0), endpoint=endpoint, dtype=float) #Vector de tiempo


def validate_signal_params(freq: float, amp: float) -> None: #Valida parámetros de señal
    if freq < 0: 
        raise ValueError("La frecuencia no puede ser negativa.") #Frecuencia no negativa
    if not math.isfinite(amp): #Amplitud finita
        raise ValueError("La amplitud debe ser un número finito.") #Amplitud finita


def rms(x: np.ndarray) -> float: #Valor RMS de una señal discreta
    if x.size == 0: #Señal vacía
        return 0.0 
    return float(np.sqrt(np.mean(np.square(x)))) #RMS


def phasor(amp: float, phase: float) -> complex: #Fasor a partir de amplitud y fase
    return amp * complex(math.cos(phase), math.sin(phase)) #A + jB = A∠φ = A(cosφ + j sinφ)