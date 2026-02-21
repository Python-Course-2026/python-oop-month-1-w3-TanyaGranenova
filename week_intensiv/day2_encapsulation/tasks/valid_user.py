class ValidUser:
    """ЗАДАЧА: Сеттер пароля с проверкой длины >= 8 и наличия цифр"""
    def __init__(self, user, pwd): self.username, self._password = user, pwd
    @property
    def password(self): return "********"
    @password.setter
    def password(self, val): pass