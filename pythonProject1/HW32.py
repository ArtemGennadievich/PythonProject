class Reboot:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __lt__(self, other):
        return self.value <= other.value

    def __le__(self, other):
        return self.value <= other.value


c3 = Reboot(3)
c1 = Reboot(1)
print('c3 > c1', c3 > c1)
print('c3 >= c1', c3 >= c1)
print('c3 < c1', c3 < c1)
print('c3 <= c1', c3 <= c1)
