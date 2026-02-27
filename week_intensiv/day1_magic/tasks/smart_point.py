class SmartPoint:
    """ЗАДАЧА: Реализовать __str__ (Точка(x, y)) и __repr__ (SmartPoint(x=x, y=y))"""
    def __init__(self, x, y): self.x, self.y = x, y
    def __str__(self): pass
    def __repr__(self): pass
class SmartPoint:
    """ЗАДАЧА: Реализовать str (Точка(x, y)) и repr (SmartPoint(x=x, y=y))"""
    def __init__(self, x, y): self.x, self.y = x, y
    def __str__(self):
        return  'Точка({}, {})'.format(self.x, self.y)

    pass
    def __repr__(self):
        return 'SmartPoint(x={}, y={})'.format(self.x, self.y)

    pass