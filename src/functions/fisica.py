import math
""" ---------------------------Etapa antes de entrar a placas deflectoras

vf mediante conservación de energía v = (2eV/M)^1/2 se usará para determinar la intensidad del brillo
    e carga del electrónn
    V voltaje proporcionado por el usuario
    M masa del electrón """
def velocidadCE(q, V, M):
    vel = pow(((2*q*V)/M),0.5)
    return vel

""" --------------------------Etapa dentro de las placas deflectoras y fuera de ellas hasta el impacto con la pantalla
Tiempo dentro de las placas | Tiempo despues de las placas hasta la pantalla
    t = d/v
    t tiempo requerido
    d distancia recorrida
    v velocidad de entrada """
def tiempo(d, v):
    tiempo = d/v
    return tiempo
""" 
Velocidad final al salir de las placas, usado para determinar con qué vel se inicia la fase entre el final de las placas y la pantalla
    v = at
    v velocidad
    a aceleración
    t tiempo """
def velFinal(aceleracion, tiempo):
    vel = aceleracion*tiempo
    return vel
    
""" 
 Aceleración de la particula a = qV/Md || a = 2qV/Md
    q carga electrónn
    V voltaje ajustado por el usuario
    M masa del electrón
    d distancia de la placa al electron """
def aceleracion(q, V, M, d, ejeZ):
    if (ejeZ == True ): #En el caso de que se quiera saber la aceleración de impulso
        acel = (q*V)/(M*d)
    else: #Aceleración para calcular desvios en eje x,y
        acel = (2*q*V)/(M*d)
    return acel
""" 
 Posición final de una particula dentro de las placas
     x = (1/2 * a * t1^2) + (velI * t2)
     Se asume que la velocidad inicial es 0 m/s
     Se usa solo en ejes x,y
     x = 1/2 * a * t^2
     a aceleración
     tPlaca tiempo que pasó dentro de la placa
     velI velocidad inicial de la segunda etapa (Despues de salir de la tapa -> velocidad constante)
     tVuelo tiempo que pasó desde que salió de las placas hasta la pantalla """
def posicionFinal(a, tPlacas, velI, tVuelo):
    posc1 = 0.5*a*pow(tPlacas, 2)
    posc2 = velI*tVuelo
    posc = posc1+posc2
    return posc

""" ----------------------------Caso sinusoidal
 V = Vo sen(2pi * w*t + k)
     Vo Amplitud máxima del voltaje
     w frecuencia angular
     t tiempo
     k angulo de fase """
def voltajeSinusoidal(amplitud, frecuencia, fase, tiempo):
    voltaje = amplitud * math.sin(2*math.pi * frecuencia * tiempo + fase)
    return voltaje


"""
    Calcula la posición y velocidad lateral del electrón en un paso de tiempo dt
    bajo un voltaje sinusoidal.
    
    q: carga del electrón
    m: masa del electrón
    d: separación entre placas
    amplitud: voltaje máximo (Elegida por usuario)
    f: frecuencia (Hz) (Elegida por el usuario)
    fase: fase inicial (rad y elegida por el usuario)
    t: tiempo actual
    dt: paso de tiempo
    v: velocidad lateral actual
    pos: posición lateral actual
    """
def poscSinusoidal(q,m,d,a,f,fase,t,dt):
    V = voltajeSinusoidal(a, f, fase, t)
    a = aceleracion(q, V, m, d, False)
    v = v + a * dt
    pos = pos + v * dt
    t = t + dt
    return v, pos, t