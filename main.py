class Integer:
    @classmethod
    def verify_method(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом!')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_method(value)
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @classmethod
    def verify_method(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом!')


p = Point3D(1, 2, 3)
