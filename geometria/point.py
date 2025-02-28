import math

class Point:
    def __init__(self, x=0, y=0):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be numeric values.")  # verifica que los números dados sean numéricos
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be a numeric value.")  # verifica que el número dado sea numérico
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be a numeric value.")  # verifica que el número dado sea numérico
        self._y = value

    def compute_distance(self, other):
        if not isinstance(other, Point):
            raise TypeError("Argument must be a Point instance.")  # verifica que el argumento sea un objeto Point
        return math.sqrt((self._x - other.x) ** 2 + (self._y - other.y) ** 2)
