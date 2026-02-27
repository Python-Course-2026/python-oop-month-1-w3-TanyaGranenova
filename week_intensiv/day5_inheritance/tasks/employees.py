class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class Developer(Employee):
    """
    ЗАДАЧА: Реализовать расчет зарплаты с бонусом.
    1. Конструктор должен принимать name, base_salary и bonus.
    2. Использовать super() для инициализации родительских атрибутов.
    3. Переопределить calculate_salary: возвращать base_salary + bonus.
    """
    def __init__(self, name, base_salary, bonus):
        # ТВОЙ КОД ЗДЕСЬ
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # ТВОЙ КОД ЗДЕСЬ
        return self.base_salary + self.bonus