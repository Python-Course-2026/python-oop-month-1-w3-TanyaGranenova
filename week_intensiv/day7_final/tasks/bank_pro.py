class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

class SavingsAccount(Account):
    """Сберегательный счет: нельзя снимать больше, чем есть (уже в родителе)"""
    pass

class BusinessAccount(Account):
    """
    Бизнес-счет:
    1. Комиссия за каждый перевод (transfer) — 5% от суммы.
    2. Позволяет уходить в минус до лимита -1000.
    """
    def withdraw(self, amount):
        if self._balance - amount >= -1000:
            self._balance -= amount
            return True
        return False

class BankPro:
    """
    ЗАДАЧА: Реализовать логику перевода между счетами.
    Метод transfer(from_acc, to_acc, amount):
    1. Если from_acc — BusinessAccount, сумма списания = amount + 5% комиссии.
    2. Если на from_acc недостаточно средств (с учетом его правил withdraw), вернуть "Ошибка".
    3. Если всё ок:
       - Списать деньги с from_acc.
       - Зачислить amount (без комиссии!) на to_acc.
       - Вернуть "Успех".
    """
    def transfer(self, from_acc, to_acc, amount):
        # ТВОЙ КОД ЗДЕСЬ
        if isinstance(from_acc, BusinessAccount):
            commission = amount * 0.05
            withdraw_amount = amount + commission
        else:
            withdraw_amount = amount
        if not from_acc.withdraw(withdraw_amount):
            return "Ошибка"
        to_acc._balance += amount
        return "Успех"
        pass