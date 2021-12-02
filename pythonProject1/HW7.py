from math import *

# Для быстрого ввода (без ввода) можно нажимать Enter
while True:
    try:
        x3 = float(input('Введите x1: ') or 10)
        x4 = float(input('Введите x2: ') or 50)
        y3 = float(input('Введите y1: ') or 20)
        y4 = float(input('Введите y2: ') or 30)

        res = sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
        print('Расстояние между точками: ', res)

        # Я не понял , почему при одинаково поставленных решениях разные ответы?/ И по идее правильный именно 1 вариант?

        x1 = float(input('Введите x1: ') or 10)
        x2 = float(input('Введите x2: ') or 50)
        y1 = float(input('Введите y1: ') or 20)
        y2 = float(input('Введите y2: ') or 30)


        def rast(x1, x2, y1, y2):
            return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


        print('Расстояние между точками: ', round(rast(x1, x2, y1, y2), 2))
    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break
while True:
    try:
        s1 = float(input('Сторона 1: ') or 3)
        s2 = float(input('Сторона 2: ') or 4)
        ugol = float(input('Угол: ') or 90)


        def ploshad(s1, s2, ugol):
            return s1 * s2 * sin(radians(ugol))


        print('Площадь треугольника', round(ploshad(s1, s2, ugol), 2))
    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
