# # class Point3D:
# #     pass
#
#
# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coorsd(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# # print(Point.__doc__)
# # print(Point.__name__)
# # print(dir(Point))
#
# t = Point()
#
# # print(type(t))
# # print(type(t) == Point)
# # print(isinstance(t, Point))
# # print(isinstance(t, Point3D))
#
# # t.x = 5
# # t.y = 10
# # t.z = 20
# t.set_coorsd(5, 10)
# # print(t.x, Point.x )
# # # Point.x = 100
# # # print(t.x, t.y)
# # # print(id(t))
# # # print(id(Point))
# # #
# # # print(t.__dict__)
# # #
# # # print(getattr(t, 'x'))
# # setattr(t, 'z', 7)
# # print(hasattr(t, 'x'))
# # print(hasattr(t, 'z'))
# # # p2 = Point()
# # # print(p2.__dict__)
# # delattr(t, 'z')
# # print(t.__dict__)
# Point.set_coorsd(t, 6, 4)

# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'Street, house'
#
#     def print_info(self):
#         print('Персональные данные'.center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}'
#               f'\nСтрана: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, name, birthday, phone, country, city, address):
#         self.name = name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):  # Получаем имя
#         return self.name
#     #
#     # def get_birthday(self):
#     #
#     # def get_phone(self):
#     # def get_country(self):
#     # def get_city(self):
#     # def get_address(self):
#     # def set_birthday(self, birthday):
#     #     self.birthday = birthday
#     # def set_phone(self):
#     # def set_country(self):
#     # def set_city(self):
#     # def set_address(self):
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля', '23.05.1986', '45-46-98', 'Россия', 'Москва', 'Чистопрудный бульвар 1А')
# h1.print_info()
# h1.set_name('Irina')
# print(h1.get_name())


# class Person:
#     skill = 10  # квалисификация сотрудника
#
#     def print_info(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print(f"Данные сотрудника: {self.name} {self.surname}")
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f"Квалисификация сотрудника: {self.name}:", self.skill)
#
#
# p1 = Person()
# p1.print_info("Viktor", 'Reznik')
# p1.add_skill(3)
# p2 = Person()
# p2.print_info("Anna", 'Dolgix')
# p2.add_skill(2)

# def sum_args(a,b):
#     print(a + b)
#
#
# sum_args(5, 2)
# sum_args("Hello", " world")


# __магический метод__
# Специальные методы
# конструктор __new__
# инициализатор __init__
# дестркутор  __del__

# class Point:

# def __new__(cls, *args, **kwargs):
#     print('Costructor')
#     return super().__new__(cls)

#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_val(x) and Point.check_val(y):
#             self.x = x
#             self.y = y
#         else:
#             print('Координаты должны быть числами')
#
#     def get_corods(self):
#         return self.x, self.y
#
#     # def __del__(self):
#     #     print('Udalenie ekzenpliara: ' + self.__class__.__name__)
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# p2 = Point(2, 3)
# print(p2.__dict__)
# print(p1.count)
# print(p1.count)
# p1.set_coords(2, 3)
# p1.set_coords(2, '3')
# print(p1.get_corods())
# p2 = Point()
# print(p2.__dict__)
# p3 = Point(2)
# print(p3.__dict__)
# Point.__init__(p1, 20)
# print(p1.__dict__)
# del p1
# print(p1.x)

# class Robot:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('Инициализация робота: ', self.name)
#         Robot.count += 1
#
#     def __del__(self):
#         print(self.name, 'выключается!')
#         Robot.count -= 1
#
#         if Robot.count == 0:
#             print(self.name, 'был последний')
#         else:
#             print("Работающий роботов осталось:", Robot.count)
#
#     def say_hi(self):
#         print('Приветствую! Меня зовут', self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print('Численность роботов: ', Robot.count)
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print('Численность роботов: ', Robot.count)
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы закончили свою работу.Давайте их выключим")
# del droid1
# del droid2
#
# print('Численность роботов', Robot.count)
#
# class Point:
#     WIDTH = 5
#     z = 110
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __getattr__(self, item):
#         return f"В классе {__class__.__name__} отсуствует атрибут: {item}"
#
#     # def __getattribute__(self, item):
#     #     if item == '_Point__x':
#     #         return "Закрытая переменная"
#     #     else:
#     #         return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key == "z":
#             raise AttributeError
#         else:
#             self.__dict__[key] = value
#
#     def check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_val(x) and Point.check_val(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координаты должны быть числами')
#
#     def set_coords_x(self, x):
#         if Point.check_val(x) and Point.check_val(x):
#             self.__x = x
#
#     def set_coords_y(self, y):
#         if Point.check_val(y) and Point.check_val(y):
#             self.__y = y
#
#     def get_corods(self):
#         return self.__x, self.__y
#
#     def area(self):
#         return (self.__x * self.__y) + Point.z
#
#
# p1 = Point(5, 10)
# print(p1._Point__x)
# print(p1.__x)
# p1.WIDTH = 10
# p1.z = 100
# print(p1.area())
# print(p1.area())
# print(p1.zzz)
# print(p1.get_corods())
# p1.set_coords(2, 3)
# print(p1.get_corods())
# p1.set_coords_x(100)
# p1.set_coords_y(1)
# print(p1.get_corods())
# print(p1.__x, p1.__y)
# p1.x = 100
# p1.y = 'abd'
# print(p1.__x, p1.__y)

# Инкапсуляция
# x - public
# _x - protrcted
# __x - private

# print(p1.__dict__)

#
# p1._Point__x = 111
# print(p1.__dict__)

# import math
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def set_length(self, length):
#         self.__length = length
#
#     def set_width(self, width):
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def square(self):
#         return self.__width * self.__length
#
#     def perimeter(self):
#         return (self.__length * self.__width) * 2
#
#     def hypo(self):
#         return math.sqrt(self.__length ** 2 + self.__width ** 2)
#
#     def art(self):
#         for i in range(self.__length):
#             print(self.__width * "*")
#
# res1 = Rectangle(3, 9)
# print('Ширина прямоугольника', res1.get_width())
# print('Длина прямоугольника', res1.get_length())
# print('Площадь прямоугольника', res1.square())
# print('Периметр прямоугольника', res1.perimeter())
# print('Гипотянуза прямоугольника', res1.hypo())
# res1.art()

# class Point:
#     __slots__ = ['__x', '__y', 'z', '__dict__']
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# print(p1.__dict__)
# print(Point.__dict__)

# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def __get_coords_x(self):
#         print("Вызов __get_coords_x")
#         return self.__x
#
#     def __set_coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             raise ValueError("Не верный формат данных")
#
#
#     def __del__coords_x(self):
#         print('Удаление свойства')
#         del self.__x
#
#     coordX = property(__get_coords_x, __set_coords_x, __del__coords_x)
#
#
#
# p1 = Point(5, 10)
# p1.coordX = 100
# print(p1.coordX)
# del p1.coordX
# p1.coordX = 7
# print(p1.coordX)
# print(p1.__dict__)

# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     @property  # getter
#     def coords_x(self):
#         print("Вызов __get_coords_x")
#         return self.__x
#
#     @coords_x.setter  #setter
#     def coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             raise ValueError("Не верный формат данных")
#
#     @coords_x.deleter  #deleter
#     def coords_x(self):
#         print('Удаление свойства')
#         del self.__x
#
#     # coordX = property(__get_coords_x, __set_coords_x, __del__coords_x)
#
#
# p1 = Point(5, 10)
# p1.coords_x = 100
# print(p1.coords_x)
# # del p1.coordX
# # p1.coordX = 7
#
# print(p1.coords_x)


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# w = KgToPounds(12)
# print(w.to_pound())
# w.kg = 41
# print(w.to_pound())

#
# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.get_count())
# print(p1.get_count())
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print((Change.inc(10)), Change.dec(10))
# q = Change()
# print(q.dec(5))
# print(q.inc(5))

#
# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         if a > b and a > c and a > d:
#             return a
#         if b > a and b > c and b > d:
#             return b
#         if c > a and c > b and c > d:
#             return c
#         if d > a and d > b and d > c:
#             return d
#
#     @staticmethod
#     def min(a, b, c, d):
#         if a < b and a < c and a < d:
#             return a
#         if b < a and b < c and b < d:
#             return b
#         if c < a and c < b and c < d:
#             return c
#         if d < a and d < b and d < c:
#             return d
#
#     @staticmethod
#     def srednee(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factorial(a):
#         fac = 1
#         for i in range(1, a + 1):
#             fac *= i
#         return fac
#
#
# print(Numbers.max(1, 2, 3, 4))
# print(Numbers.min(1, 2, 3, 4))
# print(Numbers.srednee(1, 2, 3, 4))
# print(Numbers.factorial(4))


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         day1 = cls(day, month, year)
#         return day1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# # d = '16.12.2021'
# # # day, month, year = map(int, d.split('.'))
# # # print(day, month, year)
# # d1 = Date()
# #
# # date = Date.from_string('16.12.2021')
# # print(date.string_to_db())
#
# dates = [
#     '12.12.2122',
#     '30-11-2012',
#     '02.11.2023',
#     '32.23.2222'
# ]
# for i in dates:
#     if Date.is_date_valid(i):
#         date = Date.from_string(i)
#         db = date.string_to_db()
#         print(db)
#     else:
#         print("Не правильная дата или формат с датой")


# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     siffix = 'RUB'
#     siffix_usd = 'USD'
#     siffix_euro = 'EUR'
#
#     def __init__(self, two_name, number, percent, value=0):
#         self.two_name = two_name
#         self.number = number
#         self.percent = percent
#         self.value = value
#         print(f'Счёт #{self.number} принадлежащий {self.two_name} был открыт.')
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f'Счёт #{self.number} принадлежащий {self.two_name} был закрыт.')
#
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_euro_rate(cls, rate):
#         cls.rate_euro = rate
#
#     def convert_to_usd(self):
#         usd_value = self.convert(self.value, Account.rate_usd)
#         print(f'Состояние счёта: {usd_value} {Account.siffix_usd}')
#
#     def convert_to_euro(self):
#         euro_value = self.convert(self.value, Account.rate_euro)
#         print(f'Состояние счёта: {euro_value} {Account.siffix_euro}')
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.value} {Account.siffix}')
#
#     def print_info(self):
#         print('Информация о счёте:')
#         print("-" * 20)
#         print(f'#{self.number}')
#         print(f'Владелец: {self.two_name}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print("-" * 20)
#
#     def get_sur_name(self, name):
#         self.two_name = name
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению у вас {val} {Account.siffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.siffix} было успешно снято')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.siffix} было успешно добавлено')
#         self.print_balance()
#
#
#
# acc = Account('Долгих', 12345, 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_euro()
# Account.set_usd_rate(2)
# print()
# Account.set_euro_rate(3)
# acc.convert_to_usd()
# acc.convert_to_euro()
# print()
# acc.get_sur_name('Дюма')
# acc.print_info()
# acc.add_percent()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'{self.x},{self.y}'
#
#
# # print(isinstance(Point, object))
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int or float = 1):
#         print('Инициализатор базового класса Prop')
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.width = width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f'Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}')
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f'Рисование прямоугольника: {self.sp}, {self.ep}, {self.color}, {self.width}')
#
# line = Line(Point(1, 2), Point(10, 20))
# print(line.__dict__)
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# #
# #
# class Rectangle(Figure):
#     def __init__(self, width, height, color, border):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#         self.__border = border
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError('Значение ширины должно быть больше нуля')
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, w):
#         if w > 0:
#             self.__height = w
#         else:
#             raise ValueError('Значение высоты должно быть больше нуля')
#
#     # def border_new(self, b):
#     #     self.__border = b
#
#     def area(self):
#         # return self.__color
#         return self.width * self.height
#
#
# rect = Rectangle(10, 20, 'green', 30)
# print(rect.area())


# class Liquid:  # Жидкость
#     def __init__(self, name, density):
#         self._name = name
#         self._density = density  # плотность жидкости
#
#     def edit_density(self, val):  # изменение плотности
#         self._density = val
#
#     def calc_v(self, m):  # вычисление объёма жидкости
#         res = m / self._density
#         print(f'Объём {m} кг {self._name} равен {res} m^3')
#         return res
#
#     def calc_m(self, v): # вычесление массы жидкости соотвествующее заданному значению
#         res = v * self._density
#         print(f'Вес {v} m^3 {self._name} равен {res} кг')
#         return res
#
#     def print_info(self):
#         print(f'Жидкость {self._name} (плотность = {self._density} kg/m^3).')
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength  # крепость
#
#     def edit_strength(self, val): # изменение крепости
#         self.strength = val
#
#
# a = Alcohol('Wine', 1064.2, 14)
# a.print_info()
# a.edit_density(1000)
# a.print_info()
# a.calc_v(300)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'{self.x}, {self.y}'
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         else:
#             return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         else:
#             return False
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print('Координаты должны быть числами')
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp},{self._ep},{self._color}, {self._width}")
#
#     def set_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print('Координаты должны быть целыми числами')
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30.2, 40), Point(100, 200))
# line.draw_line()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f'Прямоугольник:\nШирина: {self.width}\nВыста: {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print('Фон:', self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print('Рамка:', self.border)
#
#
# shape1 = RectFon(400, 200, 'yellow')
# shape1.show_rect()
# shape2 = RectBorder(600, 300, '1px solid red')
# shape2.show_rect()


# class Liquid:  # Жидкость
#     def __init__(self, name, density):
#         self._name = name
#         self._density = density  # плотность жидкости
#
#     def edit_density(self, val):  # изменение плотности
#         self._density = val
#
#     def calc_v(self, m):  # вычисление объёма жидкости
#         res = m / self._density
#         print(f'Объём {m} кг {self._name} равен {res} m^3')
#         return res
#
#     def calc_m(self, v): # вычесление массы жидкости соотвествующее заданному значению
#         res = v * self._density
#         print(f'Вес {v} m^3 {self._name} равен {res} кг')
#         return res
#
#     def print_info(self):
#         print(f'Жидкость {self._name} (плотность = {self._density} kg/m^3), ', end=' ' )
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength  # крепость
#
#     def edit_strength(self, val): # изменение крепости
#         self.strength = val
#
#     def calc_v(self, m):  # переопределение вычисление объёма жидкости
#         v = super().calc_v(m)
#         v_alc = m * self.strength
#         print(f'Объём алкоголя в {m} кг {self._name} сотсовляет {v_alc} m^3.')
#         return v, v_alc
#
#     def calc_m(self, v):  # переопределение вычесление массы жидкости соотвествующее заданному значению
#         m = super().calc_v(v)
#         m_alc = v * self.strength
#         print(f'Вес алкоголя в {v} кг {self._name} сотсовляет {m_alc} m^3.')
#         return m, m_alc
#
#     def print_info(self):
#         super().print_info()
#         print(f', крепость = {self.strength:.0%}')
#
#
#
# a = Alcohol('Wine', 1064.2, 14)
# a.print_info()
# a.edit_density(1000)
# a.print_info()
# a.calc_v(300)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)
#
# a.print_info()

