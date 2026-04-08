from Exercises.Ejercicio1 import ejercicio_1
from Exercises.Ejercicio2 import ejercicio_2
from Exercises.Ejercicio3 import ejercicio_3
from Exercises.Ejercicio4 import ejercicio_4

from poo.ejer1poo import Ejercicio1 
def menuPrincipal():
    while True:
        print("\n :: Menu ::")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Salir")
        
        op = int(input("Ingrese la opcion deseada: "))
        match(op):
            case 1:
                #Llamada a la funcion
                #Ejercicio_1()
                
                #Crear el objeto de la clase
                e1 = Ejercicio1()
                e1.leerDatos()
                e1.calcularAprox()
                e1.mostrarResultados()
                
                ejercicio_1()
            case 2:
                ejercicio_2()
            case 3:
                ejercicio_3()
            case 4:
                ejercicio_4()
            case 5:
                print("Hasta pronto")
                break
            case _:
                print("Ingrese un dato valido")