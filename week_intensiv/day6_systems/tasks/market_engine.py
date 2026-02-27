class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Participant:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.inventory = []

class Market:
    """
    ЗАДАЧА: Реализовать метод deal(buyer, seller, item).
    1. Проверить, есть ли у buyer достаточно денег (money >= item.price).
    2. Если денег нет, вызвать ValueError("Недостаточно средств").
    3. Если деньги есть:
       - Вычесть цену из денег buyer.
       - Добавить цену к деньгам seller.
       - Добавить item в список buyer.inventory.
    """
    def deal(self, buyer: Participant, seller: Participant, item: Item):
        if buyer.money < item.price:
            raise ValueError("Недостаточно средств")
        buyer.money -= item.price
        seller.money += item.price
        buyer.inventory.append(item)
        pass