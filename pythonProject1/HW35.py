class SG:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('Число должно быть целым')
        instance.__dict__[self.name] = value


class Point3D:
    x = SG()
    y = SG()
    z = SG()

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z


point = Point3D(1, 2, 3)
print(point.__dict__)
