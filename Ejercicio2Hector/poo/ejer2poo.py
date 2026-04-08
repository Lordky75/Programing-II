class Ejercicio2():
    def __init__(self):
        self.password = 0
        self.intentos = 0
        self.palabra = 0
    def asignarDatos(self):
        self.password = "lunes"
        self.intentos = 0
        self.palabra = ""
        return self.password,self.intentos,self.palabra
    def mostrarMensaje(self):
        while self.palabra != self.password:
            self.palabra = input("Contraseña:")
            self.intentos += 1
            if self.intentos == 5:
                print("Excediste las oportunidades")
                break