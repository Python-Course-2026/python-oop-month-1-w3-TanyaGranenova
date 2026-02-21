class Wallet:
    """ЗАДАЧА: Сложение кошельков через __add__ (новый Wallet) и длина через __len__ (целый баланс)"""
    def __init__(self, name, balance): self.name, self.balance = name, balance
    def __add__(self, other): pass
    def __len__(self): pass