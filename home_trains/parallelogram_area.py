import math
class parallelogram :
    def __init__(self, a, b, alpha):
        self.a = a
        self.b = b
        self.alpha = alpha

    def calc_hight(self):
        teta = math.radians(self.alpha)
        return math.sin(teta) * self.b


    def calc_area(self):
        return self.a *self.calc_hight()

p = parallelogram(10, 5, 30)
print(p.calc_area())