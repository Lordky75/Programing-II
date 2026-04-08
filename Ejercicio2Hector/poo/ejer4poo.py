import math
class Ejercicio4():
    def __init__(self):
            self.n = 0
            self.u = 0
            self.d = 0
            self.ascenso = 0
            self.tiempo = 0
    def leerValores(self):
        self.n = int(input("Profundidad del pozo(pulg)="))
        self.u = int(input("Energía(pulg/min)="))
        self.d = 1
        self.ascenso = 0
        self.tiempo = 0
        return self.n,self.u,self.d,self.ascenso,self.tiempo
    def calcularTiempo(self):
        while True:
            self.ascenso += self.u    #Desplazamiento hacia arriba
            self.tiempo += 1 #Tiempo de ascenso
            if self.ascenso >= self.n:   #Si llego a la cima sale del ciclo
                break;
            self.ascenso -= self.d    #Desplazamiento hacia abajo
            self.tiempo += 1 #Tiempo de descanso
        return self.tiempo
    def mostrarResultados(self):
        print("Tiempo en salir: ",self.tiempo)