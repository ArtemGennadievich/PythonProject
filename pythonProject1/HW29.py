import math


class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def change_val_a(self, a):
        self.a = a

    def change_val_b(self, b):
        self.b = b

    def summa_val(self):
        return f'Сумма: {self.a + self.b}'

    def multiplication_val(self):
        return f'Произведение: {self.a * self.b}'


class RightTriangle(Pair):
    def __init__(self, a, b, hyp=0):
        super().__init__(a, b)
        self.hyp = hyp

    def find_hypotenuse(self):
        self.hyp = round(math.sqrt(self.a ** 2 + self.b ** 2), 2)
        return f'Гипотенуза АВС: {round(math.sqrt(self.a ** 2 + self.b ** 2), 2)}'

    def find_square(self):
        return f"Площадь АВС: {0.5 * (self.a * self.b)}"

    def print_info(self):
        return f'Прямоугольный треугольник АВС {self.a, self.b, self.hyp}'


pair = RightTriangle(5, 8)
print(pair.find_hypotenuse())
print(pair.print_info())
print(pair.find_square())
print(pair.summa_val())
print(pair.multiplication_val())
pair.change_val_a(10)
print(pair.find_hypotenuse())
pair.change_val_b(20)
print(pair.find_hypotenuse())
print(pair.summa_val())
print(pair.multiplication_val())
print(pair.find_square())
