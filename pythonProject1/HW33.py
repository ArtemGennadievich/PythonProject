import math
from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):
    @abstractmethod
    def share_perimeter(self):
        pass

    @abstractmethod
    def share_square(self):
        pass

    @abstractmethod
    def draw_figure(self):
        pass

    @abstractmethod
    def print_info_pp(self):
        pass


class Square(Shape):
    def __init__(self, side, color):
        self.side = side
        self.color = color

    def share_square(self):
        return self.side ** 2

    def share_perimeter(self):
        return self.side * 4

    def print_info(self):
        print(f'Сторона: {self.side}\nЦвет: {self.color}\nПлощадь: {self.share_square()}\n'
              f'Периметр: {self.share_perimeter()}')

    def draw_figure(self):
        for i in range(self.side):
            print("* " * self.side)

    def print_info_pp(self):
        print('===Квадрат===')


class Rectangle(Shape):
    def __init__(self, side_a, side_b, color):
        self.side_a = side_a
        self.side_b = side_b
        self.color = color

    def share_square(self):
        return self.side_a * self.side_b

    def share_perimeter(self):
        return (self.side_a + self.side_b) * 2

    def print_info(self):
        print(f'Длина: {self.side_a}\nШирина: {self.side_b}\nЦвет: {self.color}\nПлощадь: {self.share_square()}\n'
              f'Периметр: {self.share_perimeter()}')

    def draw_figure(self):
        for i in range(self.side_a):
            print('*' * self.side_b)

    def print_info_pp(self):
        print('===Прямоугольник===')


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c, color):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.color = color

    def share_square(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return round(math.sqrt(p * ((p - self.side_a) * (p - self.side_b) * (p - self.side_c))), 2)

    def share_perimeter(self):
        return (self.side_a + self.side_b + self.side_c) / 2

    def print_info(self):
        print(
            f'Сторона 1: {self.side_a}\nСторона 2: {self.side_b}\nСторона 3: {self.side_c}\nЦвет: {self.color}\nПлощадь: {self.share_square()}\nПериметр: {self.share_perimeter()}')

    def print_info_pp(self):
        print('===Треугольник===')

    # def draw_figure(self):
    #     print(' ' * 5 + '*' + ' ' * 5)
    #     print(' ' * 4 + '***' + ' ' * 4)
    #     print(' ' * 3 + '*****' + ' ' * 3)
    #     print(' ' * 2 + '*******' + ' ' * 2)
    #     print(' ' * 1 + '*********' + ' ' * 1)
    #     print('***********')

    def draw_figure(self):
        count = self.side_b - 1
        count_for_z = self.side_a - (self.side_a - 1)
        for i in range(self.side_b):
            print(' ' * count + '*' * count_for_z + ' ' * count)
            count -= 1
            count_for_z += 2


squ = Square(3, 'Red')
squ.print_info_pp()
squ.share_perimeter()
squ.share_square()
squ.print_info()
squ.draw_figure()
print()
rec = Rectangle(3, 7, 'Green')
rec.print_info_pp()
rec.share_perimeter()
rec.share_square()
rec.print_info()
rec.draw_figure()
print()
tri = Triangle(11, 6, 6, 'Yellow')
tri.print_info_pp()
tri.share_perimeter()
tri.share_square()
tri.print_info()
tri.draw_figure()
