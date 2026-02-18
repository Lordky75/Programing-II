from Resueltos.Ejercicio1 import ejercicio_1
from Resueltos.Ejercicio2 import ejercicio_2
from Ejercicios.Ejercicio3 import ejercicio_3

def menuPrincipal():
    while True:
        print("::Menu::")
        print("a. Ejercicio 1")
        print("b. Ejercicio 2")
        print("c. Ejercicio 3")
        print("d. Salir")
        op = int("Ingrese la opcion deseada: ")
        match(op):
            case 1:
                ejercicio_1()
            case 2:
                ejercicio_2()
            case 3:
                ejercicio_3()
            case 4:
                print("Ha salido exitosamente")
                break