# import random
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# for i in my_list:
#     print(i**2, end="")
# for i in range(len(my_list)):
#     my_list[i] += 5
#     print(my_list)

# suma = 0
# a = int(input("Vvedite chislo"))
# for j in range(a):
#     b = int(input("->"))
#     if b < 0:
#         suma += b
# print("Summa: ", suma)
# n = list(range(21, 41))
# print("Список: ", n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Количество: ", k)
# print("Сумма: ", s)

# suma = 0
# a = int(input("Vvedite chislo"))
# for j in range(a):
#     b = int(input("->"))
#     if b != 0:
#         suma += b
#     else:
#         r = a - 1
#
# print("Среденее арифметическое: ", suma / r)
# print(suma)

# Срезы - получение какой-то части списка в свою очередь
# тоже является списком
# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4:-1])

# g = [1, 2, 3, 4, 5, 6, 7]
# print(g[:])
# print(g[::-1])
# print(g[::2])
# print(g[0:1])
# print(g[3:4])
# print(g[6:7])
# print(g[-3:-6:-1])
# g[1:3] = [0, 0, 0, 0]
# g[1:2] = [20]
# g[8] = 20
# print(type(g[8]))
# print(g)


# s.append(99)
# append - добавляет элементв конец списка
# print(s)
# s1 = []

# s1.extend([1, 2, 3])  # добавляет множество элементов
# print(s1)
# s1.extend('add')
# print(s1)
# s2 = []
# s2.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# input(s2)

# s.insert(1,100) # Добавляет элемент в список в заданную позицию
# и с указаными значениями
# print(s)
# s1 = []
# n = int(input('n = '))
# for i in range(n):
#     x = int(input('->'))
#     s1.extend(x)
# print(s1)

# s1 = []
# n = int(input('n = '))
# for i in range(n):
#     x = int(input('->Введите число кратное 3: '))
#     if x % 3 == 0:
#         s1.append(x)
#     else:
#         print('Число', x, 'не делится на 3 без остатка')
# print(s1)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c)
# s = [0, 2, 3, 4, 5, 6, 7]
# print(s)
# s[7:] = []
# print(s)
# s.remove(0)  # удаляем элемент из списка с заданным значением, если элементов несколько, то удалится самый первый
# print(s)
#
# s[3:5] = []
# print(s)
#
# last = s.pop() # возвращает элемент на указаные позиции, удаляя его из списка
# print(last)
# print(s)
# second = s.pop(-2)
# print(second)
# print(s)
#
# s.clear() # удаляет из списка все значения
# print(s)
#
# del s[:]
# print(s)


# ??????????????

# s1 = []
# n = int(input('n = '))
# for i in range(n):
#     x = int(input('->Введите число: '))
#     s1.append(x)
#
# k = int(input('index: '))
# s1.pop(k)
# print(s1)
# s = []
# s.extend([3, 1, 3, 20, 3, 4, 3, 50, 3])
# print(s)
# num = s.count(3)  # считает количество "3" в списке
# print(num)
# ind = s.index(20)  # возвращает положение первогго индекса
# print(ind)
# ind2 = s.index(3, 3, -1)
# print(ind2)
# s_copy = s.copy()  # возвращает копию списка
# print(s)
# print(s_copy)
#
# a = [1, 2, 3]
# b = a
# print('a =', a)
# print('b =', b)
# a.append(20)
# print('a =', a)
# print('b =', b)
#
# s.append(120)
# print(s)
# print(s_copy)
#
# s.reverse() # перестраивает элементы списка вобратном порядке
# print(s)

# s.sort() # сортирует список
# print(s)

# s.sort(reverse=True) # сортирует список в порядке убывания
# print(s)

# sorted_s = sorted(s)
# print(sorted_s)
# print(s)

# sorted_s = sorted(s, reverse=True)
# print(sorted_s)
# # print(s)

# s2 = ['Vitaliy', 'Sergey', 'Aleksandr', 'Anna']
# s2.sort(key=len)
# print(s2)

# s1 = []
# n = int(input('n = '))
# for i in range(n):
#     x = int(input('->Введите число: '))
#     s1.append(x)
#
# k = int(input('index: '))
# s1.pop(k)
# s1.sort(reverse=True)
# print(s1)

# from random import random, randint, randrange
#
# print(random())
# print(randint(3, 9))
# print(randrange(2, 6, 2))

# import random as r
#
# print(r.randint(0, 5))
# print(r.randint(0, 5))
#
# city = ['London', 'Moscow', 'SPT', 'Sochi', 'fff', 'dsdf']
# f = [55, 66, 77, 88, 99, 111, 222, 22]
# print(r.sample(f, 5))
# print(r.choices(f, k=5))
# r.shuffle(f)
# print(f)
# print(r.uniform(10.5, 25.5))
#
# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)
import copy
import locale
import random as r

# lst = [5, 3, 2, 4, 1]
# rtd = []
# print("Длина списка: ", len(lst))
# print("Минимальное значение: ", min(lst))
# print("Максимальное значение: ", max(lst))
# print("Сумма: ", sum(lst))
# for i in range(10):
#     rtd.append(r.randint(1, 100))
#     print(rtd)
# max_1 = max(rtd)
# print(max_1)
# rtd.remove(max_1)
# rtd.insert(0, max_1)
# print(rtd)

# rtd = []
# for i in range(10):
#     rtd.append(r.randint(-20, 20))
#     print(rtd)
# rtd.sort(reverse=True)
# print(rtd)

# rtd = []
# for i in range(10):
#     rtd.append(r.randint(0, 100))
#     print(rtd)
# print(rtd)
# min_l = min(rtd)
# print('min')
# indexd = rtd.index(min_l)
# print(indexd)
# # del rtd[0:indexd]
# # print(rtd)
#
# print(rtd[indexd:])

# in - оператор принадлежности
# not in - противополжно оператор принадлежности
# a = list('1aq32gas34')
# print(a)
# print('q' in a)
# lst = ['12341dfs']
# rts = []
# if not rts:
#     print('True/Cписок пустой')
# if '' not in
# rtd = []
# rtd2 = []
# rtd3 = []
# rtd4 = []
# a = int(input('Razmer 1 spiska: '))
# b = int(input('Razmer 2 spiska: '))
# for i in range(a):
#     rtd.append(r.randint(1, 10))
# print(rtd)
# for i in range(b):
#     rtd2.append(r.randint(1, 10))
# print(rtd2)
# rtd3 = rtd + rtd2
# print(rtd3)
# rtd3 = []
# for i in range(len(rtd)):
#     if rtd[i] not in rtd3:
#         rtd3.append(rtd[i])
# for i in range(len(rtd2)):
#     if rtd2[i] not in rtd3:
#         rtd3.append(rtd2[i])
# print(rtd3)
#
# rtd3 = []
# for i in rtd:
#     repeat = False
#     for j in rtd2:
#         if i == j:
#             repeat = True
#     if not repeat:
#         rtd3.append(i)
# for i in rtd2:
#     repeat = False
#     for j in rtd:
#         if i == j:
#             repeat = True
#     if not repeat:
#         rtd3.append(i)
# print(rtd3)
# rtd3 = []
# for i in range(len(rtd)):
#     if rtd[i] in rtd2 and rtd[i] not in rtd3:
#         rtd3.append(rtd[i])
# print(rtd3)
# rtd3 = []
# rtd3 = [min(rtd), min(rtd2), max(rtd), max(rtd2)]
# print(rtd3)

# user1 = ['Igor', 'Vladimir', 'Anna']
# # user2 = user1
# # user1.append('Viktoria')
# # print(user1)
# # print(user2)
# # # is - возвращает True если оба операдна указывают на один и тот же объект
# # # is not возвращает True если оба операдна указывают на разные объекты
# # print(user1 is user2)
# user2 = copy.deepcopy(user1)
# user2.append('Vika')
# print(user1)
# print(user2)

# m = [
#     [1, 2, 3, 4],  # строка 0
#     [5, 6, 7, 8],  # строка 1
#     [9, 10, 11, 12]  # строка 2
# ]
#
# # m[row][col]
# print(m[1][2])
# print(len(m))
#
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()
# print()
# for row in m:
#     for i in row:
#         print(i**2, end='\t')
#     print()
# square = [[i**2 for i in row] for row in m]
# for row in square:
#     for i in row:
#         print(i, end='\t')
#     print()
# print(square)

# w, h = 5, 3
# m = [[0 for x in range(w)] for y in range(h)]
# for row in m:
#     for i in row:
#         print(i, end='\t')
#     print()
# print(m)

# m = [[x for x in range(y, y + 12)] for y in range(10)]
# for row in m:
#     for i in row:
#         print(i, end='\t')
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y, '=', x + y)
#
# m = [
#     [2, 5, 3],
#     [9, 8, 7],
#     [9, 9, 9],
#     [1, 1, 1],
#     [3, 4, 5]
# ]
# for row in m:
#     for i in row:
#         print(i, end='\t')
#     print()
# print('\n')
# for i in range(len(m)):
#     if i % 2 == 0:
#         m[i].sort()
#     else:
#         m[i].sort(reverse=True)
#
#
# for row in m:
#     for i in row:
#         print(i, end='\t')
#     print()
# import random as g
# # w, h = 5, 4
# # m = [[g.randint(1, 30) for x in range(w)] for y in range(h)]
# # for row in m:
# #     for i in row:
# #         print(i, end='\t')
# #     print()
# j = 0
# w, h = 3, 4
# m = [[g.randint(-20, 10) for x in range(w)] for y in range(h)]
# for row in m:
#     for i in row:
#         print(i, end='\t')
#         if i < 0:
#             j += 1
#     print()
# print(j)
from math import *

# radius = 9
# print(pi * (radius ** 2))
# print(int(2 * pi * radius))
# enum = sqrt(2)
# print(enum)
# num2 = ceil(3.5)
# print(num2)
# num3 = floor(3.5)
# print(num3)
# num = -5.24
# print('Модуль числа: ', fabs(num))
# a = 8
# b = 6
# print('Наибольший общий делитель: ', gcd(a, b))
# mass = [3, 3, 3]
# mass2 = [3, 3, 3]
# print('Summa elementov spiska: ', fsum(mass))
# print('Summa elementov spiska: ', sum(mass2))
# print(0.3 + 0.3 + 0.3)
# # decimal
#
# print(degrees(3.123443))
# print(radians(180))
# print(cos(radians(60)))
# print(sin(radians(90)))
# print(tan(radians(0)))
# print(sqrt((a ** 2) + (b ** 2)))

# a1 = int(input('Figura: '))
# a = float(input('Storona a: '))
# b = float(input('Storona b: '))
# c = float(input('Storona c: '))
# if a1 == 1:
#     a_t = float(input('Storona trugolnika: '))
#     b_t = float(input('Visota trugolnika: '))
#     t = (a_t * b_t) / 2
#     print(t)
# if a1 == 2:
#     a_p = float(input('Shirina: '))
#     b_p = float(input('Dlina: '))
#     p = (a_p * b_p) / 2
#     print(p)
# if a1 == 3:
#     a_r = float(input('Radius: '))
#     r = pi * (a_r ** 2)
#     print(r)
# from time import *
# from locale import *
#
# setlocale(locale.LC_ALL, 'ru')


# sec = time()
# print('Sekudi s nachala epoxi', sec)
# local_time = ctime(sec)
# print('Mestnoe vremya: ', local_time)
# res = localtime(sec)
# print('Localnoe vremy', res)
# print(res[0:3])
# print('god', res.tm_year)
# print('mesyas', res.tm_mon)
# print('den mesaysa', res.tm_mday)
# print('Chasi', res.tm_hour)  # c 0 do 23
# print('minuti', res.tm_min)  # c 0 do 59
# print('secundi', res.tm_sec)  # c 0 do 61
# print('ded nedeli', res.tm_wday)  # c 0 do 6
# print('ded goda', res.tm_yday)  # c 1 do 365
# print('Uchet perexoda na letnee vremia', res.tm_isdst)  # 0 or 1 or -1
# print(strftime('Today is %B %d %Y', localtime(323543)))
# print(strftime('%m/%d/Y, %I:%M:%S'))
#
# pause = 5
# print('Program started... ')
# sleep(pause)
# print(str(pause) + 'seconds.')

# a = input('Nazvanie napominaniya: ')
# b = float(input('Cherez skolko midut napomnit: '))
# b = b * 60
# sleep(b)
# print(a)

# start = monotonic()
# sleep(1)
# finish = monotonic()
# res = finish - start
# print('Program time: ' + str(res) + ' seconds.')

# print(strftime('Сегодня: %B %d, %Y'))
# sec = time()
# local = ctime(sec)
# print('Местное время: ', local)


# def hello(name, word):
#     print('Hello', name, '.Say ' + word, sep='')
#
#
# hello('Igor', 'hi')
# hello('Ivan', 'hello')

# def get_sum(a, b):
# return a + b
#     print(a + b)
#
# x = 2
# y = 3

# /?
# res = get_sum(x, y)
# print(res)
# get_sum(2.6, 4.3)
# get_sum('as', 'def')
# get_sum('aaa', str(x))
#
#
# def ret(r, t, s):
#     for i in range(r):
#         if i % 2 == 0:
#             print(t, end='')
#         else:
#             print(s, end='')
#
#
# ret(5, '+', '-')

# def hi(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(hi(10, 5))
# print(hi(5, 15))

# def maxmin(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
#
# print(maxmin(10, 5))
# print(maxmin(5, 15))


# def maxmin(x, y):
#     if x > y:
#         return x - y
#     if x < y:
#         return x + y
#
#
# print(maxmin(5, 9))
#
#
# def kub(x):
#     return x ** 3
#
#
# for i in range(1, 11):
#     print(i, 'v kube = ', kub(i))


# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         c = a + b
#         a = b
#         b = c
#     print()
#
#
# fib(22)
# fib(61)

# g = [1, 3, 34, 4, 5, 6]
#
#
# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append()
#     lst.insert(0, start)
#     return lst
#
#
#
#
#
# print(change([1, 2, 3]))
#
# def get_sum(a, b, c=0, d=0):  # Аргумегты по умолчанию
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 3))
# print(get_sum(1, 5, d=6))  # именованные параметры

# def get_sum(a, b, c, d):  # Аргумегты по умолчанию
#     return a + b + c + d
#
#
# print(get_sum(3, 1, 5, 2))  # именованные параметры


# def ion(x, y):
#     for i in range(x):
#         print(y, end='')
#
#
# ion(15, '+')

# summ = 0
# summa = 0
# def suma(x):
#     for i in range(x):
#         if i % 2 == 0:
#             summ += i
#         else:
#             summa += i
#     return summ
# print((suma(9874023))


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         a = n % 10
#         if even and a % 2 == 0:
#             s += a
#         elif not even and a % 2 != 0:
#             s += a
#         n //= 10
#
#     return s
#
#
# print('Summa mechetnix: ')
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print('summa chetnix')
# print(digit_sum(9874023, even=False))

# def display_info(name, age):
#     print("Name: ", name, '\nAge: ', age)
#
# display_info('Ira', 23)
# display_info('Ira', 23)

# def func(a, ln=None):
#     if ln is None:
#         ln = []
#     ln.append(a)
#     return ln


# def func(a, ln=[]):
#     ln.append(a)
#     return ln
#
#
# print(func(1))
# print(func(2))
# print(func(3))

# a1 = [1, 2, 3]
# a2 = [1, 2, 3]

# print(id(a1))
# print(id(a2))
# print(a1 == a2)
# print(a1 is a2)
#
# a3 = 'Hello'
# a4 = 'Hello'
#
# print(id(a3))
# print(id(a4))
# print(a3 == a4)
# print(a3 is a4)
#
# a7 = 5
# a8 = 5
#
# print(id(a7))
# print(id(a8))
# print(a7 == a8)
# print(a7 is a8)

# a1 = [1, 2, 3]
# print(id(a1))
# a1.append(4)
# print(a1)
# print(id(a1))
#
# a1[1] = 'Hello'
# print(a1)
# print(id(a1[1]))

# s = 'Hello '
# print(id(s))
# s += 'World' # s = s + 'World'
# print(s)
# print(id(s))
#
# a = 9
# print(id(a))
# a += 1
# print(a)
# print(id(a))

# st = 'Hello'
# print(id(st))
# st = st[1:-1]
# print(st)
# print(id(st))

# a1 = [1, 2, 3]
# a2 = [1, 2, 3]
# print(id(a1))
# print(id(a2))
# y = a1
# h = 1
# b = h
# print(id(h))
# print(id(b))
# print(a1 == a2)
# print(a1 is a2)
# print(a1 == y)
# print(a1 is y)
# print(a1, y)
# a1[0] = 0
# print(a1)
# print(y)

# x = [1, 2, 3]
# y = x[:]
# k = x
# k[0] =
# print(y)
# y[0] = 0
# print(y)
# print(x)
# print(id(y))
# print(id(x))

# x = [1, 2, 3]
# print(id(x))
# x += [4, 5]
# print(x)
# print(id(x))
#
#
# def add_number(n):
#     print('Внутри функции: ', n, '=', id(n))
#     n += 1
#     print('После присваивания: ', n, '=', id(n))
#
#
# x = 1
# print(x, '=', id(x))
# add_number(x)
# print(x, '=', id(x))

# Картеж (typle)
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(tpl)
#
# a = ()
# print(type(a))
# b = tuple()
# print(type(b))
#
# # Упаковка картежа
# c = 1, 2, 3
# print(c)
# print(type(c))
# print(type(c[1]))
#
# t1 = tuple('hello')
# print(type(t1[2]))
#
#
# a = tuple((1, 2, 3, 4, 5))
# print(a)
# print(a[3])
# s1 = tuple([int(input('-> ')) for i in range(5)])
# print(s1)

# s = input('Введите по порядку, без пробелов элементы кортежа:  ')
# a = tuple(s)
# print(a)
import random as r

# mas = tuple([r.randint(0, 100) for i in range(10)])
# print(mas)
#
# mas = tuple([2 ** i for i in range(1, 13)])
# print(mas)

# t1 = tuple('Hello')
# t2 = tuple(' world')
# t3 = t1 + t2
# print(t3)


# print(len(t3))
# print(t3.count('l'))
# print(t3.count('3'))
# # print(t3.index('0'))
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print('Netu takogo simvola net')
#
# for i in t3:
#     if i == ' ':
#         continue
#     print(i, end=' ')
# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             g = tpl.index(el)
#             s = tpl.index(el, g + 1) + 1
#             return tpl[g:s]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def kortej(a, b):
#     mas = tuple(a for i in range(10))
#     mas = tuple(a for i in range(10))
#     mas2 = tuple(b)
#     mas3 = mas + mas2
#     return mas3
#
#
# print(kortej(r.randint(0, 5), r.randint(-5, 0)))

#
# t = (10, 11, [1, 2, 3], [5, 6, 7], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# print(t, id(t))
# t[4].append('hi')
# print(t, id(t))
# def gg(lst):
#     a = []
#     [a.append(i) for i in reversed(lst) if i not in a]
#     return tuple(a)
#
#
# print(gg([1, 2, 3, 3, 2]))
# print(gg([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))

# Распоковка кортежа
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = 'Igor'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])

# lst = [1, 2, 3, 4, 5]
# a = tuple(lst)
# print(a)
# ls = list(a)
# print(ls)

# contries = (
#     ('England', 80.2, (('London', 3.326), ('Manchester', 718))),
#     ('Spanish', 66, (('Paris', 234), ('Rena', 145)))
# )
# print(contries)
# print(contries[0][0])
# for counrty in contries:
#     counrtyName, counrtyPopulation, cities = counrty
#     print('\nStrana: ', counrtyName, '\nNaselenie: ', counrtyPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print('\nGorod: ', cityName, '\nNaselenie: ', cityPopulation)

# Множества - set()
# s = {'banana', 'apple', 'orange', 'apple', 'orange'}
# print(type(s))
# print(s)
# print(len(s))
#
# b = set('hello')
# print(type(b))
# print(b)
# c = ['red', 'green', 'green', 'blue', 'purple']
# col = set(c)
# print(col)

# s = {x * x for x in range(10)}
# print(s)

# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# num = list({i for i in numbers if i % 2 == 0})
# print(num)
#
# def to_set(a):
#     b = set(a)
#     return b, len(b)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4,5,4,6,2,9,11,3,4,2]))

# c = {'red', 'green', 'green', 'blue', 'purple'}
# print('green' not in c)

# pr = {1, 2, 3, 5, 7, 7, 11}
# for i in pr:
#     print(i, end=" ")

# h = ["ab_1", 'ac_2', 'bc_1', 'bc_2']
# a = {'A' + i[1:]
#      if i[0] == 'a' else 'B' + i[1:]
#      for i in h
#      if i[1] == 'c'}
# print(a)

# a = {0, 1, 2, 3}
# a.add(4)  # добавление элемента
# print(a)
# a.remove(4)  # добавление элемента
# print(a)
# b = 6
# if b in a:
#     a.remove(b)
# print(a)
#
# a.discard(3)  # удаляет элемент если он есть в списке, без ошибки
# print(a)
#
# a.pop()  # Удаление первого элемента
# print(a)
# a.pop()
# print(a)
#
# a.clear()  # удаляет все элементы

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}

# c = a.union(b)
# print(c)
# c = a | b
# print(c)

# a.update(b)
# print(a)
# a |= b
# print(a)

# h = a.intersection(b)
# print(h)

# h = a & b
# print(h)

# h = b - a
# print(h)

# h = b ^ a
# print(h)
#
# b ^= a
# print(b)

# h = a <= b
# print(h)

# c = a.copy() #
# print(c)

# a, b, c, d, e = {1, 2}, {3}, {4, 5}, {6, 7}, {8, 9}
# ob = a | b | c | d | e
# print(ob)
# maxs = max(ob)
# minx = min(ob)
# print('unic elems count: ', len(ob))
# print('Min elem: ', maxs)
# print('Max elem: ', minx)
#
# y = input('Введите первую строку: ')
# x = input('Введите первую строку: ')
# c = set(y) & set(x)
# for i in c:
#     print(i, end=' ')

# g = {'Marina', 'Jena', 'Sveta', 'Kostia', 'Ilia'}
# drawing = {'Marina', 'Jena', 'Sveta'}
# music = {'Kostia', 'Jena', 'Ilia'}
# ind = drawing ^ music
# brosil = drawing & music
# print(ind)
# print(brosil)

# тип Frozenset (замороженное множество)
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# g = frozenset({i**2 for i in range(10)})
# print(g)
#
# r1 = set('ABCD')
# b = {frozenset({i + j for j in r1.difference({i})}) for i in r1}
# print(b)


# def superset(s1, s2):
#     if s1 > s2:
#         print('Объект ', s1, ' является чистым супермножеством')
#     elif s1 == s2:
#         print('Множества равны')
#     elif s1 < s2:
#         print('Объект ', s2, ' является чистым супермножеством')
#     elif s1 != s2:
#         print('Супермножество не обнаружено')
#
#
# set_1 = {1, 8, 3, 5}
# set_2 = {3, 5}
# set_3 = {5, 3, 8, 1}
# set_4 = {90, 100}
#
# superset(set_1, set_2)
# superset(set_1, set_3)
# superset(set_2, set_3)
# superset(set_4, set_2)

# Словари{dict}
# h = [1, 2, 3, 4]
#
# # j = {'one': 1, 'two': 2}
# # print(h)
# # print(j)
#
# d = {}
# print(d)
# print(type(d))
# d1 = dict()
# print(d1)
#
# d3 = dict.fromkeys(['a', 'b'], 100)
# print(d3)
#
# user = [
#     ('igor@gmail.com', 'igor'),
#     ('maikl@gmail.com', 'maikl'),
#     ('inna@gmail.com', 'inna')
# ]
# print(user)
# d_user = dict(user)
# print(d_user)
#
# d4 = {a: a ** 2 for a in range(7)}
# print(d4)
# print(d4[2])
# d4[2] = 15
# print(d4)
# d4[5] = 4 ** 2
# print(d4)

# d5 = {0: 'tex1', 'one': 40, (1, 2.3): 'kortej', 42: [2, 3, 6, 7], True: 1}
# print(d5)
# print(d5[42][1])
# print(d5[(1, 2.3)])
# del d5[(1, 2.3)]
# print((d5))
#
# print('one' in d5)
# print(40 in d5)
# print(d5.keys())

# d6 = {'one' : 1, 'two': 2, 'three': 3}
# # print(d6["four"])
# key = 'four'
# # if key in d6:
# #     del d6[key]
# print(d6)
# try:
#     del d6[key]
# except KeyError:
#     print('Елемента с ключем "' + key + '" нет в словаре')
#
# print(d6)
#
# a = [1, 2, 3, 4]
# # c = dict(a)
# # print(c)
# # b = {'one': 1, 'two': 2}
# # print(b)
#
# d = {}
# print(type(d))
#
# d1 = dict()
# print(d1)
# d3 = dict.fromkeys(['a', 'b'], 1000)
# print(d3)
#
# user = (
#     ('igor@gmail.com', 'igor'),
#     ('slava@gmail.com', 'slava'),
#     ('anna@gmail.com', 'anna')
# )
# print(user)
# d_user = dict(user)
# print(d_user)

# d4 = {a: a ** 2 for a in range(7)}
# print(d4)
# print(d4[2])
# d4[2] = 15
# print(d4)
# d4[5] = 4 ** 2
# print(d4)

# d5 = {0: 'text1', 'one': 40, (1, 2.3): 'kortej', 31: [2, 3, 6, 7], True: 1}
# print(d5)
# print(d5[31][1])
# print(d5[(1, 2.3)])
# del d5[(1, 2.3)]
# print(d5)
#
# print('one' in d5)
# print('a' in d5)
#
# print(d5.keys())
#
# if 'one' in d5:
#     print("True")
# if 'one' in d5.keys():
#     print("True")

# d6 = {'one': 1, 'two': 2, 'three': 3}
# # print(d6['four'])
# key = 'four'
# # if key in d6:
# #     del d6[key]
# print(d6)
# try:
#     del d6[key]
# except KeyError:
#     print('Элемента с заданным ключом "' + key + '" нет в словаре')
# print(d6)
# for key in d6:
#     print(key,'=', d6[key])

# r = 1
# d8 = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# for key in d8:
#     r *= d8[key]
# print(r)
#
# d9 = {}
#
# for i in range(1,5):
#     d9[i] = input('->')
# print(d9)
#
# delg = int(input('kakuyu stroku udalit: '))
# del d9[delg]
# print(d9)
# print(len(d6))
#
# capitals = dict()
# capitals['Russia'] = 'Mockow'
# capitals['Italy'] = 'Rime'
# capitals['Spanich'] = 'Madrid'
#
# countries = ['Russia', 'Italy', 'France', 'Spanich']
#
# for country in countries:
#     if country in capitals:
#         print('Столица страны ' + country + ': ' + capitals[country])
#     else:
#         print('В базе нет страны названием: ' + country)

# di = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400]
# }
# for i in di:
#     print(i, ') ', di[i][0], ' - ', di[i][1], ' шт. по ', di[i][2], 'руб', sep='')
# l = 100
# for i in range(l):
#     h = (input('№: '))
#     str(h)
#     kol = int(input('kolichestvo: '))
#     di[h][1] = kol
#     print(di)

#
# a = {
#     "First": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "Second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ':', a[x][y])
#
#
# c = {
#     "John": {
#         1: "3056",
#         2: "8463",
#         3: "8441",
#         4: '2694'
#     },
#     "Tom": {
#         1: "4832",
#         2: "6786",
#         3: "4737",
#         4: '3612'
#     },
#     "Anne": {
#         1: "5239",
#         2: "4802",
#         3: "5820",
#         4: '1859'
#     },
#     "Fiona": {
#         1: "3904",
#         2: "4324",
#         3: "4356",
#         4: '3556'
#     },
# }
# print(c)
# for x in c:
#     print(x)
#     for y in c[x]:
#         print('\t', y, ':', c[x][y])
#
# hh = input('Name: ')
# hh2 = int(input('Region: '))
# print(c[hh][hh2])
# hh3 = input('New item: ')
# c[hh][hh2] = hh3
# print(c)

# a = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# h = {key: value for key, value in a.items()}
# print(h)
#
# a = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# h = {key: value for key, value in a.items() if value <= 2}
# print(h)

# a = {i:i for i in [10,20,30,40]}
# print(a)
#
# s = 'hello'
# b = {i: i for i in s}
# print(b)

# value = input('-> ')
# lst = [1, 2, 3, 4]
# d = {k: value for k in lst}
# print(d)


# m = dict()
# m[(0, 1)] = 1
# m[(1, 2)] = 3
# m[(2, 0)] = 2
#
# # try:
# #     print(m[(2, 1)])
# # except KeyError:
# #     print(0)
# print(m.get((2,1), 0))
# print(m.get((2,0), 0))
# # if (2,1) in m:
# #     print(m[(2, 1)])
# # else:
# #     print(0)

# SciPy

# list()
# a = {1: "Rectagle", 2: 'Triangle', 3: 'Circle'}
# value = list(a.values())  # Список значений словаря
# print(value)
# value = list(a.keys())  # Список ключей словаря
# print(value)
#
# par = list(a.items())  # Список пар словаря
# print(par)
# mass = ['one', 1, 2, 3, 'two', 10, 20, 'tree', 15, 36, 60, 'four', -2]
# hh = {}
# for k in mass:
#     if k is str(k):
#         hh[k] = []
#         lst = k
#     else:
#         hh[lst].append(k)
# print(hh)
#

# Zip
# a = {3: 'Math',4 : 'April', 5: 'May'}
# b = {3: 'rrr', 12: 'Dec',1: 'Jan',2: 'Feb'}
# # c = [4.6, 4.8, 9.2]
# # # d = {k: v for (k, v) in zip(b, a)}
# # d = zip(a,b,c)
# # print(list(zip(range(5), range(2))))
#
# for (k1, v1) , (k2, v2) in zip(a.items(), b.items()):
#     print(k1, '-> ', v1)
#     print(k2, '-> ', v2)

# pairs = [(1, 'a'),(2, 'b'),(3, 'c'),(4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# ls = [2, 1, 5, 4]
# n = ['a', 't', 'h', 'b']
# a = sorted(zip(ls, n))
# print(a)

# a = list(zip(ls, n))
# print(a)
# a.sort()
# print(dict(a))

# totalSal = [52000, 51000, 48000]
# month = ['Jan', 'Feb', 'Mat']
# ProductCost = [46800, 45900, 43200]
# for t, p, m in zip(totalSal, ProductCost, month):
#     profit = t - p
#     print('Obchaya pribil v', m , ' = ', profit)

# one = {'apple': 23, 'orange': 43}
# two = {'pepper': 11, 'onion': 21}
# print({**one, **two})
# for k, v in {**one, **two}.items():
#     print(k, '->', v)

# data = {9: 5, 2: 6, 3: 7, 4: 8, 5: 9, 6: 4, 7: 1}
# for i, val in enumerate(data):
#     print(i, ':', val)
# d = {1: {'a': 1, 'b': 2, 'c': 3},
#      2: {'a': 10, 'b': 20, 'c': 30}}
#
# for i, k in enumerate(d):
#     print(i, ') key = ', k , ', value = ', d[k], sep='')


# lst = [1, 2, 3, 4, 5]
# itr = iter(lst)
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr, 'STOP'))


# lst = [1, 2, 3, 4, 5]
# b = enumerate(lst, 1)
# c = next(b)
# print(b)
# print(type(c))
# print(next(b))


# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args, **kwargs):
#     return args, kwargs
#
#
# print(func(4, 5, 6, a=1, b=3, c=5))
# print(func())
# print(func(a='Python'))
#
#
# def summa(*ar):
#     # res = 0
#     # for n in ar:
#     #     res += n
#     # return res
#     return sum(ar)

# print(summa(1,2,3,4,5))
# print(summa(1,3,5))

# def u(*uta):
#     return {i: i for i in uta}
#
#
# print(u(1, 2, 3, 4))
# print(u('grey', (2, 17), 3.11, -4))


# def u(*uta):
#     summa = sum(uta)
#     hg = []
#     j = len(uta)
#     sred = summa / j
#     print(sred)
#     for i in uta:
#         if i < sred:
#             hg.append(i)
#     return hg
#
#
# print(u(1, 2, 3, 4, 5, 6, 7, 8, 9))

# def print_scores(student, *scores):
#     print('Имя студента: ', student)
#     for s in scores:
#         print(s)
#
#
# print_scores("Михаил", 100, 90, 88, 92, 99)
# print_scores("Игорь", 10, 92, 48, 42, 9)


# g = []
# res = []
#
#
# def rev(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def ooo(*yy, only_odd=False):
#     if only_odd is True:
#         for k in yy:
#             if k % 2 != 0:
#                 g.append(rev(k))
#         return g
#     else:
#         for i in yy:
#             res.append(rev(i))
#         return res
#
#
# print(ooo(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=False))
# print(ooo(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))
#

# def info(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#     print()
#
#
# info(firstname='Ivan', lastname="Ivanov", age=22, phone='8345122432')
# info(firstname='Iha', lastname="Itav", email='itav@ag.com', country='America', phone='8345122432')


# my_dict = {'one': 'first'}
#
#
# def db(**kwargs):
#     my_dict.update(**kwargs)
#     return my_dict
#
#
# db(k1=22, k2=31, k3=11, k4=91)
# print('my_dict = ', db(name='Bob', age=31, weight=61, eyes='grey'))


# def func(name, *args, odd=False, **kwargs):
#     return name, args, odd, kwargs
#
#
# print(func('Irina', 1, 2, 3, 4, odd=True, one='1', three='3'))

# def func(name, *args, odd=False, **kwargs):
#     print(args[0])
#     print(kwargs['one'])
#
#
# print(func('Irina', 1, 2, 3, 4, odd=True, one='1', three='3'))

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {**x,'one':1, 'two':2, **y}
# print(z)


# name = 'Tom'
# print(name)
#
#
# def hi():
#     global name
#     name = 'Same'
#     print('Hello', name)
#
#
# def bye():
#     print('Good bye', name)
#
#
# hi()
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5


# def add_two(a):
#     x = 2
#     return a + x
#
#
# print(add_two(3))


# def add_five(a):
#     x = 2
#
#     def wrap():
#         print('x =', x)
#         return a + x
#
#     return wrap()
#
#
# print(add_five(5))


# x = 4
#
#
# def func():
#     a = 3
#     print(x + a)
#
#
# func()

#
# import builtins
#
# names = dir(builtins)
# for i in names:
#     print(i)


# def outer_func(a):
#     def inner_func():
#         print('Hello, ', a ,'!')
#
#     inner_func()
#
#
# outer_func('world')


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print('Summa vnutreney fun: ',a + b)
#
#     print('Znachenie vneshney peremenoy a :', a)
#     fun2(4)
#
#
# fun1()


# x = 25
#
#
# def fn():
#     global t
#     a = 30
#     t = a
#     print('flobal: ', x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('nonlocal: ', a)
#         return
#
#     inner()
#     return
#
#
# fn()
#
# z = x + t
#
# print(z)

# def fn1():
#     x1 = 25
#
#     def fn2():
#         x1 = 33
#
#         def fn3():
#             nonlocal x1
#             x1 = 55
#
#         fn3()
#         print('fn2.x1', x1)
#
#     fn2()
#     print('fn1.x1', x1)
#
#
# fn1()

#
# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# result = outer(2, 3, -1, 4)
# print('Result: ', result)
#

# Closure (Замыкание)
# def incement(n):
#     def inner_incement(x):
#         return n + x
#
#     return inner_incement

# a = incement(10)
# print(a(5))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         b = b + 'str'
#         a = a + 1
#         return a, b, c
#
#     return func2()
#
#
# func = func1()
# print(func)

# def city(h):
#     s = 0
#
#     def infun():
#         nonlocal s
#         s += 1
#         print(h, s)
#
#     return infun
#
# res1 = city('Москва')
# res1()
# res1()
# res1()
# res1()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Andri': 88,
#     'Mirinda': 55,
#     'Eli': 33,
#     'Rendi': 78,
#     'Enda': 55
# }
#
#
# def make_classfilter(lower, upper):
#     def class_student(exem):
#         return {k: v for (k, v) in exem.items() if lower <= v <= upper}
#
#     return class_student
#
#
# a = make_classfilter(80, 100)
# b = make_classfilter(70, 80)
# c = make_classfilter(50, 70)
# d = make_classfilter(0, 50)
# print(a(students))
# print(b(students))
# print(c(students))
# print(d(students))


# def ff(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def rep():
#         print()
#
#     rep.add = add
#     rep.sub = sub
#     rep.mul = mul
#     return rep
#
# obj1 = ff(5,2)
# print(obj1.add())
#
# obj2 = ff(5,2)
# print(obj2.sub())
#
# obj3 = ff(5,2)
# print(obj3.mul())

# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
# print(func(1,2))

# print((lambda x, y: (x ** 2) + (y ** 2))(2, 5))

# summ = lambda a = 1, b= 2, c = 3: a + b + c
# print(summ())
# print(summ(10))
# print(summ(10,1))


# f1 = lambda *args: args
# print(f1(1, 2, 3, 4))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for u in c:
#     print(u('abc'))

#
# def inc(b):
#     return lambda x: x + b

# inc = (lambda f: (lambda x: x + f))
#
# f = inc(42)
# print(f(5))
# print(f(2))
#
#
# print((lambda f: (lambda x: x + f))(42)(3))
#
# print((lambda x, y, t: x + y + t)(2, 4, 6))


# d = {'c': 4, 'b': 15,'a': 10 }
# list_d = list(d.items())
# print(list_d)
# list_d.sort()
# list_d.sort(key=lambda i: i[1])
# print(list_d)
# print(dict(list_d))
#
# slovar = [{'name': 'Антон','last name':"Бирюков", 'raiting': 9},
#           {'name': 'Алексей','last name':"Бодня", 'raiting': 10},
#           {'name': 'Федор','last name':"Сидоров", 'raiting': 4},
#           {'name': 'Михаил','last name':"Семенов", 'raiting': 6}]
#
# lst_sort_lastName = sorted(slovar, key= lambda item: item['last name'])
# lst_sort_lastName2 = sorted(slovar, key= lambda item: item['raiting'])
# lst_sort_lastName3 = sorted(slovar, key= lambda item: item['raiting'], reverse=True)
#
# print(lst_sort_lastName)
# print(lst_sort_lastName2)
# print(lst_sort_lastName3)

# a = [
#     (lambda x, y: x + y),
#     (lambda x, y: x - y),
#     (lambda x, y: x * y),
#     (lambda x, y: x / y)
# ]
# b = a[1](5,12)
# print(b)


# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))
#
# d = {
#     1: lambda: print('Monday'),
#     2: lambda: print('Tuesday'),
#     3: lambda: print('Wednesday'),
#     4: lambda: print('Thursday'),
#     5: lambda: print('Friday'),
#     6: lambda: print('Saturday'),
#     7: lambda: print('Sunday')
# }
#
from math import *


#
# d[2]()
# dd={
#     '1': lambda x: pi * x ** 2,
#     "Прямоугольник" : lambda x, y: x * y,
#     "Трапеция": lambda x, y, z: 0.5 * (x + y) * z
# }
# print('Площадь окружности', dd['1'](12))
# print('Площадь трапеции', dd['Трапеция']())
# print('Площадь прямоугольника ', dd['Прямоугольник'])

# True if условие else FALSE

# maxxx = lambda a, b: a if a > b else b
# print(maxxx(15, 13))
# print(maxxx(5, 13))

# min_1 = lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c
# print(min_1(2, 10, 9))

# def mul(t):
#     return t * 2
#
#
# lst = [3, 8, 12, -5, -10]
# # lst2 = list(map(mul, lst))
# # print(lst2)
#
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)


# t = (2.88 , -1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)

# lst = ['1', '2', '3', '4', '5', '6', '7']
# lst2 = list(map(int, lst))
# print(lst2)


# areas = [3.56773, 5,456345, 6.667345, 5.65362222234, 3334.5523562]
# rs = list(map(round, areas, range(1, 7)))
# print(rs)


# strr = ['a', 'b', 'c', 'd', 'e']
# stre = [1, 2, 3, 4, 5]
# res = list(map(lambda x, y: (x, y), strr, stre))
# print(res)

# strr = [1, 2, 3]
# stre = [4, 5, 6]
# res = list(map(lambda x, y: (x + y), strr, stre))
# print(res)

# s ='hello'
# res = list(map(lambda x: (x * 3), s))
# print(res)

# t = ('sdfdfdf', 'sdffg', 'sff', 'e3', 'dsdrt')
# t2 = tuple(filter(lambda s: len(s) == 5, t))
# print(t2)


# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)
# from random import *
# b = [randint(1,40) for i in range(10)]
# res = list(filter(lambda s: 10 <= s <= 20, b))
# print(res)

# b = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda s: s % 15 == 0, b))
# print(res)

# m = list(map(lambda x: x ** 2 , filter(lambda x: x % 2 != 0, range(10))))
# print(m)
# gg = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')
# m = list(filter(lambda x: x == x[::-1], gg))
# print(m)

# def square(n):
#     """Принимет число n , возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(help(square))
#
# # a = '''Три двойных ковычки'''
# # b = """Три двойных ковычки"""
# # print(a)
# # print(b)

import  math
def cylinder(r, h):
    """
    Вычисляет площадь цилиндра.

    Вычисляет площадь цилиндра на основе заданной высоты и радиуса основания
    :param r: положительное число , радиус основания цилиндра
    :param h: положительное число , высота основания цилиндра
    :return: положительное число , площадь цилиндра
    """
    return 2 * math.pi * r * (r + h)


print(cylinder(3, 6))
print(cylinder.__doc__)
print(max.__doc__)