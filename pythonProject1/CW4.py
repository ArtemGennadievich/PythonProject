# kol = int(input("Введите количетсво чисел последовательности"))
# ch = float(input("Введите число"))
# min_ch = ch
# i = 1
# while i < kol:
#     ch = float(input("Введите число: "))
#     if ch < min_ch:
#         min_ch = ch
#     i += 1
# print("Минимальное число: ", ch)

# kol = int(input("Введите количетсво чисел последовательности"))
# ch = float(input("Введите число"))
# max_ch = ch
# sum_ch = ch
# i = 1
# while i > kol:
#     ch = float(input("Введите число: "))
#     sum_ch += ch
#     if ch > max_ch:
#         max_ch = ch
#     i += 1
# print("Минимальное число: ", ch)
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1
# i = 0
# while i < 5:
#     print(" " * i + "*")
#     i += 1

# for  element in collections:
#     print(element)


# for i in 'Hello':
#     print(i)
#
#
# j = 1
# for color in 'red' , 'orange' , 'yellow', 'black', 'blue':
#     print(j, "color:", color)
#     j += 1


# for i in "one", "two", 1, 23, 0.3:
#     print(i)

# for i in range(n):
#     Тело цикла

# range(start, stop, step)

# for i in range(9, 2, -1):
#     print(i, end='')

# a = int(input("Vvod: "))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(11, 101, 11):
#     print(i)

# for i in range(10):
#     print(i, end=" ")
# else:
#     print("\nDone!")
# a = int(input("Weight: "))
# b = int(input("Height: "))
# for i in range(b):
#     print()
#     for j in range(a):
#         print("-", end="")

a = int(input("Weight: "))
b = int(input("Height: "))
for i in range(b):
    for j in range(a):
        if (i == 0 or i == b - 1) or (j == 0 or j == a - 1):
            print('*', end="")
        else:
            print(' ', end="")
    print()

# [результат| цикл | опциональные условия ]
# print([i for i in "hello"])

# print([i ** 3 for i in range(30) if i % 2 == 0])
# sum = [i ** 3 for i in range(30) if i % 2 == 0]
# print(sum)

# a = 56
#
# for i in range(1, 100):
#     b = int(input("Ch: "))
#
#     if b > a:
#         print("Menche")
#     if b == 0:
#         print("Vi vichli")
#         break
#     elif b < a:
#         print("Bolche")
#     elif b == a:
#         print("Win!")
#         print(i)

# Списки

# num = [8, 3, 4, 54, 3]
# print(id(num))
# print(num)
# num[1] = 256
# print(num)
# num[3] += 100
# print(num)
# print(id(num))

# print("Длина списка: ", len(num))

# s = []
# s = [5, 6]
# print(s)

# s = [5] * 6
# print(s)
#
# b = list()
# print(b)

# n = list(range(10, 2, -2))
# print(n)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# c = [i * 3 for i in "list"]
# print(c)\\

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("->"))
# print(a)

# a = [input("->") for i in range(int(input("Количество элементов")))]
# print(a)
# n = list(range(10, 2, -2))
# for i in range(len(n)):
#     print(n[i], end=" ")
#
# print()
# for j in n:
#     print(j, end=" ")

