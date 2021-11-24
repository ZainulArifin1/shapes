"""Shapes."""

from math import pi
import sys
import os


class Circle:
    def __init__(self, radius, fill="red", stroke="black"):
        self._radius = radius
        self._fill = fill
        self._stroke = stroke

    def calculate_area(self):
        return pi * self._radius ** 2

    @property
    def radius(self):
        return self._radius

    def __len__(self):
        return 2 * pi * self._radius

    def __call__(self):
        return "I am a depressed circle"


def main():

    circle = Circle(22, fill="orange", stroke="red")
    print(f"area = {circle.calculate_area()}")
    print(f"Radius = {circle.radius}")
    print(f"Circumference = {circle.__len__()}")
    print(f"Description = {circle.__call__()}")
    # circle2 = Circle(8.0)
    return 0 #os.EX_OK for linux, 0 for windows


if __name__ == '__main__':
    sys.exit(main())