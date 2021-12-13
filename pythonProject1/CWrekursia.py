# Рекурсия
# def elevator(n):
#     if n == 0:
#         print('Вы на 0 этаже')
#         return
#     print('-> ', n)
#     elevator(n - 1)
#     print(n, end=' ')
#
#
# n1 = int(input('На каком вы этаже: '))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# def sum_list(lst):
#     if len(lst) == 1:  #  Базовый случай
#         print(lst)
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = '0123456789'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(356, 2))


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
#
#
# def count_items(item):
#     count = 0
#     for i in item:
#         if isinstance(i, list):
#             count += count_items(i)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# print(isinstance(names, list))
# print(len(names))


# def coutn_items(item_list):
#     count = 0
#     for i in item_list:
#         if isinstance(i, list):
#             for j in i:
#                 if isinstance(j, list):
#                     for k in j:
#                         count += 1
#                 else:
#                     count += 1
#         else:
#             count += 1
#     return count
#
#
#
#
# print(coutn_items(names))

# def union(s):
#     if not s:  # s == []
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(union(names))

# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == ' ':
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove('Hello\tWorld'))


# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos = pos + 1
#
#     return found
#
#
# # lst = [1, 2, 3, 444, 52, 35, 78, 99, 42]
# lst = [1, 2, 3, 4, 5, 6, 13, 44, 55, 78]
# print(seq_search(lst, 8))
# print(seq_search(lst, 35))

# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midlpoint = (first + last) // 2
#         if s[midlpoint] == item:
#             found = True
#         else:
#             if item < s[midlpoint]:
#                 last = midlpoint - 1
#             else:
#                 first = midlpoint + 1
#
#     return found
#
#
# lst = [1, 2, 3, 4, 5, 6, 13, 44, 55, 78]
# print(binary_search(lst, 8))
# print(binary_search(lst, 3))

#
# import random as r
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [r.randint(1, 99) for i in range(10)]
#
# bubble(a)
#
#
#
# def bubble2(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] < array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [r.randint(1, 99) for i in range(10)]
#
#
#
# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos = pos + 1
#
#     return found
#
#
# b1 = [5, 9, 6, 7]
# b2 = [3, 11, 8]
# b3 = [2, 4]
# b4 = [10, 1, 12]
# lst = b1 + b2 + b3 + b4
# t = int(input('1 - сортировка по убыванию\n2 - сортировка по возрастанию'))
# if t == 1:
#     bubble2(lst)
# else:
#     bubble(lst)
# print(lst)
# print(seq_search(lst, int(input('->'))))
#
# def mer(s):
#     n = len(s)
#     if n < 2:
#         return s
#
#     l = mer(s[:n // 2])
#     r = mer(s[n // 2:n])
#     print(l)
#     print(r)
#
#     i = j = 0
#     res = []
#
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j < len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] < r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#     return res
#
# array = [9,5,3,6]
# print(array)
# array = mer(array)
# print(array)


# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#         print(gap, 'Список: ', s)
#         gap //= 2
#
#     return s
#
#
# a = [10, 44, 26, 14, 67, 21, 9, 87]
# print(a)
# shell_sort(a)
# print(a)


# f = open(r"D:\pythonProject4\text.txt", "r")
# print(f.read(3))
# print(f.read())
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# print(*f)
# print(f)
# f = open("text.txt", "r")
# try:
#     print(f.read())
# finally:
#     f.close()
# f = open("test.txt", "r")
# print(f.read())
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# print(f.readlines(16))
# t = f.readlines()
# print(t)
# print("в документе", len(t), "строк")
# count = 0
# for line in f:
#     count += 1
# print(count)
# f.close()
# f.writelines(lines)
# f = open('xyz.txt', 'a')
# # print(f.write('New text.'))
# lst = [str(i) + str(i-1) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + "\t")
# f.close()
# import codecs
# my_file = open("text2.txt", "w")
# my_file.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# my_file.close()
# my_file = open("text2.txt", "r")
# read_file = my_file.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == "изменить строку в списке;\n":
#         read_file[i] = "Hello World\n"
# print(read_file)
# my_file.close()
# my_file = open("text2.txt", "w")
# my_file.writelines(read_file)
# my_file.close()

# f = open('text.txt', 'r+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# print(f.read(3))
# print(f.tell())  # 3
# print(f.seek(1)) # 1
# print(f.read())
# print(f.tell())
# f.close()

# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789'))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:6])
#
# file_name = 'res_1.txt'
# lst = [3.4, 4.44, 2.222, 12.44, 3.3, 7.65]
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
#
#
# with open(file_name, 'w') as d:
#     d.write(get_line(lst))
#
# print('Done!')
#
# with open('res_1.txt', 'r') as j:
#     file_lst = j.read().split()
#
# file_lst = list(map(float, file_lst))
# print(file_lst)
# print(len(file_lst))


# def find_in_file(file_name):
#     max_l = 0
#     temp_res = []
#     res = []
#     c = 0
#     with open(file_name, "r", encoding='utf-8') as new_file:
#         temp_file = new_file.read().split()
#         for i in temp_file:
#             temp_res.append(len(i))
#             if len(i) > max_l:
#                 max_l = len(i)
#         for j in temp_res:
#             if j == max_l:
#                 res.append(temp_file[c])
#             c += 1
#     return res
#
#
# print(find_in_file("rab.txt"))
#
#
#
# file_name = 'res_1.txt'
# lst = ['один', 'два', 'три', 'четыре', 'пять', 'шесть!']
#
# with open(file_name, 'w', encoding='utf-8') as f:
#     f.write(' '.join(lst))
#
#
# def open_file_and_find_max(file):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         file_lst = f.read().split(' ')
#         max_len = max(len(i) for i in file_lst)
#         new_lst = []
#         for i in file_lst:
#             if len(i) == max_len:
#                 new_lst.append(i)
#         return new_lst
#
#
# print(open_file_and_find_max(file_name))

# with open('rab.txt', 'r', encoding='utf-8') as f:
# #         lst = f.read().split()
# #         m = max(len(i) for i in lst)
# #         print([i for i in lst if len(i) == m])


# text = "Строка№1\nСтрока№2\nСтрока№3\nСтрока№4\nСтрока№4\nСтрока№5\nСтрока№6\nСтрока№7\nСтрока№8\nСтрока№9\nСтрока№10\n"
# with open('one.txt','w')as f:
#     f.write(text)
#
# read_file = 'one.txt'
# write_file = "two.txt"
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', "Линия - ")
#         fw.write(line)
#
# with open(write_file, 'r') as fr:
#     for line in fr:
#         print(line)

# os
# os.path

import os

# print('Текущая директроия', os.getcwd())  # Ввзвращает текущую директорию (там где *.py)
# print(os.listdir('..'))  # Возвращает список директорий и файлов, находящихся в текущей директории(по умолчанию)
# # или в директории по указаному пути
# os.mkdir('folder') #  создаёт директорию по указаному пути

# os.makedirs('folder1/folder2/folder3')  # создаст конечную директорию и также промежуточные папки, если их не было
# os.remove('two.txt')  # Удаляет файл
# os.rename('folder', 'test')  #  переименовывает файл или папку
# os.rename('rb.txt', 'folder1/folder2/ts1.txt')
# os.renames('test.txt', 'text/new_text/tx.txt')  # переименовывается и перемещает файл, создавая промежуточные дериктории
# os.rmdir('test')  #  удаляет пустую папку. Если папка не существует или она не пустая, будет ошибка

# Возвращает имена объектов в дереве папок, обходя это дерево сверху вниз(topdown=True)
# cнизу вверх (topdown=False)
# for root, dirs, files in os.walk("folder1", topdown=False):
#     if len(dirs) == 0 and len(files) == 0:
#         print("Deriktoriya " + root + " udalena")
#         os.rmdir(root)

# for root, dirs, files in os.walk("folder1", topdown=False):
#     if not  os.listdir(root):
#         os.rmdir(root)
#         print(f"Директория {root} удалена.")

import os.path

# print(os.path.split(r"D:\pythonProject4\folder1\folder2\folder0\folder3\folder4\folder5\file.txt"))
# # разбивает путь на кортеж (head, tail)
# print(os.path.dirname(r"folder5\file.txt"))
# # возаращает имя директории
# print(os.path.basename(r"folder5\file.txt"))
# # возващает имя файла
# print(os.path.join('files', r"D:\pythonProject4", "/folder1", "folder2", "file.txt"))
# # соединяет один или несколько компонентов пути с учетом особенностей OS

# dirs = ['Works/F1', 'Works/F2/F21']
# for dir1 in dirs:
#     os.makedirs(dir1)
#
# files = {
#     'Works': ['w.txt'],
#     r'Works\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Works\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for dir1, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir1,file)
#         print(file_path)
#         open(file_path, 'w').close()
#
# file_with_text = [r'Works\w.txt', r'Works\F1\f12.txt', r'Works\F2\F21\f211.txt', r'Works\F2\F21\f212.txt']
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f'some saple text for {file} file')
#
#
# def print_tree(root, topdown):
#     print(f'Обход {root} {"сверху вниз" if topdown else "снизу вверх"}')
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print('-' * 50)
#
#
# print_tree('Works', topdown=False)
# print_tree('Works', topdown=True)

# print(os.path.exists(r'C:\Users\dotap\PycharmProjects\pythonProject1\Works\w.txt'))
# # проверяет путь на существование (True - если путь существует)
#
# print(os.path.getctime(r'C:\Users\dotap\PycharmProjects\pythonProject1\Works\w.txt'))
# # возвращает время создания файла
# print(os.path.getatime(r'C:\Users\dotap\PycharmProjects\pythonProject1\Works\w.txt'))
# # возвращает время последнего доступа файла
# print(os.path.getmtime(r'C:\Users\dotap\PycharmProjects\pythonProject1\Works\w.txt'))
# # возвращает время изменения последнего файла
# print(os.path.getsize(r'C:\Users\dotap\PycharmProjects\pythonProject1\Works\w.txt'))
# # возвращает размер файла в байтах

import time

# path = r'res_1.txt'
# size = os.path.getsize(path)
# kb = size // 1024
# atime = os.path.getatime(path)
# mtime = os.path.getmtime(path)
# print('Размер: ', kb, 'KB')
# print('Дата последнего использования: ', time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(atime)))
# print('Дата последнего редактирования: ', time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(mtime)))
#

# print(os.path.normcase('C:/Users/dotap/PycharmProjects'))
# # нормализует регистр пути и слеши
# print(os.path.relpath(r'C:\Users\dotap\PycharmProjects\pythonProject1\Works\w.txt'))
# # возращает относительный путь
# print(os.path.isfile(r'C:\Users\dotap\PycharmProjects\pythonProject1\Works\w.txt'))
# # возвращает True, если концом пути является существующий файл
#
# print(os.path.isdir(r'C:\Users\dotap\PycharmProjects'))
# # возвращает True, если концом пути является существующая папка

#
# print('Hi, i add new info'
#       '')


