# Aceleración de la particula a = qV/Md
    #q carga electrónn
    #V voltaje ajustado por el usuario
    #M masa del electrón
    #d distancia de la placa al electron
def aceleracion(carga, voltaje, masa, distancia):
    acel = (2*carga*voltaje)/(masa*distancia)
    return acel

# Posición final de una particula, puede usarse en los 3 ejes
# Se asume que la velocidad inicial es 0 m/s
def posicion(aceleracion, tiempo):
    posc = 0.5*aceleracion*tiempo*tiempo
    return posc

