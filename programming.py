class Point:
    default_size = 14

    @classmethod  # decorators
    def zero(cls):
        print("Zero Values")
        return cls(0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.default_size)
print(Point.default_size)
point.draw()
print(point)
