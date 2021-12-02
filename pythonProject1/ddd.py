# Декораторы

# def hello():
#     return 'Hello, i an func "hello"'
#
#
# def super_func(func):
#     print('Hello, i an func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, i an func "hello"'
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# @my_decorator
# def func_test():
#     print('Hello, i an func "hello"')
#
#
# func_test()

# def my_decorator(func):
#     def func_wrapper(n, m):
#         print('Code before')
#         func(n, m)
#         print('Code after')
#
#     return func_wrapper
#
#
# @my_decorator
# def func_test(a, b):
#     print(a * b)
#
#
# func_test(2, 5)


# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return 'text'
#
#
# print(hello())


# def kolichestvo(hh):
#     h = 0
#
#     def wen():
#         nonlocal h
#         h = h + 1
#         return hh() + str(h)
#
#     return wen
#
#
# @kolichestvo
# def text():
#     return "Hello\nВызов функции: "
#
#
# print(text())
# print(text())
# print(text())

def args_decorator(fn):
    def wrap(arg1, arg2):
        print('Данные: ', arg1, arg2)
        fn(arg1, arg2)
    return wrap


@args_decorator
def print_full_name(first, last):
    print('My name is', first, last)


print_full_name('Igor', 'lavrov')
