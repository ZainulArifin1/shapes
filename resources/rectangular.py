"""Rectangular."""

from math import pi
import sys
import os

class Rectangle:
    def __init__(self, width, height, fill="red", stroke="black"):
        self._width = width
        self._height = height
        self._fill = fill
        self._stroke = stroke

    def calculate_area(self):
        return self._width * self._height

    @property
    def height(self):
        return self._height

    def width(self):
        return self._width


    def __len__(self):
        return (2 * self._height) + (2 * self._width)

    def __call__(self):
        return "I am a depressed rectangle"


def main():

    rectangle = Rectangle(width=10,  height= 11, fill="orange", stroke="red")
    print(f"area = {rectangle.calculate_area()}")
    print(f"width = {rectangle.width()}")
    print(f"Circumference = {rectangle.__len__()}")
    print(f"Description = {rectangle.__call__()}")
    return 0 #os.EX_OK for linux, 0 for windows


if __name__ == '__main__':
    sys.exit(main())