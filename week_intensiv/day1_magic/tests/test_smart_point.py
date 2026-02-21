import pytest
from week_intensiv.day1_magic.tasks.smart_point import SmartPoint

def test_point_str():
    p = SmartPoint(10, 20)
    assert str(p) == "Точка(10, 20)", "Метод __str__ возвращает неверный формат"

def test_point_repr():
    p = SmartPoint(5, -5)
    assert repr(p) == "SmartPoint(x=5, y=-5)", "Метод __repr__ возвращает неверный формат"