import random
import json


class Data:

    def __init__(self, name):
        self.name = name

    def ran_num(self):
        return random.randint(1, 1000000)

    def random_dict(self):
        number = ''
        name_dic = ['Anna', 'Igor', 'Ivan', 'Pasha', 'Dima']
        person = {}

        for num in range(10):
            number += str(random.randint(1, 9))
        number = '8' + number
        name_dict = random.choice(name_dic)
        person.update({'name': name_dict, 'number': number})
        return person

    def dict_for_i(self):
        person3 = {}
        for i in range(5):
            person3[i + 1] = self.random_dict()
        return person3

    def dump_dict(self):
        try:
            dat = json.load(open(self.name))
        except FileNotFoundError:
            dat = {}
        dat[self.ran_num()] = (self.random_dict())

        with open(self.name, 'w') as dic:
            json.dump(dat, dic, indent=3)


data = Data('ss.json')
print(data.random_dict())
data.dump_dict()