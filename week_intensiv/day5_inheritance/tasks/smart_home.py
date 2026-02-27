class Device:
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on

class Light(Device):
    """
    ЗАДАЧА: Наследование и расширение.
    1. Конструктор принимает brand и brightness (от 0 до 100).
    2. Метод work() возвращает:
       "Свет включен, яркость: X%" если is_on True,
       "Свет выключен" если is_on False.
    """
    def __init__(self, brand, brightness):
        super().__init__(brand)
        self.brightnees = brightness


    def work(self):
        if self.is_on:
            return f"Свет включен, яркость: {self.brightnees}%"
        else:
            return "Свет выключен"
