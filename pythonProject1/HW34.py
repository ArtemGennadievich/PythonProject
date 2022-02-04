# class Person:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, surname, forename=None):
#         lst = []
#         lst2 = []
#         lst3 = []
#         if forename is None:
#             for i in self.func:
#                 lst.append(i[0])
#             lst.sort()
#             return lst
#         else:
#             for i in self.func:
#                 lst2.append(i[0])
#                 lst3.append(i[1])
#             lst2.sort()
#             lst3.sort()
#             return lst2, lst3
#
#
#
# pers = Person([
#     ["Иванов", 'Игорь', 28],
#     ["Иванов", 'Иван', 28],
#     ["Петров", 'Степан', 28],
#     ["Сидоров", 'Игорь', 28],
#     ["Петров", 'Анатолий', 28]
# ])
# print(pers('surname', 'ff'))


class Person:
    def __init__(self, func):
        self.func = func

    def __call__(self, surname, forename=None):
        lst = []
        lst2 = []
        lst3 = []
        ver_list = []
        end_list = []
        count = -1
        if forename is None:
            for i in self.func:
                lst.append(i[0])
            lst.sort()
            return lst
        else:
            for i in self.func:
                lst2.append(i[0])
                lst2.sort()
            count1 = []
            count2 = 0
            ver = set(lst)
            for i in lst2:
                count += 1
                for j in ver:
                    if i == j:
                        ver_list.append(count)
                        if len(ver_list) > 1:
                            for i in ver_list:
                                end_list.append(i)
                            ver_list.clear()
            print(end_list)
            for i in lst2:
                for j in end_list:
                    print(i,j)
                    if lst2[count2] == lst2[j]:
                        count1.append(j)
                        print('dd',count1)
                lst3.append(i[1])
            lst2.sort()
            lst3.sort()
            return lst2, lst3


pers = Person([
    ["Иванов", 'Игорь', 28],
    ["Иванов", 'Иван', 28],
    ["Петров", 'Степан', 28],
    ["Сидоров", 'Игорь', 28],
    ["Петров", 'Анатолий', 28]
])
print(pers('surname', 'fd'))
