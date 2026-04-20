class Persona(object):
    def __init__(self, nombre, apellidos, documento, tipo):
        self.nombres = nombre
        self.apellidos = apellidos
        self.documento = documento
        self.tipo = tipo
    def __str__(self):
        return self.apellidos + " " + self.nombres + " " + self.documento + " " + self.tipo