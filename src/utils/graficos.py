# Graficado de señales y curvas de Lissajous (usando matplotlib)

#Imports
import matplotlib.pyplot as plt
from typing import Optional
from src.utils.constantes import SignalDefaults
from src.functions.señales import SignalSpec, SignalGenerator


def plot_lissajous(spec_x: SignalSpec, spec_y: SignalSpec, defaults: Optional[SignalDefaults] = None, fs: Optional[float] = None, duration: Optional[float] = None, show_time_series: bool = False) -> None:
    gen = SignalGenerator(defaults)
    t, x, y = gen.lissajous(spec_x, spec_y, fs=fs, duration=duration)

    #Figura Lissajous (x vs y)
    fig_xy = plt.figure()
    ax = fig_xy.add_subplot(1, 1, 1)
    ax.plot(x, y, linewidth=1.0)
    ax.set_xlabel("X(t)")
    ax.set_ylabel("Y(t)")
    ax.set_title("Curva de Lissajous")
    ax.grid(True)

    if show_time_series: #Series temporales X(t) y Y(t)
        #X(t)
        fig_tx = plt.figure()
        ax_tx = fig_tx.add_subplot(1, 1, 1)
        ax_tx.plot(t, x, linewidth=1.0)
        ax_tx.set_xlabel("t [s]")
        ax_tx.set_ylabel("X(t)")
        ax_tx.set_title("Señal X(t)")
        ax_tx.grid(True)

        #Y(t)
        fig_ty = plt.figure()
        ax_ty = fig_ty.add_subplot(1, 1, 1)
        ax_ty.plot(t, y, linewidth=1.0)
        ax_ty.set_xlabel("t [s]")
        ax_ty.set_ylabel("Y(t)")
        ax_ty.set_title("Señal Y(t)")
        ax_ty.grid(True)

    plt.show()