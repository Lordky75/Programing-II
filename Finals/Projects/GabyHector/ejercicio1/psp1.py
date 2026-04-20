import math

class calculadoraRegresion:
    def __init__(self, datos_x, datos_y, xk_val):
        self.x = datos_x
        self.y = datos_y
        self.xk = xk_val
        self.n = len(datos_x)
        self.beta0 = 0.0
        self.beta1 = 0.0
        self.r = 0.0
        self.r2 = 0.0
        self.yk = 0.0

    def calcularOperaciones(self):
        if self.n == 0:
            return

        sum_x = sum(self.x)
        sum_y = sum(self.y)
        sum_x2 = sum([xi ** 2 for xi in self.x])
        sum_y2 = sum([yi ** 2 for yi in self.y])
        sum_xy = sum([self.x[i] * self.y[i] for i in range(self.n)])

        x_avg = sum_x / self.n
        y_avg = sum_y / self.n

        denominador_b1 = sum_x2 - (self.n * (x_avg ** 2))
        if denominador_b1 != 0:
            self.beta1 = (sum_xy - (self.n * x_avg * y_avg)) / denominador_b1
        
        self.beta0 = y_avg - (self.beta1 * x_avg)

        num_r = (self.n * sum_xy) - (sum_x * sum_y)
        den_r_x = (self.n * sum_x2) - (sum_x ** 2)
        den_r_y = (self.n * sum_y2) - (sum_y ** 2)
        
        if den_r_x > 0 and den_r_y > 0:
            self.r = num_r / math.sqrt(den_r_x * den_r_y)
            
        self.r2 = self.r ** 2
        self.yk = self.beta0 + (self.beta1 * self.xk)