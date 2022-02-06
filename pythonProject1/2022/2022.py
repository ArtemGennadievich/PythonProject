# import re
#
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_weight(weight)
#         self.verify_ps(ps)
#         self.__fio = fio
#         self.__weight = weight
#         self.__ps = ps
#         self.__old = old
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Не верный формат ФИО")
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14  *-v-*or old > 100:
#             raise TypeError("Возраст должен быть числом в диапозоне от 14 до 100 лет")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, (int, float)) or w < 20:
#             raise TypeError("Вес должен быть числом от 20 киллограм и выше")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Не верный формат паспорта")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def ps(self):
#         return self.__ps
#
#     @ps.setter
#     def ps(self, ps):
#         self.verify_ps(ps)
#         self.__ps = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# p1 = UserDate('Спиридонов Артём Геннадьевич', 23, "1123 434556", 111)
#
# p1.fio = 'Соболев Игорь Николаевич'
# print(p1.fio)
# p1.old = 26
# print(p1.old)
# p1.weight = 23
# print(p1.weight)
# p1.ps = '3453 234234'
# print(p1.ps)
# =============================================

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
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
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def __set_one_coords(self, sp):
#         if sp.is_int():
#             self._sp = sp
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def __set_two_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def set_coords(self, sp: Point, ep: Point = None):
#         if ep is None:
#             self.__set_one_coords(sp)
#         else:
#             self.__set_two_coords(sp, ep)
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40), Point(100, 200))
# line.draw_line()
# line.set_coords(Point(-10, -23))
# line.draw_line()
# ====================================================================

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
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
#             print("Координаты должны быть числами")
#
#     def draw(self):  # Абстрактный метод
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rectangle(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольник: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование элипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figure = list()
# figure.append(Line(Point(0, 0), Point(10, 10)))
# figure.append(Line(Point(20, 20), Point(30, 30)))
# figure.append(Rectangle(Point(60, 60), Point(80, 80)))
# figure.append(Ellipse(Point(440, 440), Point(3310, 3310)))
#
# for i in figure:
#     i.draw()
#
#
# from abc import ABC, abstractmethod
#
#
#  # абстрактный класс
# class Chess(ABC):
#     def draw(self):
#         print('Нарисовал шахматную фигуру')
#
#     @abstractmethod
#     def move(self):  # адстракстный метод
#         print('Ферзь перемещен на 32у4')
#
#
# class Queen(Chess):
#     def move(self):
#         print('Ферзь перемещен на у2у4')
#
#
# q = Queen()
# q.draw()
# q.move()
# a = Chess
# a.move(3)
# import math
#
#
# class Table:
#
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             self._width = width
#             self._length = length
#         else:
#             self._radius = radius
#
#     def set_radius(self, radius):
#         self._radius = radius
#
#     def set_sides(self, width=None, length=None):
#         if length is None:
#             self._width = self._length = width
#         else:
#             self._width = width
#             self._length = length
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class Sq_table(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class Round_table(Table):
#     def calc_area(self):
#         return math.pi * self._radius ** 2
#
#
# t = Sq_table(20, 10)
# print(t.__dict__)
# print(t.calc_area())
# t1 = Round_table(radius=4)
# t1.set_radius(56)
# print(t1.__dict__)
# print(t1.calc_area())


from abc import ABC, abstractmethod

# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(f'{Dollar.suffix}', end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EURO'
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(f'{Euro.suffix}', end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# print('*' * 50)
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
#
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print('*' * 50)
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print('Child class')
#         print('Display 1 Abstract Method')
#
#
# class GrandChild(Child):
#     def display2(self):
#         print('GrandChild')
#         print('Display 2 Abstract Method')
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print('Я - метод внешнего класса')
#
#     def outer_obj_method(self):
#         print('Я являюсь связывающим методом объектса внешнего класса')
#
#     class MuInner:
#         def __init__(self, inner_name, obj):
#             self.obj = obj
#             self.inner_name = inner_name
#
#         def inner_method(self):
#             print('Я - метод внутренего класса')
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#             print(self.obj.name)
#             # out1 = MyOuter('Внешний класс')
#             # print(out1.name)
#
#
#
# out = MyOuter('Внешний')
# inner = out.MuInner('Внутрений', out)
# inner.inner_method()


# class Employer:
#     def __init__(self):
#         self.name = 'Employer'
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Employer list')
#         print('Name:', self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#             self.id = '567'
#
#         def display(self):
#             print('Name', self.name)
#             print('Degree:', self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Albina'
#             self.id = '56'
#
#         def display(self):
#             print('Name', self.name)
#             print('Degree:', self.id)
#
# out = Employer()
# out.show()
# d1 = out.intern
# d1.display()
# d2 = out.head
# d2.display()

# class Geefforgeeks:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print('Родительский класс')
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass
#         def show(self):
#             print("Вложенный классс")
#
#         class InnerClass:
#             def show(self):
#                 print('Вложенный класс в вложенном классе')
#
#
# outer = Geefforgeeks()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()
# class Computer:
#     def __init__(self):
#         self.name = 'PC001'
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return 'Windows 10'
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'Core-i7'
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make(), end=' ')
# print(my_cpu.model())


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('In Base Class')
#
#     class Inner:
#         def display1(self):
#             print('Inner of Base Class')
#
# class SubClass(Base):
#     def __init__(self):
#         print('in SubClass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Inner of SubClass')
#
#
# a = SubClass()
# a.display()
#
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' is braking')
#
#
# b = Dog('Buddy')
# b.bark()
# b.play()
# b.sleep()

# class A:
#     # def __init__(self):
#     #     print('Инициализатор класса А')
#     # def hi(self):
#     #     print('A')
#     pass
#
#
# class AA:
#     pass
#
#
# class B(A):
#     # def __init__(self):
#     #     print('Инициализатор класса B')
#     # def hi(self):
#     #     print('B')
#     pass
#
#
# class C(AA):
#     # def __init__(self):
#     #     print('Инициализатор класса C')
#     # def hi(self):
#     #     print('C')
#     pass
#
#
# class D(B, C):
#     pass
#
#
# # def __init__(self):
# #     print('Инициализатор класса D')
#
#
# # class D(B, C):
# #     pass
#
#
# d = D()
# d.hi()
# print(D.mro())
#
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x, self.y})'
#
# class Styles:
#     def __init__(self, color='red', width=1):
#         print('Инициализатор Styles')
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp:Point, ep:Point):
#         print('Инициализатор Pos')

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def show(self):
#         print(self.name, end='')
#         self.note.show()
#
#     class Notebook:
#         def __init__(self):
#             self.brand = 'HP'
#             self.cpu = 'i7'
#             self.ram = 16
#
#         def show(self):
#             print(f'=> {self.brand}, {self.cpu},{self.ram}')
#
# s1 = Student('Roman')
# s2 = Student('Vladimir')
#
# s1.show()
# s2.show()

# class Display:
#     @staticmethod
#     def display(message):
#         print(message)
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#             Display.display(message)
#             self.log(message)
#
# class MySubClass(LoggerMixin, Display):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclass.txt')
#
#
# sub = MySubClass()
# sub.display('Это строка будет отображатся и записываться в файл')

# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print('Init Goods')
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print('Init MixinLog')
#         MixinLog.ID += 1
#         self.id = self.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: товар был продан в 00:00 часов')
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook('HP', 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# n2 = NoteBook('HP', 1.5, 35000)
# n2.save_sell_log()
#
# print(NoteBook.mro())

# class Clock:
#     __DAY = 86400  # 24*60*60 - число секунд во одном дне
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise TypeError('Секунды должны быть целым числом')
#
#         self.__secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.__secs % 60
#         m = (self.__secs // 60) % 60
#         h = (self.__secs // 3600) % 24
#         return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#         return Clock(self.__secs + other.__secs)
#
#     def __sub__(self, other):
#         return Clock(self.__secs - other.__secs)
#
#     def __mul__(self, other):
#         return Clock(self.__secs * other.__secs)
#
#     def __floordiv__(self, other):
#         return Clock(self.__secs // other.__secs)
#
#     def __mod__(self, other):
#         return Clock(self.__secs % other.__secs)
#
#     def __eq__(self, other):
#         return self.__secs == other.__secs
#         # if self.__secs == other.__secs:
#         #     return True
#         # return False
#
#
# c1 = Clock(200)
# c2 = Clock(200)
#
# if c1 == c2:
#     print('Время одинаковое')
# else:
#     print('Время разное')
# print(c1.get_format_time())
# c3 = c1 - c2
# print(c3.get_format_time())
# c3 = c1 * c2
# print(c3.get_format_time())
# c3 = c1 // c2
# print(c3.get_format_time())
# c3 = c1 % c2
# print(c3.get_format_time())
# c1 -= c2
# print(c1.get_format_time())
# c1 *= c2
# print(c1.get_format_time())
# c1 //= c2
# print(c1.get_format_time())
# c1 %= c2
# print(c1.get_format_time())
#

# print(c1.get_format_time())
# print(c2.get_format_time())
# c3 = Clock(300)
# c4 = c1 + c3
# print(c4.get_format_time())

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError('Неверный индекс')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('Индекс должен быть целым неотрицательным числом')
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError('Индекс должен быть целым числом')
#         del self.marks[key]
#
#
# s1 = Student('Sergey', [5, 5, 3, 4, 5])
# print(s1[0])
# s1[10] = 4
# del s1[2]
# print(s1.marks)

# class Point3D:
#     CH = 'Координата должна быть числом'
#     RIGHT = 'Правый операнд должен быть типом Point3D'
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f'{self.x}, {self.y}, {self.z}'
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x * other.x, self.__y * other.y, self.__z * other.z)
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         self.__check0(other)
#         return Point3D(self.__x / other.x, self.__y / other.y, self.__z / other.z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         return self.__x == other.x and self.__y == other.y == self.__z == other.z
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise TypeError('Ключ должен быть строкой')
#         elif item == 'x':
#             return self.__x
#         elif item == 'y':
#             return self.__y
#         elif item == 'z':
#             return self.__z
#         else:
#             print('Неверное значение ключа')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise TypeError('Ключ должен быть строкой')
#         if self.__check_value(value):
#             if key == 'x':
#                 self.__x = value
#             if key == 'y':
#                 self.__y = value
#             if key == 'z':
#                 self.__z = value
#         else:
#             print('Неверное значение ключа')
#
#     @staticmethod
#     def __check0(v):
#         if v.x == 0 or v.y == 0 or v.z == 0:
#             raise ZeroDivisionError('Значение правого операнда не должна равнятся 0')
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, int) or isinstance(v, float)
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.CH)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.CH)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.CH)
#
#
# pt = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print(f'Координаты 1-й точки: {pt}')
# print(f'Координаты 2-й точки: {pt2}')
# pt3 = pt + pt2
# print(f'Сложение координат: ({pt3})')
# pt4 = pt - pt2
# print(f'Вычитание координат: ({pt4})')
# pt5 = pt * pt2
# print(f'Умножение: ({pt5})')
# pt6 = pt / pt2
# print(f'Деление: ({pt6})')
# print(f'Равенство координат: {pt == pt2}')
#
# print('x =', pt['x'], 'x1 =', pt2['x'])
# print('x =', pt['y'], 'x1 =', pt2['y'])
# print('x =', pt['z'], 'x1 =', pt2['z'])
#
# pt['x'] = 20
# print('Запись значения в координату x:', pt['x'])
# print(f'Координаты 1-й точки: {pt}')

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_per(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_per(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# print(r1.get_per(), r2.get_per())
#
# s1 = Square(10)
# s2 = Square(20)
# print(s1.get_per(), s2.get_per())
#
# shape = [r1, r2, s1, s2]
#
# for q in shape:
#     print(q.get_per())

# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text('Python')
# print(t1.total(35))
# print(t2.total(35))

# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
# 
#     def info(self):
#         print(f'{self.last_name} {self.first_name} {self.age}')
# 
# 
# class Student(Human):
#     def __init__(self, spec, group, rating, last_name, first_name, age):
#         super().__init__(last_name, first_name, age)
#         self.speciality = spec
#         self.group = group
#         self.rating = rating
# 
#     def info(self):
#         print(f'{self.speciality} {self.group} {self.rating}', end=' ')
#         super().info()
# 
# 
# class Teacher(Human):
#     def __init__(self, spec, ex, last_name, first_name, age):
#         super().__init__(last_name, first_name, age)
#         self.speciality = spec
#         self.ex = ex
# 
#     def info(self):
#         print(f'{self.speciality} {self.ex}', end=' ')
#         super().info()
# 
# 
# class Graduate(Student):
#     def __init__(self, topic, spec, group, rating, last_name, first_name, age):
#         super().__init__(spec, group, rating, last_name, first_name, age)
#         self.topic = topic
# 
#     def info(self):
#         print(f'{self.topic}', end=' ')
#         super().info()
# 
# 
# group = [
#     Student('Батодалаев', "даши", 16, "ГК", 'Web_011', 5)
# ]
# for i in group:
#     i.info()

# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p = Point(5, 9)
# print(p.length)
# p.z = 6
# print(p.__dict__)

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
#
# print("pt = ", pt.__sizeof__())
# print("pt2 = ", pt2.__sizeof__() + pt2.__dict__.__sizeof__())
#
# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#     def __init__(self, x, y, z):
#         super().__init__(x,y)
#         self.z = z
#
#
# pt3 = Point3D(10, 20, 30)
# pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)
# print(pt3.__dict__)


# Функторы

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#         return self.__counter
#
#
# c1 = Counter()
# c1()
# c1()
# c1()f
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()
# c2()
# c2()

# class ScripsChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError('Argument should be str')
#         return args[0].strip(self.__chars)
#
#
# s1 = ScripsChars('?:!.; ')
# print(s1(" ?Hello World! "))
#
#
# def strip_string(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError('Argument should be str')
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = strip_string('?:!.; ')
# print(s1(" ?Hello World! "))

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('Перед вызовом функции')
#         self.func()
#         print('после вызова функции')
#
#
# @MyDecorator
# def function():
#     print('func')
#
#
# function()

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         print('Перед вызовом функции')
#         res = self.func(a, b)
#         print('после вызова функции')
#         return res ** 2
#
#
# @MyDecorator
# def function(a, b):
#     return a * b
#
#
# print(function(2, 3))


# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print('Перед вызовом функции')
#             print(self.name)
#             func(a, b)
#             print('после вызова функции')
#
#         return wrap
#
#
# @MyDecorator('test2')
# def function(a, b):
#     print(a, b)
#
#
# print(function(2, 3))

# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, argf):
#         def wrap(a, b):
#             return argf(a, b) ** self.arg
#
#         return wrap
#
#
# @Power(3)
# def multuple(a, b):
#     return a * b
#
#
# print(multuple(2, 2))

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print('*' * 20)
#         fn(*args, **kwargs)
#         print('*' * 20)
#     return wrap
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person('Vitaly', 'Ivanov')
# p1.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print('Init ActualClass')
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))
#
# class Message:
#     _REGISTERY = {}
#
#     def __init__(self, text):
#         self.text = text
#
#     @classmethod
#     def register(cls, name):
#         def decorator(klass):
#             cls._REGISTERY[name] = klass
#             return klass
#         return decorator
#
#     @classmethod
#     def create(cls, type_mess, text):
#         klass = cls._REGISTERY.get(type_mess)
#         if klass is None:
#             raise ValueError('Такого мессенджера нет')
#         print(text, end=' ')
#         return klass(text)
#
# @Message.register('Telegram')
# class Telegram(Message):
#     def send(self):
#         print('(Telegram)')
#
# @Message.register('WhatsApp')
# class WhatsApp(Message):
#     def send(self):
#         print('(WhatsApp)')
#
#
# m1 = Message.create('Telegram','Hi, i am programmer in T')
# m1.send()
# m2 = Message.create('WhatsApp', 'Hi, i am programmer in W')
# m2.send()

# Дескриптор
# class Person:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, value):
#         self.__surname = value
#
# p = Person('Ivan', 'Ivanov')

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#
# p = Person('Ivan', 'Ivanov')
# print(p.name.get())
# p.name.set('Игорь')
# print(p.name.get())


# Дескрипторы
# __get__()
# __set__()
# __delete__()
# __set_name__()
# non-data descriptor - дескриптор не данных


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person('Ivan', 'Ivanov')
# print(p.name)
# p.surname = 'Kirill'
# print(p.surname)

# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Значение должно быть положительным')
#         instance.__dict__[self.__name] = value
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#
# class Order:
#     price = NonNegative()
#     qua = NonNegative()
#
#     def __init__(self, name, price, qua):
#         self.name = name
#         self.price = price
#         self.qua = qua
#
#     def total(self):
#         return self.price * self.qua
#
#
# apple = Order('apple', 5, 10)
# print(apple.total())
# apple.price = 10
# print(apple.price)

# Метаклассы

# a = 5
# print(type(a))
# print(type(int))
# print(type(type))
#

# class Mylist(list):
#     def het_length(self):
#         return len(self)
#
#
# lst = Mylist()
# lst.append(1)
# lst.append(2)
# lst[0] = 3
# print(lst, lst.het_length())

# Mylist = type(
#     'Mylist',
#     (list,),
#     dict(het_length=lambda self: len(self))
# )
# lst = Mylist()
# lst.append(1)
# lst.append(2)
# lst[0] = 3
# print(lst, lst.het_length())

# class MyMetaclass(type):
#     def __new__(mcs, name, bases, attr):
#         print('Создание нового объекта', name)
#         return super(MyMetaclass, mcs).__new__(mcs, name, bases, attr)
#
#     def __init__(cls, name, bases, attr):
#         print('Init of class', name)
#         super(MyMetaclass, cls).__init__(name, bases, attr)
#
#
# class Student(metaclass=MyMetaclass):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# stud = Student('Ann')
# print(stud.get_name())
# print(type(stud))
# print(type(Student))

# import math
# from math import pi
# print(pi)

# import пакет.модуль
# import geometry.rect
# import geometry.sq
# import geometry.trian
# from wheel import rect,sq,trian
# from wheel import *
#
# # from geometry import *
#
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
# s1 = sq.Square(10)
# s2 = sq.Square(20)
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())
#
# print(__name__)
#
if __name__ == '__main__':
    #  содержимое класса
    pass


from car import electrocar

e = electrocar.Electrocar('Tesla', 'T', 2018, 99000)
e.show_car()
e.decription_battery()


# Упаковка данных
# Сериализация (кодирование) - запись данныз на диск
# Десериализация (декодирование) - чтение данных с памяти/диска

# Ствндарстной библиотеке python:
# - marshal
# - pickle
#          dump() - сохраняет данные в файл
#          load() - считывает данные
#          dump() - сохраняет данные в оперативную память
#          loads() - считывает данные оперативной памяти
# - json

import pickle


# filename = 'basket.txt'
#
# shoplist = {
#     "фрукты": ['apple', 'mango'],
#     'овощи': ['morkov'],
#     'money': 1000
# }
#
# with open(filename, 'wb') as yyyy:
#     pickle.dump(shoplist, yyyy)
#
# with open(filename, 'rb') as h:
#     print(pickle.load(h))


# class Test:
#     a_number = 35
#     a_string = 'hi'
#     a_list = [1, 2, 23, 4, 3]
#     a_tuple = (23, 22)
#     a_dict = {'31234': 'df', 'sef': 334, 'ddf': [2, 2, 2]}
#
#     def __str__(self):
#         return f'Число: {Test.a_number}\nСтрока{Test.a_string}\nСписок данных{Test.a_list}\nКортеж{Test.a_tuple}' \
#                f'\nСловарь{Test.a_dict}'
#
#
# obj = Test()
# my_obj = pickle.dumps(obj)
# print(f'Сериализация в строку: \n{my_obj}\n')
#
# obj_a = pickle.loads(my_obj)
# print(f'Десериализация в строку: \n{obj_a}\n')

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f'{self.a}, {self.b}, {self.c(2)}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         print(attr)
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#         print(state)
#
# item = Test2()
# item2 = pickle.dumps(item)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)

# class TextReader:
#     def __init__(self, filename):
#
#
