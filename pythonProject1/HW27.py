class Temperature:
    count = 0

    @staticmethod
    def celsius(t):
        Temperature.count += 1
        return int((t - 32) / 1.8)

    @staticmethod
    def fahrenheit(t):
        Temperature.count += 1
        return int(t * 1.8 + 32)

    @staticmethod
    def count_value():
        return Temperature.count


print(Temperature.fahrenheit(10))
print(Temperature.celsius(50))
print(Temperature.count_value())
