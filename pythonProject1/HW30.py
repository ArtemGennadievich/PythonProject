import math
from abc import ABC, abstractmethod
import re


class Root(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def solution(self):
        pass




class Line(Root):

    def solution(self):
        lst = re.findall('[1-9]', self.value)
        a = int(lst[0])
        b = int(lst[1])

        if a == 0 and b == 0:
            print("Бесконечное количество решений.")
        if a == 0 and b != 0:
            print("Решений нет.")
        if a != 0:
            print(f"The roots of '3x+7=0' are: {round(b / (-1 * a), 2)}")


class Square(Root):

    def solution(self):
        lst = re.findall('[1-9]', self.value)
        a = int(lst[0])
        b = int(lst[2])
        c = int(lst[3])
        d = b ** 2 + 4 * a * c
        if d > 0:
            x1 = (b + math.sqrt(d)) / (2 * a)
            x2 = (b - math.sqrt(d)) / (2 * a)
            print(f"The roots of '1x^2-2x-3=0' are: {x1}, {x2}")
        elif d == 0:
            x = b / (2 * a)
            print(f"Корень = {x}")
        else:
            print("Корней нет")


solution = Line('3x+7=0')
solution.solution()
solution2 = Square('1x^2-2x-3=0')
solution2.solution()
