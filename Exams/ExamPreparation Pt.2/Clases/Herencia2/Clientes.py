from Clases.Herencia1.Personas import Persona
class Cliente(Persona):
    def __init__(self, nombres, apellidos, documento, tipo, categoria, codigo):
        super().__init__(nombres, apellidos, documento, tipo)
        self.categoria = categoria
        self.codigo = codigo
    def __str__(self):
        return super().__str__() + " " + self.categoria + " " + self.codigo
    def generarCodigo(self):
        print("986876")