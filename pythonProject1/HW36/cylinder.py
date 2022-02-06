from HW36 import rectangle
from math import pi


class Cylinder(rectangle.Rectangle):
    def __init__(self, h, r, a, b):
        self.h = h
        self.r = r
        super().__init__(a, b)

    def length_cir(self):
        return round(2 * pi * self.r, 2)

    def square_cir(self):
        return round(pi * self.r ** 2, 2)

    def volume_cyl(self):
        return round(pi * self.r ** 2 * self.h, 2)

    def len_print(self):
        print(f'Длина окружности: {self.length_cir()}')

    def sua_print(self):
        print(f'Площадь круга: {self.square_cir()}')

    def vol_print(self):
        print(f'Объём: {self.volume_cyl()}')
