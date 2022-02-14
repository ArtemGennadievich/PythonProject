import json


class Country:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        country_dict = {self.key: self.value}
        self.dict = country_dict

    def __str__(self):
        return f'Страна:{self.key}, Cтолица: {self.value}'

    def add_dict(self, key, value):
        other = {key: value}
        self.dict.update(other)
        return f'Данные внесены'

    def remove_dict(self, key):
        self.dict.pop(key)
        print('Данные удалены')

    def ret_dict_value(self, key, sor):
        if sor == 1:
            for k, v in self.dict.items():
                if k == key:
                    return k
            else:
                return 'Нет такого значения'
        if sor == 2:
            for k, v in self.dict.items():
                if v == key:
                    return v
            else:
                return 'Нет такого значения'

    def change_dict(self, pos, key, value):
        if pos == 2:
            for k, v in self.dict.items():
                if v == key:
                    self.dict[k] = value
                else:
                    return 'Не верные значения'
            return f'Данные изменены'
        if pos == 1:
            self.dict[value] = self.dict.pop(key)
            return f'Данные изменены'

    def dump_dict(self, filename):
        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = []
        data.append(self.dict)
        with open(filename, 'w') as file:
            json.dump(data, file, indent=5)
        return f'Файл сохранён'

    @classmethod
    def load_dict(cls, filename):
        with open(filename, 'r') as file:
            print(json.load(file))


country = Country('Russia', 'Moscow')
while True:
    try:
        user = int(
            input(
                'Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных'
                '\n4 - редактирование данных'
                '\n5 - сохранение данных\n6 - просмотр данных\n'))
        if user == 1:
            value_country_add = input('Какую страну вы хотите добавить? ') or 'USA'
            value_capital_add = input('Какую столицу вы хотите добавить? ') or 'Washington'
            country.add_dict(value_country_add, value_capital_add)
            print(country.dict)
        if user == 2:
            value_country_del = input(f'Какую страну вы хотите удалить? Доступно: {country.dict.keys()}') or 'USA'
            country.remove_dict(value_country_del)
            print(country.dict)
        if user == 3:
            value_country_shear = int(input('Что вы хотите найти?\n1 - Страну\n2 - Столицу\n')) or 1
            if value_country_shear == 1:
                value_country_shear_1 = input(
                    f'Какую страну вы хотите найти? Доступно: {country.dict.keys()}') or 'Russia'
                print(country.ret_dict_value(value_country_shear_1, 1))
            elif value_country_shear == 2:
                value_country_shear_2 = input(
                    f'Какую столицу вы хотите найти? Доступно: {country.dict.values()}') or 'Moscow'
                print(country.ret_dict_value(value_country_shear_2, 2))
            else:
                print("Введено не верное число")
        if user == 4:
            user_way = int(input('Что вы хотите поменять?\nСтрану - 1\nСтолицу - 2\n')) or 1
            if user_way == 1:
                value_country_1 = input(f'Какую страну вы хотите поменять? Доступно: {country.dict.keys()}') or 'Russia'
                value_country_2 = input(f'На какую страну вы хотите поменять {value_country_1}?') or 'German'
                country.change_dict(1, value_country_1, value_country_2)
                print(country.dict)
            elif user_way == 2:
                value_country_3 = input(
                    f'Какую столицу вы хотите поменять? Доступно: {country.dict.values()}') or 'Moscow'
                value_country_4 = input(f'На какую столицу вы хотите поменять {value_country_3}?') or 'Berlin'
                country.change_dict(2, value_country_3, value_country_4)
                print(country.dict)
            else:
                print("Введено не верное число")
        if user == 5:
            country.dump_dict('country.json')
        if user == 6:
            Country.load_dict('country.json')
    except ValueError:
        print("Ошибка!\nНе введены данные, попробуйте снова")
    t = input('\nДля повтора нажмите "ENTER"\nЧтобы закончить, нажмите 1: \n')
    if t == str(1):
        break
