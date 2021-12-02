import random as ran
while True:
    try:
        a = []
        ch = int(input('Программа для нахождения числа в списке\nВведите количество элементов списка: '))
        for i in range(ch):
            b = int(input('->'))
            a.append(b)
        h = int(input('Введите число: '))
        print(h)
        print(a)
        for i in a:
            if i == h:
                j = "Число в списке есть"
        print(j)
    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break
while True:
    try:
        suma = 0
        y = []
        for i in range(20):
            y.append(ran.randint(0, 50))
        for i in y:
            suma += i
        print('\nПрограмма для нахождения суммы из 20 рандомных чисел\nСписок: ', y)
        print('Сумма: ', suma)

        mas = []
        for i in range(10):
            mas.append(ran.randint(0, 20))
        print('\nПрограмма для перемещения 10 рандомных чисел в начало списка, начиная с максимального'
              '\nСписок до сортировки: ', mas)
        mas.sort(reverse=True)
        print('Список после сортировки: ', mas)
    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break

