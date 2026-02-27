class ValidUser:
    """ЗАДАЧА: Сеттер пароля с проверкой длины >= 8 и наличия цифр"""
    def __init__(self, user, pwd): self.username, self._password = user, pwd
    @property
    def password(self): return "********"
    @password.setter
    def password(self, val): pass
class ValidUser:
    """ЗАДАЧА: Сеттер пароля с проверкой длины >= 8 и наличия цифр"""
    def __init__(self, user, pwd): self.username, self._password = user, pwd
    @property
    def password(self): return "********"
    @password.setter
    def password(self, val):
        if len(val) < 8:
            return "Пароль не должен меняться, если он короче 8 символов"
        else:
            self._password = val
        pass