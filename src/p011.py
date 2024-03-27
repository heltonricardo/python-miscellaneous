class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x!r}, y={self.y!r})"


point1 = Point(3, 4)

print("Using __str__:")
print(point1)
print(f"{point1}")
print(str(point1))
print(point1.__str__())
print()
print("Using __repr__:")
print(f"{point1!r}")
print(repr(point1))
print(point1.__repr__())
