while True:
    try:
        mas = []
        ch = int(input('Программа для вывода всех элементов списка с четными индексами\nВведите количество чисел: '))
        for i in range(ch):
            ch_2 = int(input('-> '))
            if i % 2 == 0:
                mas.append(ch_2)
        print(mas)
    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break
while True:
    try:
        g = 0
        mas2 = []
        ch_3 = int(input('Программа для вывода всех элементов , которые больше предыдущего элемента \nВведите'
                         ' количество чисел: '))
        for i in range(ch_3):
            ch_4 = int(input('-> '))
            if g == 0:
                g = ch_4
            if ch_4 > g:
                mas2.append(ch_4)
            g = ch_4
        print(mas2)
    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break
print('Программа для вывода элементов, которые встречаются в списке только один раз\n'
      'Список: [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]')
mas3 = []
res = []
b = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
for i in b:
    if i not in mas3:
        mas3.append(i)
        res.append(i)
    else:
        if i in res:
            i = res.index(i)
            del res[i]
print(res)
input()