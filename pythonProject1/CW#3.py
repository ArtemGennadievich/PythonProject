# day = int(input('Введите дни недели: '))
# # if (day >= 1) and (day <= 5) :
# if 1 <= day <= 5:
#     print('Рабочий день - ', end='')
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день -", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели нету")

# day = int(input('Введите дни недели: '))
# # if (day >= 1) and (day <= 5) :
# if 1 <= day <= 12:
#     print('Месяц - ', end='')
#     if day == 1:
#         print("Январь")
#     if day == 2:
#         print("Февраль")
#     if day == 3:
#         print("Март")
#     if day == 4:
#         print("Апрель")
#     if day == 5:
#         print("Май")
#     if day == 6:
#         print("Июнь")
#     if day == 7:
#         print("Июль")
#     if day == 8:
#         print("Август")
#     if day == 9:
#         print("Сентябрь")
#     if day == 10:
#         print("Октябрь")
#     if day == 11:
#         print("Ноябрь")
#     if day == 12:
#         print("Декабрь")
# else:
#     print("Такого дня недели нету")

# a, b = 10, 20
# print("a == b" if a == b else "a > b" "a" if a > b else "a < b")

# b = 3
# a = 0
# print("На ноль делить нельзя" if a == 0 else b / a)

# try:
#     n = int(input("Введите целое число: "))
#     print((n * 2))
# except ValueError:
#     print("Неправильный ввод")

# try:
#     m = int(input("Введите делимое: "))
#     n = int(input("Введите делитель: "))
#     print((m / n))
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
# else:
#     print("Все нормально. Вы ввели чмсла", n, "and", m)
# finally:
#     print("Конец программы")

# except (ValueError, ZeroDivisionError):
# print("Нельзя вводить строки")
# print("Нельзя делить на ноль")

# n = input("1 Ch = ")
# m = input("2 Ch = ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
#     m = str(m)
# finally:
#     print(n + m)

# i = 0
# while i < 21:
#     print("i = ", i)
#     i += 2

# a = int(input("ch ="))
# c = 0
# while c < a:
#     print("*", end="")
#     c += 1

# n = input("Введите полное число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число")
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# n = input("Введите 1 полное число: ")
# b = input("Введите 2 полное число: ")
# while type(n) != int and type(b) != int and :
#     try:
#         n = int(n)
#         b = int(b)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите 1 полное число: ")
#         b = input("Введите 2 полное число: ")
# if n % 3 == 0:
#     n
#     print("Сумма целых нечетных чисел",)
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 2:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")



# while True:
#     n = int(input('Введите положительное число'))
#     if not n:
#         break
#     n = int(f)
#     f *= f
#     print(n)


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен")

# i = 1
# while i < 5:
#     print("Внешние цикл: i=", i)
#     j = 1
#     while j < 4:
#         print("Внутрений цикл: j =", j)
#         j += 1
#     i += 1
i = 1
while i < 10:
    j = 1
    while j < 10:
        print(i, "*", j, "=", i*j, "\t\t", end="")
        j += 1
    print()
    i += 1