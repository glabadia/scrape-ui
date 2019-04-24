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

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
another = Point(10, 15)
print(point.default_size)
print(Point.default_size)
point.draw()
print(point)

print(point == another)
print(point < another)

print(point + another)
