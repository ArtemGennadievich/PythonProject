class Account:
    rate_usd = 0.013
    rate_euro = 0.011
    siffix = 'RUB'
    siffix_usd = 'USD'
    siffix_euro = 'EUR'

    def __init__(self, two_name, number, percent, value=0):
        self.__two_name = two_name
        self.__number = number
        self.__percent = percent
        self.__value = value

    def __del__(self):
        print("*" * 50)
        print(f'Счёт #{acc.get_number()} принадлежащий {acc.get_two_name()} был закрыт.')

    @staticmethod
    def first_print(number, two_name):
        print(f'Счёт #{number} принадлежащий {two_name} был открыт.')
        print("*" * 50)

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_euro_rate(cls, rate):
        cls.rate_euro = rate

    def get_two_name(self):
        return self.__two_name

    def get_number(self):
        return self.__number

    def get_value(self):
        return self.__value

    def get_percent(self):
        return self.__percent

    def convert_to_usd(self, value):
        usd_value = self.convert(value, Account.rate_usd)
        print(f'Состояние счёта: {usd_value} {Account.siffix_usd}')

    def convert_to_euro(self, value):
        euro_value = self.convert(value, Account.rate_euro)
        print(f'Состояние счёта: {euro_value} {Account.siffix_euro}')

    def print_balance(self, value):
        print(f'Текущий баланс: {value} {Account.siffix}')

    def print_info(self, number, two_name, percent):
        print('Информация о счёте:')
        print("-" * 20)
        print(f'#{number}')
        print(f'Владелец: {two_name}')
        self.print_balance(acc.get_value())
        print(f'Проценты: {percent:.0%}')
        print("-" * 20)

    def set_sur_name(self, name):
        self.__two_name = name

    def add_percent(self, value, percent):
        value += value * percent
        print("Проценты были успешно начислены!")
        self.print_balance(acc.get_value())

    def withdraw_money(self, value, val):
        if val > value:
            print(f'К сожалению у вас {val} {Account.siffix}')
        else:
            value -= val
            print(f'{val} {Account.siffix} было успешно снято')
        self.print_balance(acc.get_value())

    def add_money(self, value, val):
        value += val
        print(f'{val} {Account.siffix} было успешно добавлено')
        self.print_balance(acc.get_value())


acc = Account('Долгих', 12345, 0.03, 1000)
acc.first_print(acc.get_number(), acc.get_two_name())
acc.print_info(acc.get_number(), acc.get_two_name(), acc.get_percent())
acc.convert_to_usd(acc.get_value())
acc.convert_to_euro(acc.get_value())
Account.set_usd_rate(2)
print()
Account.set_euro_rate(3)
acc.convert_to_usd(acc.get_value())
acc.convert_to_euro(acc.get_value())
print()
acc.set_sur_name('Дюма')
acc.print_info(acc.get_number(), acc.get_two_name(), acc.get_percent())
acc.add_percent(acc.get_value(), acc.get_percent())
print()
acc.withdraw_money(acc.get_value(), 3000)
print()
acc.withdraw_money(acc.get_value(), 100)
print()
acc.add_money(acc.get_value(), 5000)
print()
acc.withdraw_money(acc.get_value(), 3000)


