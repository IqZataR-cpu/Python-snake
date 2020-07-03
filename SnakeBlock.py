class SnakeBlock:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def equalsTo(self, obj):
        return self.x == obj.x and self.y == obj.y