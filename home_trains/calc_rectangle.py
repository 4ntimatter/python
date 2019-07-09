import math
class rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_area(self):
        return self.a *self.b

p = rectangle(10, 5)
print(p.calc_area())