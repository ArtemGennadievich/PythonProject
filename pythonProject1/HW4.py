while True:
    try:
        ch1 = int(input('Пользователь вводит с клавиатуры два числа. Нужно показать все нечетные числа в указанном диапозоне.\n'
                        'Начало диапозона: '))
        ch2 = int(input('Конец диапозона: '))
        i = 0
        for i in range(ch1, ch2 + 1):
            if i % 2 == 0:
                ''
            else:
                g = i
                print(g, end=' ')
    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break
while True:
    try:
        a = 8
        for i in range(8):
            for j in range(a):
                if i == 0:
                    a = 7
                    print('*', end="")
                if i == 1:
                    a = 6
                    print('*', end="")
                if i == 2:
                    a = 5
                    print('*', end="")
                if i == 3:
                    a = 4
                    print('*', end="")
                if i == 4:
                    a = 3
                    print('*', end="")
                if i == 5:
                    a = 2
                    print('*', end="")
                if i == 6:
                    a = 1
                    print('*', end="")
                if i == 7:
                    a = 0
                    print('*', end="")
            print()
        print('Треугольники из звездочек')
        a = 1
        for i in range(8):
            for j in range(a):
                if i == 0:
                    a = 2
                    print('*', end="")
                if i == 1:
                    a = 3
                    print('*', end="")
                if i == 2:
                    a = 4
                    print('*', end="")
                if i == 3:
                    a = 5
                    print('*', end="")
                if i == 4:
                    a = 6
                    print('*', end="")
                if i == 5:
                    a = 7
                    print('*', end="")
                if i == 6:
                    a = 8
                    print('*', end="")
                if i == 7:
                    print('*', end="")
            print()

    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break
while True:
    try:
        num = int(input("Программа для определения палиндрома\nВведите число:"))
        temp = num
        rev = 0
        while num > 0:
            dig = num % 10
            rev = rev * 10 + dig
            num = num // 10
        if temp == rev:
            print("Палиндром")
        else:
            print("Не палиндром")
    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break

