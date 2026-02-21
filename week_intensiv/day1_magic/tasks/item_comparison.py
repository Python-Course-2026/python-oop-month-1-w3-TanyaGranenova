class Item:
    """ЗАДАЧА: Сравнение товаров по цене через __lt__ и по всем полям через __eq__"""
    def __init__(self, name, price): self.name, self.price = name, price
    def __lt__(self, other): pass
    def __eq__(self, other): pass