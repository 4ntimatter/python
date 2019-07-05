import math
class parallegram :
    def __init__(self ,a ,b ,alpha):
        self.a = a
        self.b = b
        self.alpha = alpha

    def calc_hight(self):
        teta = math.radian(self.alpha)


        return self.b * math.sin(teta)


    def clc_area(self):
        self.a * teta

