# a = 534566346
# print(a)
# print(type(a))


# print(6/2)
# print(6//2)
#
#
# a = 5
# b = 7
# c = 3
# summ = 5 + 7 + 3
# Um = 5 * 7 * 3
# sa = (5 + 7 + 3)
# saw = sa/3
# print(summ)
# print(Um)
# print(saw)

# num = 6 + 4 * 5 ** 2 + 7
# print(num)

# num = 10
# num += 5
# print(num)


# num = 9753
# print("Исходное число:", num)
# res = (num % 10) * 1000
# num = num // 10
# res += (num % 10) * 100
# num = num // 10
# res += (num % 10) * 10
# num = num // 10
# res += num % 10
# # print("num", num)
# print("Обратное число:", res)

# num1 = "2"
# num2 = 3
# print(int(num1) + num2)
# print(num1 + str(num2))


# print(int(3.8))
# print(round(3.896, 2))

# a = 5 / 3
# print(a)
# print(round(a, 2))

# a = "5.2"
# b = 10
# print(float(a) + b)

# a = 1
# # b = 2
# # print("a:", a, "b:", b)
# #
# # name = "Ivan"
# # age =  32
# # print("My name:", name, '.Me', age, 'age. ', sep='--', end="\n\n")
# # print("Я учу Python")

# name = "Igor"
# age = 44
# grade = 9.2
# print("It's %s, %d. Level: %.1f" % (name , age , grade))

# print("This is a {0}. It's {1}.".format("ball", "red"))

# name = input("Ваше имя: ")
# city = input("Ваш город: ")
# print("Вас зовут {0}.Ваш город {1}".format(name, city))

# n = input("Введите число: ")
# print(int(n) ** 2)
# a = input("Введите 1 число: ")
# b = input("Введите 2 число: ")
# a = input("1 число")
# b = input("2 число")
# c = input("3 число")
# d = input("4 число")
# sum1 = a + b
# sum2 = c + d
# delet = int(sum1) / int(sum2)
# print(round(delet, 2))

# b1 = True
# b2 = False
#
# print(b1 + 5)
# print(b2 + 5)
#
# print(bool("Python"))
# print(bool(""))
# print(bool(" "))
# print(bool(0))
# print(bool(1))
# print(bool(15))
# print(bool(-15))
# print(bool(0.1))
# print(bool(False))
# print(bool(None))


# test = None
# print(test)
# print(test is None)
# test = 5
# print(test)
# print(test is None)


# print("привет" > "Привет")
# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4+3)
# print(3 * 3 <= 7 >= 2)
#
# a = 10
# b = 5
# c = a == b
# print(a, b, c)
#
# print(5 - 3 == 2 and 1 + 3 == 4)
# print(5 - 3 == 2 or 1 + 3 == 5)
# print(not 9 - 5)
# print(not 9 - 9)

# a = (0 or 1) and (0 or 1)
# print(a)
# b = 0 or 1 and 0 or 1
# print(b)
# c = (a or 1) and (b or 0)
# print(c)

# if логическое выражение:
#     выражение

# cnt = 9
# if cnt < 10:
#     cnt += 1
#     print(cnt)
# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещ


# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("b == a")

a = int(input("Введите 1 сторону: "))
b = int(input("Введите 2 сторону: "))
c = int(input("Введите 3 сторону: "))

if a == b or a == c or c == b:
    print("Треугольник равнобедренный")
else:
    print("Треугольник неравнобедренный")
