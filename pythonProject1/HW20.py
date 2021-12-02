import random
negative_number = []


def search_negative_numbers(lst):
    if not lst:
        return len(negative_number)
    if lst[0] < 0:
        negative_number.append(lst[0])
        return lst[0] + search_negative_numbers(lst[1:])
    else:
        return lst[0] + search_negative_numbers(lst[1:])


print('n =', search_negative_numbers([-2, 3, 8, -11, -4, 6]))


def binary_search(s, item):
    first = 0
    last = len(s) - 1
    found = False

    while first <= last and not found:
        midlpoint = (first + last) // 2
        if s[midlpoint] == item:
            found = True
        else:
            if item < s[midlpoint]:
                last = midlpoint - 1
            else:
                first = midlpoint + 1

    return found


lstg = [random.randint(1,100) for i in range(10)]
print(lstg)
print(binary_search(lstg, int(input("Введите числа: "))))
