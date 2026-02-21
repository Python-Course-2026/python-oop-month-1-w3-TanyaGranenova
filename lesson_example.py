"""
ШПАРГАЛКА ПО ИНТЕНСИВУ (Дни 1-7)
Используй этот файл как образец для решения всех задач.
"""


class Product:
    """
    ДЕНЬ 1: МАГИЧЕСКИЕ МЕТОДЫ (Dunder methods)
    Учат объект взаимодействовать с функциями Python (print, len, sort).
    """

    def __init__(self, name: str, price: float):
        # Инкапсуляция (День 2): _price — защищенный атрибут
        self.name = name
        self._price = price

    @property
    def price(self):
        """ДЕНЬ 2: ГЕТТЕР. Позволяет читать self.price как обычную переменную."""
        return self._price

    @price.setter
    def price(self, value):
        """ДЕНЬ 2: СЕТТЕР. Защищает данные от некорректного ввода."""
        if value < 0:
            raise ValueError("Цена не может быть отрицательной!")
        self._price = value

    def __str__(self):
        """Для пользователя: print(obj)"""
        return f"{self.name} ({self.price} руб.)"

    def __repr__(self):
        """Для отладки: отображение внутри списков [obj1, obj2]"""
        return f"Product(name='{self.name}', price={self.price})"

    def __lt__(self, other):
        """ДЕНЬ 1: Сравнение (Less Than). Нужно для работы функции sort()."""
        return self.price < other.price


class ShoppingCart:
    """
    ДЕНЬ 3-4: ЛОГИКА И КОЛЛЕКЦИИ (Lists & Analytics)
    Учит управлять группой объектов и считать по ним статистику.
    """

    def __init__(self):
        # ДЕНЬ 3: Список как хранилище объектов
        self.items = []

    def add_product(self, product: Product):
        """ДЕНЬ 6: ВЗАИМОДЕЙСТВИЕ. Один объект влияет на другой."""
        if not isinstance(product, Product):
            return "Ошибка: Это не товар"
        self.items.append(product)

    def get_total(self):
        """ДЕНЬ 4: АЛГОРИТМЫ. Агрегация данных (сумма, фильтры, условия)."""
        # Считаем сумму через генератор списка
        total = sum(item.price for item in self.items)

        # Сложная логика (Скидки/Бонусы)
        if len(self.items) >= 3:
            total *= 0.9  # Скидка 10%
        return round(total, 2)

    def filter_expensive(self, threshold: float):
        """ДЕНЬ 4: ФИЛЬТРАЦИЯ. Возврат подмножества объектов."""
        return [item for item in self.items if item.price > threshold]

    def __len__(self):
        """ДЕНЬ 1: Магия. Позволяет писать len(cart)."""
        return len(self.items)


# --- ПРИМЕР ---
if __name__ == "__main__":
    # 1. Создание объектов (День 1-2)
    p1 = Product("Кофе", 300)
    p2 = Product("Сэндвич", 150)
    p3 = Product("Торт", 500)

    # 2. Использование коллекции (День 3-4)
    cart = ShoppingCart()
    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)

    # 3. Демонстрация результатов
    print(f"Список объектов (repr): {cart.items}")
    print(f"Сортировка (благодаря __lt__): {sorted(cart.items)}")
    print(f"Итого со скидкой: {cart.get_total()}")