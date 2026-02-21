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
        pass

    def get_area(self):
        pass

class Square(Shape):
    """ЗАДАЧА: Реализовать площадь квадрата (сторона * сторона)"""
    def __init__(self, side):
        pass

    def get_area(self):
        pass