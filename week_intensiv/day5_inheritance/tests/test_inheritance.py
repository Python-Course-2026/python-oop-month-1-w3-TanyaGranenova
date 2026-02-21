import pytest
import math
from week_intensiv.day5_inheritance.tasks.employees import Employee, Developer
from week_intensiv.day5_inheritance.tasks.shapes import Circle, Square
from week_intensiv.day5_inheritance.tasks.smart_home import Light


# Тест сотрудников
def test_developer_inheritance():
    dev = Developer("Alice", 1000, 500)
    assert isinstance(dev, Employee), "Developer должен наследоваться от Employee"
    assert dev.calculate_salary() == 1500, "Зарплата с бонусом считается неверно"
    assert dev.name == "Alice", "Имя не проброшено через super()"


# Тест фигур
def test_shapes_area():
    c = Circle(10)
    assert math.isclose(c.get_area(), 314.159, rel_tol=1e-3), "Площадь круга неверна"

    s = Square(5)
    assert s.get_area() == 25, "Площадь квадрата неверна"


# Тест умного дома
def test_light_device():
    lamp = Light("Xiaomi", 80)
    assert lamp.is_on is False, "По умолчанию устройство должно быть выключено"
    assert lamp.work() == "Свет выключен"

    lamp.toggle()  # Метод родителя Device
    assert lamp.is_on is True
    assert "яркость: 80%" in lamp.work(), "Метод work() должен учитывать яркость"