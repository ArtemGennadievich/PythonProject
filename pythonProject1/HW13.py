from math import *


def raschet(figure_type, **args):
    if figure_type == 'rhombus':
        for k, v in args.items():
            if k == 'd1':
                d1 = v
            if k == 'd2':
                d2 = v
    elif figure_type == 'square':
        for k, v in args.items():
            a = v
    elif figure_type == 'trapezoid':
        for k, v in args.items():
            if k == 'a':
                a = v
            if k == 'b':
                b = v
            if k == 'h':
                h = v
    elif figure_type == 'circle':
        for k, v in args.items():
            r = v

    else:
        return 'invalid data'

    def rhombus(d1, d2):
        s = (d1 * d2) / 2
        return s

    def square(a):
        s = a ** 2
        return s

    def trapezoid(a, b, h):
        s = 0.5 * (a + b) * h
        return s

    def circle(r):
        s = pi * r ** 2
        return s

    if figure_type == 'rhombus':
        return rhombus(d1, d2)
    if figure_type == 'square':
        return square(a)
    if figure_type == 'trapezoid':
        return trapezoid(a, b, h)
    if figure_type == 'circle':
        return circle(r)


print(raschet('rhombus', d1=10, d2=8))
print(raschet('square', a=5))
print(raschet('trapezoid', a=12, b=3, h=6))
print(raschet('circle', r=18))
print(raschet('unknow', a=1, b=2, c=3))
