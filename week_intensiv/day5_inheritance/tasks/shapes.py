import math

class Shape:
    def get_area(self):
        return 0

class Circle(Shape):
    """
    ЗАДАЧА: Переопределить get_area для круга.
    1. Конструктор принимает radius.
    2. get_area возвращает площадь: pi * r^2.
    3. Используйте math.pi.
    """
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    """ЗАДАЧА: Реализовать площадь квадрата (сторона * сторона)"""
    def __init__(self, side):
        self.side = side
        pass

    def get_area(self):
        return self.side * self.side
        pass