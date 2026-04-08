from Clases.Herencia1.Personas import Persona
class Empleado(Persona):
    def __init__(self, nombres, apellidos, documento, tipo, tipoContrato, sueldo):
        super().__init__(nombres, apellidos, documento, tipo)
        self.tipoContrato = tipoContrato
        self.sueldo = sueldo
    def __str__(self):
        return super().__str__() + " " + self.tipoContrato + " " + self.sueldo
    def calcularSueldo(self):
        print("Calculando codigo...")