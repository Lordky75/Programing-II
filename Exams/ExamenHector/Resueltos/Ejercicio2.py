def leerDatos():
    print('::ECUACIÓN A X + B = 0::')
    a = float(input('Escriba el valor del coeficiente a: '))
    b = float(input('Escriba el valor del coeficiente b: '))
    return a,b
def calcularProcedimiento(a,b):
    if a == 0 and b == 0:
        print('Todos los números son solución')
    else:
        if a == 0:
            print('La ecuación no tiene solución')
        else:
            x = -b / a
            print(f'La ecuación tiene una solución: {x}')
a,b = leerDatos()
calcularProcedimiento(a,b)

def ejercicio_2(a,b):
    a,b = leerDatos()
    calcularProcedimiento(a,b)