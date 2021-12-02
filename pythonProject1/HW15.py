def first_func(a):
    def wrap(b):
        return a * b

    return wrap


res = first_func(2)
print(res(15))
print(res(20))
res = first_func(3)
print(res(15))
print(res(20))

sum3 = lambda x: lambda y: lambda z: x + y + z
print('\n', 'sum3(2)(4)(6) =', sum3(2)(4)(6))

lst = [{'name': 'Jennifer', 'final': 95},
       {'name': 'David', 'final': 92},
       {'name': 'Nikolas', 'final': 98}]
print('\n', lst)
lst_sort = sorted(lst, key=lambda item: item['final'], reverse=True)
print(lst_sort)

lst2 = [{'name': 'Jennifer', 'final': 95},
        {'name': 'David', 'final': 92},
        {'name': 'Nikolas', 'final': 98}]

lst_max = max(lst2, key=lambda item: item['final'])
lst_min = min(lst2, key=lambda item: item['final'])
print('\n', lst_max)
print(lst_min)

input()