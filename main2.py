class Person:
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_weight(weight)
        self.verify_ps(ps)
        self.__fio = fio
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой!")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО!")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Возраст должен быть целочисленным в пределах от 14 до 120!')

    @classmethod
    def verify_weight(cls,weight):
        if type(weight) != int or weight < 30 or weight > 320:
            raise TypeError('Вес должен быть целочисленным в пределах от 30 до 320!')

    @classmethod
    def verify_ps(cls,ps):
        if ps != str:
            raise TypeError('Паспортные данные должны быть в виду строки!')
        s = ps.split()
        if len(s) <3:
            raise TypeError('Неверный формат данных!')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self,old):
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, ps):
        self.__ps = ps

p = Person('Кимстач Даниил Борисович', 18,'MC2926685',81)
