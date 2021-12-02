input('Вы можете просто нажимать Enter , по умолчанию я поставил значения как в домашнем задании\n ')
stroka1 = input('Введите первую строку: ') or 'Python'
stroka2 = input('Введите вторую строку: ') or 'Programming language'
stroka3 = set(stroka1) - set(stroka2)
print('Искомыми буквами являются: \n', set(stroka3))

glasnieEng = ['a', 'e', 'i', 'o', 'u', 'y']
glasnieRu = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
slovo = input('\nВведите строку: ') or 'Привет, мир!'
pust = []
puste = []
y = True
for i in slovo:
    for j in glasnieRu:
        if j == i:
            pust.append(i)
    for e in glasnieEng:
        if e == i:
            y = False
            puste.append(i)
if y is True:
    print('Количество гласных равно: ', len(pust))
else:
    print('Количество гласных равно: ', len(puste))

strokaH = input('\nВведите первую строку') or 'test'
strokaH2 = input('Введите вторую строку') or 'string'
t = set(strokaH)
t2 = set(strokaH2)
t |= t2
print('Искомыми буквами является: \n', t)

strokaHe = input('\nВведите первую строку') or 'hello'
strokaHe2 = input('Введите вторую строку') or 'world'
te = set(strokaHe) ^ set(strokaHe2)
print('Искомыми буквами является: \n', set(te))
input()

players = ['Максим', 'Матвей', 'Александр', 'Евгения', 'Михаил', 'Наталья']
mathematicWin = {'Максим', 'Матвей', 'Евгения', 'Михаил', 'Наталья'}
physicsWin = {'Максим', 'Матвей', 'Александр'}
player = set(players)
physicsWin &= mathematicWin
mathematicWin &= physicsWin
print("Все призеры: ", players)
print('Призеры обеих олимпиад: ', physicsWin)
print('Обновленый список призеров по математике: ', mathematicWin)
print('\nТесты:\n'
      'list_1 = [1, 1, 3, 3, 1]\n'
      'list_2 = [5, 5, 5, 5, 5, 5, 5]\n'
      'list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]\n')


def set_gen(listy):
    list_11 = []
    list_22 = []
    list_res = []
    umnoj = '1'
    for i in listy:
        for j in listy:
            if i not in list_11:
                list_11.append(i)
    for l in list_11:
        list_22 = []
        for k in listy:
            if l == k:
                list_22.append(k)
                umnoj = str(k) * len(list_22)
                list_res.append(umnoj)
    return list_res


print(set_gen([1, 1, 3, 3, 1]))
print(set_gen([5, 5, 5, 5, 5, 5, 5]))
print(set_gen([2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]))
input('\nC последней задачкой пришлось долго повозится, но оно того стоило :)')

# for i in list_1:
#     for j in list_1:
#         if i == j and i not in list_22:
#             list_22.append(j)
# print(list_22)
