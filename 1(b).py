class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        raise TypeError("operand must be an instance of Point")

    def __str__(self):
        return f"({self.x},{self.y})"

point1 = Point(2, 3)
point2 = Point(4, 5)
result = point1 + point2
print(f"Sum of points: {result}")
