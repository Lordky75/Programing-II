import math
def leerPalabra():
    while True:
        palabra = input("Palabra: ")
        if palabra == "salir":
            break
        else:
            print(palabra)
    
#Llamadas a las funciones
def ejercicio_3():
    leerPalabra()