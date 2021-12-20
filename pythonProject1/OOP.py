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
#     # coordX = property(__get_coords_x, __set_coords_x, __del__coords_x)
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


class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('.'))
        day1 = cls(day, month, year)
        return day1

    @staticmethod
    def is_date_valid(date_as_string):
        if date_as_string.count('.') == 2:
            day, month, year = map(int, date_as_string.split('.'))
            return day <= 31 and month <= 12 and year <= 3999

    def string_to_db(self):
        return f"{self.year}-{self.month}-{self.day}"


# d = '16.12.2021'
# # day, month, year = map(int, d.split('.'))
# # print(day, month, year)
# d1 = Date()
#
# date = Date.from_string('16.12.2021')
# print(date.string_to_db())

dates = [
    '12.12.2122',
    '30-11-2012',
    '02.11.2023',
    '32.23.2222'
]
for i in dates:
    if Date.is_date_valid(i):
        date = Date.from_string(i)
        db = date.string_to_db()
        print(db)
    else:
        print("Не правильная дата или формат с датой")


