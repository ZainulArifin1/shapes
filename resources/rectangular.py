"""Rectangular."""

from math import pi
import sys
import yaml
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

    def __str__(self):
        string = {
            "rectangle":{
                "width":self._width,
                "fill":self._fill,
                "stroke":self._stroke,
            }
        }
        return yaml.dump(string)

    def from_yaml(cls, string):
        rect_dict = yaml.load(string, Loader=yaml.Loader)["rectangle"]
        print(rect_dict)
        obj = cls(fill=rect_dict["fill"], stroke=rect_dict["stroke"], width=rect_dict["width"])
        return obj



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
    print("\n")
    print(f"{rectangle.__str__()}")

    my_dict = {
        'key':{
            'inside_dict': [5,6,7,8]
        }
    }

    my_yaml = yaml.dump(my_dict)
    print(my_yaml)
    print(my_dict)

    yaml_rect = """\
    rectangle:
  fill: orange
  stroke: red
  width: 10
    """

    my_circle = Rectangle.from_yaml(yaml_rect)

    return 0 #os.EX_OK for linux, 0 for windows




if __name__ == '__main__':
    sys.exit(main())