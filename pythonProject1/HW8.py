from math import *

while True:
    try:

        def plochad_treug(osnova, visota):
            return (osnova * visota) * 0.5


        def plochad_pramoug(storona1, storona2):
            return storona1 * storona2


        def plochad_krug(radius):
            return (pi * radius) ** 2


        figura = int(input('Выберите фигуру для нахождения ее площади:\n1 - прямоугольник,'
                           ' 2 - треугольник, 3 - круг: ') or 2)
        if figura == 1:
            storona1 = float(input('Введите первую сторону: '))
            storona2 = float(input('Введите вторую сторону: '))
            print('Площадь: ', plochad_pramoug(storona1, storona2))

        elif figura == 2:
            osnova = float(input('Введите длину основания: ') or 10)
            visota = float(input('Введите высоту: ') or 16)
            print('Площадь: ', plochad_treug(osnova, visota))
        elif figura == 3:
            radius = float(input('Введите радиус окружности: '))
            print('Площадь: ', round(plochad_krug(radius), 2))
        else:
            print('Вы ввели неправильное число')
    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break
while True:
    try:
        a = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
        prostMas = []
        prostMas2 = []
        for i in a:
            h = 0

            for l in range(2, i // 2 + 1):
                if i % l == 0:
                    h = h + 1
            if h <= 0:
                if i != 1:
                    prostMas.append(i)
            else:
                prostMas2.append(i)
        print(a, '\n')
        print('Min: ', min(prostMas))
        print('Max: ', max(prostMas2))

    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break


def raschet(a):
    suma = 0
    suma2 = 0
    while a > 0:
        c = a % 10
        a = a // 10
        if c % 2 == 0:
            suma = suma + c
        else:
            suma2 = suma2 + c
    print('Сумма четных чисел: ', suma)
    print('Сумма нечетных чисел: ', suma2)

print('N = 9874023\nN = 38271\nN = 123456789\n'
      '')
raschet(9874023)
raschet(38271)
raschet(123456789)
input()
