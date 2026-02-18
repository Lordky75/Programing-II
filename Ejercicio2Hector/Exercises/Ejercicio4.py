import math
def leerValores():
    n = int(input("Profundidad del pozo(pulg)="))
    u = int(input("Energía(pulg/min)="))
    d = 1
    ascenso = 0
    tiempo = 0
    return n,u,d,ascenso,tiempo
def calcularTiempo(n,u,d,ascenso,tiempo):
    while True:
        ascenso += u    #Desplazamiento hacia arriba
        tiempo += 1 #Tiempo de ascenso
        if ascenso >= n:   #Si llego a la cima sale del ciclo
            break;
        ascenso -= d    #Desplazamiento hacia abajo
        tiempo += 1 #Tiempo de descanso
    return tiempo
def mostrarResultados(tiempo):
    print("Tiempo en salir: ",tiempo)

#Llamadas a las funciones
def ejercicio_4():
    n,u,d,ascenso,tiempo = leerValores()
    tiempo = calcularTiempo(n,u,d,ascenso,tiempo)
    mostrarResultados(tiempo)