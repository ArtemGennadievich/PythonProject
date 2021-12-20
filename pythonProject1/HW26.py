import math


class Sphere:
    def __init__(self, x=0, y=0, z=0, r=0):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def get_volume(self):
        return f'get_volume: {4 / 3 * math.pi * (self.r ** 3)}'

    def get_square(self):
        return f'get_square: {4 * math.pi * (self.r ** 2)}'

    def get_radius(self):
        return f'get_radius: {self.r}'

    def get_center(self):
        return f'get_center: {self.x, self.y, self.z}'

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def set_radius(self, r=0):
        self.r = r
        print(f'set_radius({r}): {r}')

    def is_point_inside(self, x, y, z):
        for_r = self.r ** 2
        for_coor = (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2
        if for_coor <= for_r:
            return f'is_point_inside{x, y, z}: {True}'
        else:
            return f'is_point_inside{x, y, z}: {False}'


sphere = Sphere(r=0.6)
print(sphere.get_radius())
print(sphere.get_volume())
print(sphere.get_square())
print(sphere.get_center())
print(sphere.get_square())
print(sphere.is_point_inside(0, -1.5, 0))
sphere.set_radius(1.6)
print(sphere.is_point_inside(0, -1.5, 0))
