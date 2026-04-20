import math

class integracionSimpson:
    def __init__(self, x, dof):
        self.x = float(x)
        self.dof = float(dof)
        self.E = 0.00001
        self.p = 0.0

    def funcionT(self, xi):
        parte1 = math.gamma((self.dof + 1) / 2)
        parte2 = math.sqrt(self.dof * math.pi) * math.gamma(self.dof / 2)
        parte3 = (1 + (xi**2) / self.dof) ** (- (self.dof + 1) / 2)
        return (parte1 / parte2) * parte3

    def calcularIntegral(self, num_seg):
        w = self.x / num_seg
        suma = 0.0
        for i in range(num_seg + 1):
            xi = i * w
            termino = self.funcionT(xi)
            if i == 0 or i == num_seg:
                multiplicador = 1
            elif i % 2 == 0:
                multiplicador = 2
            else:
                multiplicador = 4
            suma += (w / 3) * multiplicador * termino
        return suma

    def calcularOperaciones(self):
        if self.x == 0:
            self.p = 0.0
            return
        num_seg = 10
        integral_actual = self.calcularIntegral(num_seg)
        while True:
            num_seg *= 2
            integral_nueva = self.calcularIntegral(num_seg)
            if abs(integral_actual - integral_nueva) < self.E:
                self.p = integral_nueva
                break
            integral_actual = integral_nueva