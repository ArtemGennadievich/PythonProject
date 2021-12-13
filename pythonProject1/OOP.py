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

def sum_args(a,b):
    print(a + b)


sum_args(5, 2)
sum_args("Hello", " world")