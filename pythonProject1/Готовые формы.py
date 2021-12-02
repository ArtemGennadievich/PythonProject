while True:
    try:
        print("Бесконечный цикл с возможностью выхода из него c проверкой ошибок")
    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nДля перехода на следующее задание введите 1: \n')
    if t == str(1):
        break


def typed(*args, **kwargs):
    def wraper(fn):
        def wrap(*f_args, **f_kwargs):
            for i in range(len(args)):
                if type(f_args[i]) != args[i]:
                    raise TypeError('Типы данных не соотвествует)')

            for i in kwargs:
                if type(f_kwargs[i]) != kwargs[i]:
                    raise TypeError('Типы данных не соотвествует)')

            return fn(*f_args, **f_kwargs)

        return wrap

    return wraper


@typed(int, int, int)
def typed_fn(x, y, z):
    return x * y * z


@typed(str, str, str)
def typed_fn2(x, y, z):
    return x + y + z


@typed(str, str, z=int)
def typed_fn3(x, y, z='Hello! '):
    return (x + y) * z


print(typed_fn(3, 4, 5))
print(typed_fn(3, 4, 6))
print(typed_fn2('Hello, ', 'world', '!'))
print(typed_fn3('Hello, ', 'world', z=5))


# //////////////////////////////////////////////////////

def args_decorator(tx=None, decorator_text=''):
    def my_decorator(func):
        def wrap(*args):
            print(decorator_text, end='')
            func(*args)

        return wrap

    if tx is None:
        return my_decorator
    else:
        return my_decorator(tx)


# /////////////////////////////////////////////////////
def union(s):
    if not s:  # s == []
        return s
    if isinstance(s[0], list):
        return union(s[0]) + union(s[1:])
    return s[:1] + union(s[1:])


names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
print(union(names))
#//////////////////////////////////////////////////
