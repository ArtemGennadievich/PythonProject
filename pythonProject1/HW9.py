def gf(a):
    maxim = []
    h = False
    for i in a:
        if i % 13 == 0 and i > 0:
            maxim.append(i)
            if a[:-1] or a[0:]:
                h = True
    if h is False:
        return 'no such nums'
    else:
        return max(maxim)


print('Тестовые значения:\n2, 7, 0, 3, 1, 5, -13\n2, 7, 0, 3, 1, 5, -13, 13\n26\n99, 99, 100, 34, -39\n'
      '99, 39, 99, 100, 34\n')
print(gf([2, 7, 0, 3, 1, 5, -13]))
print(gf([2, 7, 0, 3, 1, 5, -13, 13]))
print(gf([26]))
print(gf([99, 99, 100, 34, -39]))
print(gf([99, 39, 99, 100, 34]))

print("\nИсходный кортеж: ('ab', 'abcd', 'cde', 'abc', 'def')")
g = ('ab', 'abcd', 'cde', 'abc', 'def')
print("s = 'ab'")
s = 'ab'
if s in g:
    print('Yes')
else:
    print('No')

vvod = input('\nВведите по порядку, без пробелов, элементы кортежа: \n')
h = tuple(vvod)
print(h)
tre = []
for i in h:
    rse = []
    if i not in tre:
        tre.append(i)
        for j in h:
            if j == i and j in tre:
                rse.append(j)
        print('Количество ', i, ' = ', len(rse))
input()