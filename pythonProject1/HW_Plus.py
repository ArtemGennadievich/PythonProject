import re


class Time:
    uts_static = f'UTC'

    def __init__(self, date, utc):

        if not isinstance(date, str):
            print("Дата должна быть строкой")
        if self.verify(date) is True and self.verify_utc(utc) is True:
            lst_data = date.split(':')
            self.hours = lst_data[0]
            self.minute = lst_data[1]
            self.second = lst_data[2]
            self.utc = utc
            self.date = date
            if utc > 0:
                print(f'Отметка времени: {self.date} {Time.uts_static}+{self.utc}')
            else:
                print(f'Отметка времени: {self.date} {Time.uts_static}{self.utc}')
        else:
            self.date = date
            self.utc = utc

    def __del__(self):
        print(f'Отметка времени{self.date, self.utc} быда удалена')

    @classmethod
    def change_utc(cls, utc):
        Time.utc = utc
        if utc > 0:
            print(f'{Time.uts_static}+{utc}')
            print()
        else:
            print(f'{Time.uts_static}{utc}')
            print()

    @staticmethod
    def verify_utc(utc):
        if utc < -12 or utc > 14:
            print('Неверное значение: смещение времени UTC должно быть от -12 до +14!')
        else:
            return True

    @staticmethod
    def verify(date):
        reg = r'0[1-9]|1[0-9]|2[0-4]:[0-5][0-9]:[0-5][0-9]'
        verify = re.findall(reg, date)
        if not verify:
            print('Неверные данные!')
        else:
            return True

    @staticmethod
    def convert_second_from_data(date):
        lst_data_convert = date.split(':')
        second_hours = int(lst_data_convert[0]) * 3600

        second_minute = int(lst_data_convert[1]) * 60
        second = int(lst_data_convert[2])
        res = second_hours + second_minute + second
        return res

    @staticmethod
    def convert_data_from_second(second):
        sec = second % (24 * 3600)
        hour = second // 3600
        sec %= 3600
        min = sec // 60
        sec %= 60
        return "%02d:%02d:%02d" % (hour, min, sec)

    def print_value(self):
        print(f'Отметка времени: {self.date} {Time.uts_static}{self.utc}')

    def operation_diff_data(self, data_v):
        return f'Разница между {self.date} {Time.uts_static}{self.utc} и {data_v.date} {Time.uts_static}{data_v.utc}' \
               f' {self.convert_second_from_data(self.date) - self.convert_second_from_data(data_v.date)} сек'

    def operation_plus_data_local(self, data_v):
        print(f'Добавьте {data_v} сек в {self.date} {Time.uts_static}{self.utc}:\n'
              f'Отметка времени: '
              f'{self.convert_data_from_second(data_v + self.convert_second_from_data(self.date))} {Time.uts_static}'
              f'{self.utc}')
        self.date = self.convert_data_from_second(data_v + self.convert_second_from_data(self.date))

    def operation_diff_data_local(self, data_v):
        print(f'Вычтите {data_v} сек в {self.date} {Time.uts_static}{self.utc}:\n'
              f'Отметка времени: '
              f'{self.convert_data_from_second(self.convert_second_from_data(self.date) - data_v)} {Time.uts_static}'
              f'{self.utc}')
        self.date = self.convert_data_from_second(self.convert_second_from_data(self.date) - data_v)

    def verify_return(self, date):
        if self.date.split(':') == date.date.split(':'):
            print(f'Отметки времени: {self.date} {Time.uts_static}{self.utc} и {date.date} {Time.uts_static}{date.utc} '
                  f'- это один и тот же момент)')
        else:
            print(f'Отметки времени: {self.date} {Time.uts_static}{self.utc} и {date.date} {Time.uts_static}{date.utc} '
                  f'- это не один и тот же момент)')


data = Time('23:18:00', 2)
print('-' * 50)
data_false = Time('00:00:00', -4)
print('-' * 50)
data_false2 = Time('00:00:00', -4)
print('-' * 50)
print('')
data2 = Time('14:05:37', -14)
data2.change_utc(2)
data2.change_utc(-4)
data2.print_value()
print('-' * 50)
data2.print_value()
print()
data3 = Time('08:00:03', -4)
print('-' * 50)
print(data3.operation_diff_data(data2))
del data3
data2.operation_plus_data_local(320)
data2.operation_diff_data_local(3665)
print('-' * 50)
data4 = Time('13:09:52', -4)
print('-' * 50)
data4.verify_return(data2)
del data2
data5 = Time('13:09:53', -4)
print('-' * 50)
data5.verify_return(data4)
del data5
print()
del data
del data_false
del data_false2

# data.convert_data_from_second()
