def leerDatos():
    print("::Divisor de numeros::")
    dividendo = float(input("Escriba el dividendo: "))
    divisor = float(input("Escriba el divisor: "))
    return dividendo,divisor
def calcularProcedimiento(dividendo,divisor):
    cociente = {dividendo // divisor}
    resto = {dividendo % divisor}
    if divisor == 0:
        print('No se puede dividir por cero')
    else:
        if dividendo % divisor == 0.0:
            print(f'La división es exacta. Cociente: {dividendo // divisor}')
        else:
            print(f'La división no es exacta. Cociente: {dividendo // divisor} Resto: {dividendo % divisor}')
    return cociente,resto
dividendo,divisor = leerDatos()
cociente,resto = calcularProcedimiento()
   
def ejercicio_1(dividendo,divisor,cociente,resto):
    dividendo,divisor = leerDatos()
    cociente,resto = calcularProcedimiento()