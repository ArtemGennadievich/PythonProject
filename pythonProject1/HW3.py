# Калькулятор
while True:
    try:
        tip_oper = int(input('Калькулятор\nВыберите операцию: \n1 - "r" - применяет унарный минус к операнду\n2 - "+" '
                             '- сложение '
                             '\n3 - "-" - вычитание\n4 - "/" - деление\n5 - "*" - умножение\n6 - "%" - деление по '
                             'модулю '
                             '(остаток то деления)\n7 - "<" - минимальное из двух чисел\n8 - ">" - максимальное из '
                             'двух чисел '
                             '\nВведите цифру: '))
        ch1 = int(input("Введите первое число: "))
        ch2 = int(input("Введите второе число: "))
        if tip_oper == 1:
            res = ch1 = -ch1
            res2 = ch2 = -ch2
        elif tip_oper == 2:
            res = ch1 + ch2
        elif tip_oper == 3:
            res = ch1 - ch2
        elif tip_oper == 4:
            if ch2 == 0:
                res = "На ноль делить нельзя!"
            if ch2 != 0:
                res = ch1 / ch2
        elif tip_oper == 5:
            res = ch1 * ch2
        elif tip_oper == 6:
            res = ch1 % ch2
        elif tip_oper == 7:
            if ch1 < ch2:
                res = ch1
            if ch2 < ch1:
                res = ch2
        elif tip_oper == 8:
            if ch1 > ch2:
                res = ch1
            if ch2 > ch1:
                res = ch2
        else:
            print("Введите заново")
        if tip_oper == 1:
            print("Результат: ", res, res2)
        else:
            print("Результат: ", res)
    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break

while True:
    try:
        f = int(input("Программа для нахождения максимального значения из трех чисел введеных пользователем "
                      "( с использованием тернарного выражения)\nВведите первое число: "))
        g = int(input("Введите второе число: "))
        h = int(input("Введите третье число: "))
        r = [f if h < f > g else "" or g if f < g > h else "" or h if f < h > g else "Все числа одинаковые"]
        print(r)
    except (ValueError, NameError):
        print("Не введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break
while True:
    try:
        ch_sim = int(input("Программа, которая выводит на экран линию из символов.\nВведите число символов: "))
        tip_sim = input("Введите тип символов: ")
        orient_sim = int(input("Выберите ориентацию символов:\n0 - вертикальная\n1 - горизонтальная\n "))
        i = 0
        while i < ch_sim:
            if orient_sim == 1:
                print(tip_sim, end="")
            if orient_sim == 0:
                print(tip_sim)
            i += 1
    except (ValueError, NameError):
        print("Не введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break
while True:
    try:
        g = 0
        k = 0
        j = 0
        p = 0
        i = 0
        res = 0
        kol_ch = int(input("Программа, которая вычисляет среднее арифметическое последовательности дробных чисел, "
                           "вводимых с клавиатуры.\nВведите количество чисел последовательности: "))
        while i < kol_ch:
            ch = float(input("Введите число: "))
            res = ch + res
            i += 1
            h = ch
            if h > g:
                g = h
            if j > ch:
                k = ch
                if k < ch:
                    p = k
            j = ch
        print('Количество чисел', i)
        print('Среднее арифметическое: ', res / kol_ch)
        print('Минимальное число: ', k)
        print('Максимальное число: ', g)
    except (ValueError, NameError):
        print("Не введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break
print("Очень запарился и потратил много времени на последнюю задачу , но решил сам :)\nИ скажите мне, удобно ли вам"
      " ползоваться такой программой (имеется ввиду : нажмите Enter или 1, и определения ошибок) или все таки делать\n"
      "по обычному. Лично для меня в кайф ,когда программа так отображается.")
