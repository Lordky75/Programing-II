def leerDatos():
    print("::Convertidor de cm a km,m y cm::")
    distancia = int(input("Ingrese la distancia en centimetros: "))
    return distancia
def calcularProcedimiento(distancia):
        if distancia == 0:
            print("Escriba una distancia mayor que cero.")
        else:
            kilometros = distancia // 100000
            metros = (distancia % 100000) // 100
            centimetros = distancia % 100
            print(f"{distancia} centimetros son: {kilometros}km {metros}m {centimetros}")

distancia = leerDatos()
calcularProcedimiento(distancia)

def ejercicio_3(distancia):
    distancia = leerDatos()
    calcularProcedimiento(distancia)
    