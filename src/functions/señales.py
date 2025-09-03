#Señales sinusoidales, compuestas y pares para curvas de Lissajous para el CRT

#Imports
from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple, Optional, Iterable
import numpy as np
from src.utils.constantes import SignalDefaults, PI
from src.utils.helpers import tvector, validate_signal_params

@dataclass(frozen = True)
class SignalSpec: #Especificación de una señal senoidal
    frequency: float
    amplitude: float
    phase: float = 0.0 #En rad
    offset: float = 0.0 #DC

class SignalGenerator: #Generados de señales sinoidales individuales, compuestas y Lissajous
    def __init__(self, defaults: Optional[SignalDefaults] = None) -> None: #Valores predeterminados
        self.defaults = defaults or SignalDefaults()

    def sine(self, freq: float, amp: float, phase: float = 0.0, offset: float = 0.0, fs: Optional[float] = None, duration: Optional[float] = None) -> Tuple[np.ndarray, np.ndarray]: #Señal senoidal: x(t) = offset + amp * sin(2π f t + phase)
        validate_signal_params(freq, amp)
        fs = self.defaults.fs if fs is None else fs
        duration = self.defaults.duration if duration is None else duration

        t = tvector(fs, duration)
        x = offset + amp * np.sin(2.0 * np.pi * freq * t + phase)
        return t, x #Vector de tiempo y señal

    def composite(self, specs: Iterable[SignalSpec], fs: Optional[float] = None, duration: Optional[float] = None, noise_std: float = 0.0) -> Tuple[np.ndarray, np.ndarray]: #Suma de varias senoidales con ruido gaussiano opcional
        fs = self.defaults.fs if fs is None else fs
        duration = self.defaults.duration if duration is None else duration
        t = tvector(fs, duration)

        x = np.zeros_like(t)
        for s in specs: #Suma de señales
            validate_signal_params(s.frequency, s.amplitude)
            x += s.offset + s.amplitude * np.sin(2.0 * np.pi * s.frequency * t + s.phase)

        if noise_std > 0.0: #Ruido gaussiano blanco
            x += np.random.normal(loc=0.0, scale=noise_std, size=t.shape)

        return t, x #Vector de tiempo y señal compuesta

    def lissajous(self, spec_x: SignalSpec, spec_y: SignalSpec, fs: Optional[float] = None, duration: Optional[float] = None) -> Tuple[np.ndarray, np.ndarray, np.ndarray]: #Señales senoidales (x(t), y(t)) para trazar curvas de Lissajous
        fs = self.defaults.fs if fs is None else fs
        duration = self.defaults.duration if duration is None else duration

        t = tvector(fs, duration)
        _, x = self.sine(spec_x.frequency, spec_x.amplitude, spec_x.phase, spec_x.offset, fs, duration)
        _, y = self.sine(spec_y.frequency, spec_y.amplitude, spec_y.phase, spec_y.offset, fs, duration)

        return t, x, y #Vector de tiempo y señales x(t), y(t)