class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return f'Площадь: {self.a * self.b}'

    def perimeter(self):
        return (2 * self.a) + (2 * self.b)

    def print_per(self):
        print(f'Периметр: {self.perimeter()}')
