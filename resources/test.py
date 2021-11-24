import sys
import os
import turtle
from math import pi
import yaml

class Circle:
    def __init__(self, radius, fill='blue', stroke='black', at=(0,0)):
        self._radius = radius # private/protected
        self._fill = fill
        self._stroke = stroke
        self._at = at

    def calculate_area(self):
        """ Calculate the area of a circle """
        return int(pi * self._radius ** 2)

    @property
    def radius(self): # public access for _radius; read only
        return self._radius

    def __len__(self):
        return int(2 * pi * self._radius)

    def __call__(self):
        return 'I am a circle!'

    # def __str__(self):
      # return f"A {self._fill} circle of radius {self._radius}"

    def __str__(self):
        string = yaml.dump({
            'circle':{
                'radius':self._radius,
                'fill':self._fill,
                'stroke':self._stroke,
                'at':self._at
            }
        })
        return string

    # @classmethod
    # def from_yaml(cls, string):
    #     # create an instance
    #     # create a circle from a yAML string
    #     circle_dict = yaml.load(string, Loader=yaml.Loader)['circle']
    #     print(circle_dict)
    #     obj = cls(circle_dict['radius'],fill=circle_dict['fill'], stroke=circle_dict['stroke'], at=circle_dict['at'])
    #     return obj

class Quadrilateral:
    def __init__(self, height, width, fill='grey', stroke='purple'):
        self._height = height
        self._width = width
        self._fill = fill
        self._stroke = stroke

    def calculate_area(self):
        """ Calculate the area of a circle """
        return int(self._height * self._width)

class Canvas:
    def __init__(self, height, width, background='lightgrey'):
        self._height = height
        self._width = width
        self._background = background

class Text:
    def __init__(self, size=16, font='Helvetica', color='darkorange', at=(0,0)):
        """
        :param size: set a default size for text class
        :param font: set a default font for text class
        :param color: set a default color for text class
        """
        self._size = size
        self._font = font
        self._color = color

    def write(self, pen, *args, **kwargs):
        pen.up()
        pen.goto(self._at)
        pen.down()
        pen.write(self._text)
        pen.up()
        pass

def main():
    circle = Circle(5.0, fill='green', stroke='black')
    print(f'Area of the circle is {circle.calculate_area()}')
    print(f'Circumference of the circle is {len(circle)}')
    print(circle()) # return the call
    print(circle) # return the str

    my_dict = {
        'key' : {
            'inside_dict':[5,6,7,8]
        }
    }

    my_yaml = yaml.dump(my_dict)
    print(my_yaml)

    # yaml_circle = """\
    # circle:
    # at: !!python/tuple
    # - 0
    # - 0
    # fill: green
    # radius: 5.0
    # stroke: black"""
    # my_circle = Circle.from_yaml(yaml_circle)
    pen = turtle.Turtle()
    text = Text("written by turtle")
    print(text)
    text.write(pen, "Arial",30,"bold")
    turtle.done()

    return 0

if __name__ == '__main__':
    sys.exit(main())