stroka1 = 'I am Learning Python. hello, WORLD!'
correct = stroka1.rfind('h')
correct2 = stroka1.find('h')
print(stroka1[:correct2] + stroka1[correct + 1:])

in_st = stroka1.find('h')
in_st2 = stroka1.find('.')
strr = stroka1[in_st + 1:in_st2 + 2]
print(stroka1[:in_st + 1] + strr[::-1] + stroka1[in_st2 + 2:])

strr2 = '11 23 44 55 23 22'
print('Строка: ', strr2)
zamena = input('Ее заменяемая подстрока: ')
zamena2 = input('Новая подстрока: ')
poisk = strr2.replace(zamena, zamena2)
print(poisk)

strr3 = 'Ежевику для ежат' \
        'Принесли два ежа. ' \
        'Ежевику еле-еле ' \
        'Ежата возле ели съели'
ch = -1
res = 0
for i in strr3:
    ch += 1
    if ch == 0:
        res += 1
    elif i == 'е':
        indx = ch
        if strr3[indx-1] == ' ':
            res += 1
    elif i == 'Е':
        indxx = ch
        if strr3[indxx-1] == ' ':
            res += 1
print('Количество слов: ', res)
input()

