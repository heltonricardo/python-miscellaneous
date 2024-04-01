def custom_repr(self):
    class_name = self.__class__.__name__
    class_dict = ', '.join(f"{k}={v}" for k, v in self.__dict__.items())
    return f'{class_name}({class_dict})'


def auto_repr(cls):
    cls.__repr__ = custom_repr
    return cls


@auto_repr
class Circle:
    def __init__(self, radius):
        self.radius = radius


@auto_repr
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


circle = Circle(5)
print(circle)

rectangle = Rectangle(3, 4)
print(rectangle)
