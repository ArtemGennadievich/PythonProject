from math import *


def uravnenieA(a, b, c):
    d = b ** 2 - 4 * a * c
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    return [x2, x1]


print(uravnenieA(2, 3, -5))
