# Декараторы
# def hello():
#     return "Hello, I am func 'Hello'"
#
# def super_func(func):
#     print("Hello, I am func 'super_fumc'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "Hello, I am func 'Hello'"
#
# test = hello
# print(test())

# def my_decorator(func):
#     def funccc():
#         print("Code before")
#         func()
#         print('code after')
#     return funccc
# @my_decorator
# def func_test():
#     print("Hello, I am func 'Hello'")
#
#
# # fdf = my_decorator(func_test)
# # fdf()
#
# func_test()

#
# def my_decorator(func):
#     def funccc():
#         print("Code before")
#         func()
#         print('code after')
#
#     return funccc
#
#
# @my_decorator
# def func_test(a,b):
#     print(a * b)
#
#
# # fdf = my_decorator(func_test)
# # fdf()
#
# func_test(2,5)


# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + "/<b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + "/<i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return 'text'

# def deco(fn):
#     counter = 0
#     def wrapper():
#         nonlocal counter
#         fn()
#         counter += 1
#         print('Вызов функции', counter)
#
#     return wrapper
#
#
# @deco
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()


# def arfs_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные: ", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @arfs_decorator
# def print_full_name(first, last):
#     print("My name is ", first, last)
#
#
# print_full_name("Irina", 'Lavrova')


# def arfs_decorator(fn):
#     def wrap(*args1, **kwargs2):
#         print("args: ", args1)
#         print("kwargs: ", kwargs2)
#         fn(*args1, *kwargs2)
#
#     return wrap
#
#
# @arfs_decorator
# def print_full_name(a, b, c="Vitaliy", study='Python'):
#     print(a, b, c, 'изучают', study, '\n')
#
#
# print_full_name("Irina", 'Lavrova', 'Shebankova', study='Javascript')
# print_full_name("Irina", 'Bladimir')


# def arfs_decorator(fn):
#     def wrap(*args1):
#         print('*' * 20)
#         fn(*args1)
#         print('*' * 20)
#
#     return wrap
#
#
# @arfs_decorator
# def one(a, b):
#     print(a + b)
#
#
# @arfs_decorator
# def two(a, b, c):
#     print(a * b * c)
#
#
# one(2, 3)
# two(2, 3, 4)

#
# def args_decorator(arg1, arg2):
#     print("i sozdayu decorator. Arguments: ", arg1, arg2)
#
#     def my_decorator(func):
#         print('i - decorator. Arguments: ', arg1, arg2)
#
#         def wrapper(func_arg1, func_arg2):
#             print('i - obertka vokrug decoriruemoy func')
#             func(arg1, arg2)
#             func(func_arg1, func_arg2)
#
#         return wrapper
#
#     return my_decorator
#
#
# @args_decorator('Ivan', 'Lenikov')
# def print_full_name(first, last):
#     print("My name is: ", first, last)
#
#
# print_full_name('Igor', 'Temaskov')


# def args_decorator(decorator_text):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end='')
#             func(*args)
#
#         return wrap
#
#     return my_decorator
#
# @args_decorator(decorator_text='Hello, ')
# def hello_world(text):
#     print(text)
#
# hello_world('world!')

# def args_decorator(decorator_text):
#     def my_decorator(func):
#         def wrap(*args):
#             return func(*args) * decorator_text
#
#         return wrap
#
#     return my_decorator
#
# @args_decorator(3)
# def hello_world(a):
#     return a
#
# print(hello_world(5))
# def typed(*args, **kwargs):
#     def wraper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError('Типы данных не соотвествует)')
#
#             for i in kwargs:
#                 if type(f_kwargs[i]) != kwargs[i]:
#                     raise TypeError('Типы данных не соотвествует)')
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wraper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z='Hello! '):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# print(typed_fn(3, 4, 6))
# print(typed_fn2('Hello, ', 'world', '!'))
# print(typed_fn3('Hello, ', 'world', z=5))

# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end='')
#             func(*args)
#         return wrap
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator
# def hello_world(text):
#     print(text)
#
#
# @args_decorator(decorator_text='Hello, ')
# def hello_world2(text):
#     print(text)
#
#
# hello_world('Hi!')
# hello_world2('world!')


# print(int('19'))
# # print(int('19.5'))
# print(int(19.5))
# print(int('100', 6))
# print(int('100', 8))
# print(int('100', 16))

# print(bin(19))  # Двоичная система
# print(oct(19))  # Восмеричная система
# print(hex(19))  # Шестнадсатеричная система
#
# print(0b10010)
# print(0o25)
# print(0x11)


# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e * -3)
# print(e in 'i am learn Python')
#
# s = 'Hello'
# print(s[::-1])
#
# s = 'abcdefg'
# print(s[slice(2, 5)])
# print(s[slice(5, None, -1)])

# s = 'python'
# print(id(s))
# s = s[:3] + 'g' + s[3:]
# print(id(s))
# print(s)
#
# def chage_char(s, c_old, c_new):
#     s2 = ''
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i = i + 1
#     return s2
#
#
#
#
# str1 = 'Я изучаю Nuthon. Мне нравится Nuthon.Nuthon очень интересный язык программирования'
# str2 = chage_char(str1, 'N', 'P')
# print(str1)
# print(str2)
# # str2 = str1[0:9] + 'P' + str1[10:30] + 'P' + str1[31:37] + 'P' + str1[38:]
# # print(str2)
# #
# print(str1.replace('Nuthon', 'Python'))

# print(u'Hello')
# print('I\'m learning\nPython')
# print(r'C:\file.txt')
# print(r'C:\file.txt\\'[:-1])
# print(r'C:\file.txt' + '\\')
# print('C:\\file.txt\\')
# print(b'a1b2c3'[1])
# print(b'\xff\xfe\xfd')
# print(b'\xff\xfe\xfd'[1])

# name = 'Lera'
# age = 25
# print(f'My name is {name}, i {age} old')

# import math
# print(f"Znachenie chisla pi: {math.pi:.2f}")
#
# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {x * y / 2:.0f}")
# planets = ["Меркурий", "Венера", "Земля", "Марс"]
# print(f'Мы живём на планете {planets[2]}')
#
# planet = {"name":"Земля", "radius": 5432656}
# print(f"Планета {planet['name']}. Радиус {planet['radius']/ 1000}км")
#
# print(f"13 / 3 = {round(13/3)}")
# name = 'friend'
# prof = 'programmist'
# lang = 'pyrthon'
# message = (
#     f"Hi {name}."
#     f"U {prof}."
#     f"Of language {lang}"
# )
#
# print(message)
# a = 74
# print(f"{{{a}}}")

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr"home\{dir_name}\{file_name}")
# print("home\\"+ dir_name + '\\'+ file_name)

# s = '5'
# s2 = '1'
# print(min(s, s2))

# print(ord('a')) # 97
# print(ord("#")) # 35
# print(ord("к"))
#
# while True:
#     n = input('-> ')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# stroka = 'Test string for me'
# stroka_lst = []
# suma = 0
# for i in stroka:
#     stroka_lst.append(ord(i))
#     suma += ord(i)
# sred_ar = round(suma/len(stroka))
# print('ASCII коды: ', stroka_lst)
# stroka_lst = [sred_ar] + stroka_lst
# print('Среднее арифметическое: ', stroka_lst)
# stroka_lst += [x for x in [ord(x) for x in (input('-> '))[:3] if x not in stroka_lst]]
# print(stroka_lst)
# if stroka_lst[-1] in stroka_lst[:-1]:
#     print("Количество последних элементов", stroka_lst.count(stroka_lst[-1] -1))


# print(chr(97))
#
# a = 122
# b = 97
# g = []
# for i in range(b, a+1):
#     g.append(chr(i))
# print(*g)
#

# список словарь кортеж множества
# s = 'hello, WORLD! I am learning Python. 123@!'
# print(id(s))
# print(s.capitalize())  # первый символ преобразуется в верхний регистр, все остальные в нижний
# print(s.lower())  # преобразует в нижний регистр
# print(s.upper())  # преобразует в вверхний регистр
# print(s.swapcase())  # преобразует в противоположный решистр
# print(s.title())  # преобразует первые буквы всех слов в зашлавные
# print(s.count('l', 3, 4))  # возвращает количество вхождений подстроки в строку
# print(s.find('l'))  # возвращает первый индекс который соотвествет элементу
# sttt = input('Введите два слова через пробел: ')
# d = sttt[sttt.find(' ') + 1:]
# b = sttt[:sttt.find(' ')]
# print(d)
# print(b)
# n = d + ' ' + b
# print(n)

# g = 'ab12c59p7dq'
# digits = []
# for i in g:
#     if '1234567890'.find(i) != -1:
#         digits.append(i)
# print(*digits)

# print(s.index('Python'))  # Vозвращает первый индекс который соотвествет элементу
# # Возвращает ValueError если совпадение не найдено
#
# y = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
# u = y.index('(')
# h = y.index(')')
# l = y[u+1:h]
# print(l)
# print((s.rfind("l", 18)))

# h = 'Send heri yulio hertino ftfdf'
# jjj = []
# j = 0
# for i in h:
#     j += 1
#     if i == 'f':
#         jjj.append(j)
#
# print(jjj)

# [20:55] Путанов Евгений Александрович
# s = 'aaaaaaaaaaafaaaaaaaaaaafaaaaaaa'
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') >= 2:
#     print(s.find('f'), s.rfind('f'))
#
# [20:55] Баторшин Артем Андреевич
# s = input('Введите строку: ')
# if s.count('f') == 0:
#     pass
# elif s.count('f') == 1:
#     first = s.find('f')
#     print(first)
# else:
#     first = s.find('f')
#     second = s.rfind('f')
#     print(first, second)

import re


#
# h = 'Я ищю совпадения в 2021 году. И я их найду в 2 счёта.'
# reg = 'я'
# print(h.find(reg))  # 15
# # find() - в строке будет искать шаблон и возвращать индекс первого вхождения подстроки в строке .
# # Если шаблон не найден, то будет ворзвращать значение "-1"
# print(reg in h)
#
# print(re.findall(reg, h))  # возвращает список, содержащий все совпадения с регулярным выражением
# print(re.findall("12", h))
# print(re.search(reg, h))  # индексы первого совпадения
# print(re.search(reg, h).span())
# print(re.search(reg, h).start())
# print(re.search(reg, h).end())
# print(re.search(reg, h).group())
# # reg = 'Я'
# print(re.match(reg, h))  # Поиск по заданному шабллону в начале строки
# reg = r'\.'
# print(re.split(reg, h, 1))  # Возращает список, в котором строка разбита по шаблону
# print(re.sub(reg, '!', h)) # Заменяет совпадения указанным методом

# h = 'Я ищю совпадения в 2021 году. И я их найду в 2 счёта.'
# reg = '[0-9]'
# print((re.findall(reg, h)))
#
# h = 'Я ищю совпадения в 2021 году. И я их найду в 2 счёта.'
# reg = '[12][0-9][0-9][0-9]'
# print((re.findall(reg, h)))


# reg = '[А-Яа-яё].'
# reg1 = '[А-Яа-яё.]'
# s = "Ели[-ели]"
# reg = r'[А-Яa-яё.\[\]-]'
# print((re.findall(reg, h)))
# print((re.findall(reg1, h)))
# print((re.findall(reg, s)))

# reg = r'[^0-9]'  #  [^abc] = символ ^ возвращает совпадение для любого символа кроме заданных
# print((re.findall(reg, h)))

# storka = 'Час в 24-часовом формате от 00 до 23. 2021-01-15Т21:45. Минуты, в диапозоне от 00 до 59. 2021-06-15Т01:09.'
# reg = r'[0-2][0-9][\:][0-5][0-9]'
# print((re.findall(reg, storka)))
# h = 'Я ищю совпадения в 2021 году. И я их найду в 2 счёта.'
# reg = r'ния\b'
# print((re.findall(reg, h)))
# \d - одна любая цифра [0-9]
# \w - буква , цифра , символ подчеркивания (_)
# \s - один пробельный сивол (включая табуляцию и перенос строки)
# \D - все кроме цифр
# \W - все кроме букв, цифр, символа подчеркивания (_)
# \S - все кроме пробельного сивола (включая табуляцию и перенос строки)
# \A - ищет символы в начале строки
# \Z - ищет последний символ строки
# \b - ищет окончания слов
# \B - ищет неокончания слов

# h = 'Я ищю совпадения в 2021 году. И я их найду в 2 счёта.'
# reg = r'20*'
# print((re.findall(reg, h)))

# Количество повторений
# + - от 1 до беск
# * - от 0 до беск
# ? - от 0 до 1


# d = 'Цифры: 7, +17. -42, 0013, 0.3'
# print(re.findall(r'[+-]?\d+', d))

# s = '05-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub('#.*', '', s))
# print('Дата рождения:', re.sub('-', '.', re.sub('#.*', '', s)))

# s = '12345'
# reg = r'\d{4}'
# print(re.findall(reg, s))

# s = 'МИД = Министерство иностраных дел, ГЭС - гидроэлектростанция, ФСБ - Федеральная служба безопасности'
# reg = r'[А-ЯЁ]{2,}\s*[А-ЯЁ]'
# print(re.findall(reg, s))

# t = '+7 499 456-45-78, +74994564578, 7 (499) 456-45-78, 74994564578'
# reg = r'[+]?7[\d]{10,}'
# print(re.findall(reg, t))

# h = 'Я ищю совпадения в 2021 году. И я их найду в 2 счёта.'
# reg = r'\w+\.$'
# print((re.findall(reg, h)))


# h = '45 78 458 78'
# reg = r'^\d+\s+\d+$'
# print((re.findall(reg, h)))

#
# h = 'Я ищю совпадения в 2021 году. И я их найду в 2 счёта.'
# reg = r'я'
# print((re.findall(reg, h, re.IGNORECASE)))
# print((re.findall(r'\w+', '12 + h + ؑ۲',flags=re.ASCII)))
# print((re.findall(r'\d+', '12 + ۲ؑ ')))
#
#
# # re.DEGUG
# # re.LOCALE
# # re.DOTALL
#
# text = r'''
# Торт
# с вишней
# вишней2
# '''
# print(re.findall(r'Торт.с', text))
# print(re.findall(r'Торт.с', text, flags=re.DOTALL))
# print(re.findall(r'виш\w+' , text, flags=re.MULTILINE))

# print(re.findall('''
# [\w\.-]+
# @ # разбиваем по @
# [\w\.-]+
# ''', 'test@mail.ru', re.VERBOSE))

# s = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# reg = r'\w*\s*=\s*[^;]+'
# print(re.findall(reg, s))
#
# def validate_name(name):
#     return re.findall(r'^[a-z0-9_-]{3,16}$', name, re.IGNORECASE)
#
#
# print(validate_name('Python_master'))

# Жадные(greedy) - захватывает максимально возможные символы
# ? Ленивые(lazy) - захватывают минимально возможное число

# *?, +?, ??
# {n,m}?, {, m}?, {n, ?}?
# text = '<body>Пример жадного соотвествия регулярного выражений</body>'
# print(re.findall('<.*>', text))
# print(re.search('<.*>', text).group())

# s = '<p>Изображение <img src="bg.jpg"> -  фон страницы</p>'
# reg = r"<img[^>]*>"
# print(re.findall(reg, s))

# text = 'Python[12]gggg[2]fhhnn[5]bhgffdgjh[4]'
# reg = r'\[.*?]'
# print(re.findall(reg, text))

# s = 'Петр, Ольга ,Виталий отлично учатся!'
# reg = 'Петр|Ольга|Виталий'
# print(re.findall(reg, s))

# s = "World2016, PS6, AI5, wq"
# reg = r'([a-z]+)(\d*)'
# print(re.findall(reg, s, re.I))

# s = '5 + 7*2 - 4'
# reg = r'\s*[+*-]\s*'
# # reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))
# arr = []
# s = '28-08-2021'
# reg = r'([0-2][0-9]|[3][01])-([0][1-9]|[1][0-2])-([0-2][0-9][0-9][0-9])'
# print(re.findall(reg, s))

# s2 = '28-08-2021'
# reg2 = r'(\d+)'
# print(re.findall(reg2, s2))


# 192.168.222.225
# s = "127.0.0.1"
# reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg2 = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# print(re.findall(reg2, s))

############
# s = 'Базовый JS прост. Продвинутый Python сложен. Базовый Python прост.'
# reg = r'[а-яё]+(?= Python)'
# print(re.findall(reg,s, re.I))
#############
# s = 'Базовый JS прост. Продвинутый Python сложен. Базовый Python прост.'
# reg = r'Базовый(?! Python)'
# print(re.findall(reg,s, re.I))
############
# s = 'Базовый JS прост. Продвинутый Python сложен. Базовый Python прост.'
# reg = r'(?<=Базовый )\w{2,6}'
# print(re.findall(reg, s, re.I))
############
# s = 'Базовый JS прост. Продвинутый Python сложен. Базовый Python прост.'
# reg = r'(?<!Продвинутый )Python'
# print(re.findall(reg, s, re.I))

# s = "КарлIV, КарлIX, КарлV, КарлVI, КарлVII, КарлVIII, ЛюдовикIX, ЛюдовикVI, ЛюдовикVII, ЛюдовикVIII, ЛюдовикX, ..., " \
#     "ЛюдовикXVIII, ФилиппI, ФилиппII, ФилиппIII, ФилиппIV, ФилиппV, ФилиппVI"
# reg = r'Людовик(?=VI)\w+'
# reg2 = r'Людовик(?!VI)\w+'
# reg3 = r'\w+(?<=Людовик)VI'
# reg4 = r'\w+(?<!Людовик)VI'
# print(re.findall(reg, s, re.I))
# print(re.findall(reg2, s, re.I))
# print(re.findall(reg3, s, re.I))
# print(re.findall(reg4, s, re.I))


# s = "1X, Text ABC 123 A1B2C3"
# reg = r'(?<!\d)\d(?!\d)'
# print(re.findall(reg, s))
#
# s1 = "text from #START# till #END#"
# reg1 = r'(?<=#START#).*(?=#END#)'
# print(re.findall(reg1, s1))
#
# s2 = "12_34__56"
# reg2 = r'\d+(?=_(?!_))'
# print(re.findall(reg2, s2))


# h = 'Я ищю совпадения в 2021 году. И я их найду в 2 счёта.'
# reg = r'([0-9]+)\s(\D+)'
# print(re.findall(reg, h))
# print(re.search(reg, h).group())
# m = re.search(reg, h)
# print('Строка: ', m[0])
# print('Цифра: ', m[1])
# print('Буквы: ', m[2])


# s = 'Самолет прилетает 10/23/2021. Будем вас рады видеть после 10/24/2021'
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# y = 'google.com and google.ru'
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', y))


def is_roman_number(num):
    pattern = r'^M{0,3}(CD|CM|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$'
    if re.search(pattern, num):
        return True
    return False


print(is_roman_number('MMDCCLXXIII'))
print(is_roman_number('CCCMMVIIVV'))
