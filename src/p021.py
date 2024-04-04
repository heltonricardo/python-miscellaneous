"""
Geometry Module

This module provides utility functions and classes for basic geometric operations.
"""

import math


def calculate_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in 2D space.

    Parameters:
    point1 (tuple): A tuple containing the (x, y) coordinates of the first point.
    point2 (tuple): A tuple containing the (x, y) coordinates of the second point.

    Returns:
    float: The Euclidean distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
    width (float): The width of the rectangle.
    height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle object with the given width and height.

        Parameters:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
        float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


class Circle:
    """
    A class representing a circle.

    Attributes:
    radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize the Circle object with the given radius.

        Parameters:
        radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
        float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
        float: The circumference of the circle.
        """
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    rectangle = Rectangle(5, 10)

    print("Rectangle:")
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())

    circle = Circle(7)

    print("\nCircle:")
    print("Area:", circle.area())
    print("Circumference:", circle.circumference())

    point1 = (0, 0)
    point2 = (3, 4)
    distance = calculate_distance(point1, point2)

    print("\nDistance between point1 and point2:", distance)
