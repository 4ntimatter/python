class temerature:
    def __init__(self, cels):
        self.cels = cels

    @property

    def farh(self):
        self.farh = ((self.cels * 9 / 5) + 32)
        return self.farh


    @farh.setter

    def farh(self, value):
        self.cels = ((value - 32) * 5)
        return self.cels

t = temerature
t.farh(100)
print(t.farh)
