import math

class Shape:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_area(self):
        pass

class RectageleShape(Shape):
    def __init__(self, name,length, width):
        super().__init__(name)
        self._length = length
        self._width = width
    def get_area(self):
        return self._length * self._width

class CircleShape(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self._radius = radius

    def get_area(self):
        return math.pi * self._radius ** 2

class SquareShape(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self._side = side

    def get_area(self):
        return self._side ** 2

class TriangleShape(Shape):
    def __init__(self, name, base, hight):
        super().__init__(name)
        self._base = base
        self._hight = hight

    def get_area(self):
        return (self._base * self._hight) / 2
