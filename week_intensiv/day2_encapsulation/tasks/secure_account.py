class SecureAccount:
    """ЗАДАЧА: Приватный __balance, геттер @property и депозит с проверкой > 0"""
    def __init__(self, bal): self.__balance = bal
    @property
    def balance(self): pass
    def deposit(self, amt): pass
class SecureAccount:
    """ЗАДАЧА: Приватный __balance, геттер @property и депозит с проверкой > 0"""
    def __init__(self, bal): self.__balance = bal
    @property
    def balance(self):
        return self.__balance
        pass
    def deposit(self, amt):
        if amt <= 0:
            raise ValueError("Amount must be greater than 0")
        self.__balance += amt
        return self.__balance