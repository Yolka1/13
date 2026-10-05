import math

class Triangle:

    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError ("Стороны треугольника должны быть положительными")
        if a + b <= c or b + c <= 0 or a + c <= 0:
            raise ValueError ("Треугольника с такими сторонами не существует")

        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def perimeter(self):
        return self.__a + self.__b + self.__c
    @property
    def area(self):
        p = self.perimeter / 2
        return math.sqrt(p*(p - self.__a)*(p - self.__b)*(p - self.__c))
    def angle(self, a, b, c):
        cos_angle = (a**2 + b**2 - c**2) / (2*a*b)
        return math.degrees (math.acos(cos_angle))