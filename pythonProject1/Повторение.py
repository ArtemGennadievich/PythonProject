# i = 0
# c = 0
# a1 = int(input('Shislo: '))
# count = 0
# m = a1
# while m > 0:
#     count = count + 1
#     m = m // 10
# while i < count:
#     b = int(a1 % 10)
#     a1 /= 10
#     if c == 0:
#         c = (c + 1)
#     else:
#         c = (c + b) * 10
#     i += 1
#     if i == count:
#         print("Результат: ", int(c / 10))

# n = int(input('Enter a number : '))
# reverse = 0
# while n != 0:
#     r = int(n % 10)
#     reverse = reverse * 10 + r
#     n = int(n / 10)
# print(reverse)


z = ['a', 'b', 'a', 'c', 'b', 'a', ]
print(set(z))
g = [z[i] for i in range(len(z)) if i == z.index(z[i])]
print(g)

# my_list = [3, 5, 2, 1, 4, 4, 1]
# my_set = set(my_list).intersection_update()
# print(my_set)
# opt = [item for item in set(my_list) if my_list.count(item) > 1]
# print(opt)
# for i in set(my_list):
#     if my_list.count(i) > 1:
#         print(i, my_list.index(i))



