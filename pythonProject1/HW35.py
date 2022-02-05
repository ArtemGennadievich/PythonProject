class SG:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('Число должно быть целым')
        instance.__dict__[self._name] = value


class Point3D:
    x = SG()
    y = SG()
    z = SG()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


point = Point3D(1, 2, 3)
print(point.__dict__)
