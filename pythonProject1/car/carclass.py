class CarClass:
    def __init__(self,brand, model, year, distance):
        self.brand = brand
        self.model = model
        self.year = year
        self.distance = distance

    def show_car(self):
        print(f'{self.brand}, {self.model}, {self.year} год, {self.distance} км')

    if __name__ == '__main__':
        pass