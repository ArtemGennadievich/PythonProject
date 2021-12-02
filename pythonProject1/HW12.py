spisok1 = ['red', 'green', 'blue']
spisok2 = ['FF0000', '#008000', '#0000FF']
slovar_spiska = dict(zip(spisok1, spisok2))
print(slovar_spiska, '\n')

slovar = {i: i ** 3 for i in range(1, 11)}
print(slovar, '\n')

lst1 = ['color', 'fruit', 'pet']
lst2 = ['blue', 'apple', 'dog']
slov = {i: j for (i, j) in zip(lst1, lst2)}
print(slov, '\n')


def min_item(*args):
    accept_items = []
    for i in args:
        accept_items.append(i)
    return min(accept_items)


print(min_item(10, 9))
print(min_item(2, 3, 4))
print(min_item(3, 5, 10, 6), '\n')


def summa(*args):
    res_lst = []
    res = 0
    for i in args:
        res += i
        res_lst.append(res)
    return res_lst


print(summa(3, 9, 1))
print(summa(2, 5, 4, 2))
print(summa(3, 5, 10, 6, 3))
input()
