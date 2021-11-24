import sys
import os
from math import pi
import yaml
import turtle

#turtle.tracer(False)


class Canvas(turtle.TurtleScreen):
    def __init__(self, width=10, height=10, bg='white'):
        self._width = width
        self._height = height
        self.bg = bg
        self.cv = turtle.getcanvas()
        super().__init__(self.cv)
        self.screensize(width, height, bg=bg)
        self._pen = turtle.Turtle()
    def draw_axes(self):
        # self._pen.speed(0)
        self._pen.up()
        self._pen.goto(0, self._height / 2)
        self._pen.down()
        self._pen.goto(0, -self._height / 2)
        self._pen.up()
        self._pen.goto(-self._width / 2, 0)
        self._pen.down()
        self._pen.goto(self._width / 2, 0)
        self._pen.up()
        self._pen.goto(-self._width / 2, -self._height / 2)
    def draw_grid(self, colour='#00cc00', hstep=50, vstep=50):
        # self._pen.speed(0)
        original_pen_colour = self._pen.pencolor()
        self._pen.color(colour)
        # vertical grids
        self._pen.up()
        for hpos in range(-500, 500 + hstep, hstep):
            self._pen.goto(hpos, 350)
            self._pen.down()
            self._pen.goto(hpos, -350)
            self._pen.up()
        # horizontal grids
        for vpos in range(-350, 350 + vstep, vstep):
            self._pen.goto(-500, vpos)
            self._pen.down()
            self._pen.goto(500, vpos)
            self._pen.up()
        # reset
        self._pen.pencolor(original_pen_colour)

    def write(self, text, *args, **kwargs):
        text.write(self._pen, *args, **kwargs)

    def draw(self, shape):
        """Draw the given shape"""
        shape.draw(self._pen)

class Text:
    def __init__(self, font="Arial", size=20, color="black", at=(0, 0), text=""):
        self.font = font
        self.size = size
        self.color = color
        self._at = at
        self.text = text

    def write(self, pen, *args, **kwargs):
        pen.up()
        pen.goto(self._at)
        pen.down()
        pen.write(self.text, *args, **kwargs)
        pen.up()


class Circle:
    def __init__(self, radius, fill='red', stroke='black', at=(0, 0)):
        self._radius = radius  # Private/protected
        self._fill = fill
        self._stroke = stroke
        self._at = at

    @property
    def radius(self):  # public access for radius READ ONLY
        return self._radius

    @property
    def are(self):
        return self.calculate_area()

    @property  # decorator
    def diameter(self):
        return self._radius * 2

    def calculate_area(self):
        """
        Calculare the area
        :return:
        """
        return pi * self._radius ** 2

    def __len__(self):
        return int(2 * pi * self._radius)  # using the private value

    def __call__(self):
        return "I am a happy circle c:"

    def __str__(self):
        string = {
            'circle': {
                'radius': self.radius,
                'fill': self._fill,
                'stroke': self._stroke,
                'at': self._at
            }
        }
        string = yaml.dump(string)
        return string

    def draw(self, pen):
        """Draw a circle"""
        if pen.isdown():
            pen.up()
        pen.goto(*self._at)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self._stroke)
        pen.fillcolor(self._fill)
        pen.circle(self._radius)
        pen.end_fill()
        pen.up()

    @classmethod
    def from_yaml(cls, string):
        """create circle from yaml str"""
        circle_dict = yaml.load(string, Loader=yaml.Loader)['circle']
        print(circle_dict)
        obj = cls(circle_dict['radius'], fill=circle_dict['fill'], stroke=circle_dict['stroke'], at=circle_dict['at'])
        return obj

    def __repr__(self):
        return f"Circle({self._radius}, {self._fill}, {self._stroke})"


class Stroke:
    def __init__(self, width=1, color="red"):
        self.width = width
        self.color = color


class Quadrilateral:
    def __init__(self, width, height, fill='red', stroke='#000000', at=(0, 0)):
        self._width = width
        self._height = height
        self._fill = fill
        self._stroke = stroke
        self._at = at

    def area(self):
        return self.width * self.height

    @property
    def vertices(self):
        return [
            (self.xpos - self._width / 2, self.ypos + self._height / 2),
            (self.xpos + self._width / 2, self.ypos + self._height / 2),
            (self.xpos + self._width / 2, self.ypos - self._height / 2),
            (self.xpos - self._width / 2, self.ypos - self._height / 2),
        ]
    @property
    def left(self):
        return self._at[0] - self._width / 2

    @property
    def top(self):
        return self._at[1] + self._height / 2

    @property
    def right(self):
        return self._at[0]

    @property
    def bottom(self):
        return self._at[1]

    def draw(self, pen, *args, **kwargs):
        pen.up()
        pen.goto(self.left, self.top)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self._stroke)
        pen.fillcolor(self._fill)
        pen.goto(self.left, self.bottom)
        pen.goto(self.right, self.bottom)
        pen.goto(self.right, self.top)
        pen.goto(self.left, self.top)
        pen.end_fill()
        pen.up()


def main():
    circle = Circle(50.0, fill='orange', stroke='red')
    print(f"Area = {circle.calculate_area()}")
    print(f"area = {circle.are}")
    print(f"circunference is {len(circle)}")
    print(circle._radius)
    print(circle())

    print(repr(circle))
    print(circle)
    yaml_circle = """\
circle:
  at: !!python/tuple
  - 0
  - 0
  fill: orange
  radius: 5.0
  stroke: red
    """
    my_circle = Circle.from_yaml(yaml_circle)
    pen = turtle.Turtle()
    text = Text("Written by turtle")
    # print(text)  # This will print an object definition
    text.write(pen, font=('Arial', 30, 'bold'))
    circle.draw(pen)

    canvas = Canvas(1000, 700)
    gquad = Quadrilateral(
        200, 300, fill='#009a44', stroke='white', at=(-100, 0)
    )
    wquad = Quadrilateral(
        200, 300, fill='white', stroke='#dddddd', at=(0, 0)
    )
    oquad = Quadrilateral(
        200, 300, fill='#ff8200', stroke='white', at=(100, 0)
    )
    text = Text('IRELAND', at=(0, -250))
    canvas.draw(gquad)
    canvas.draw(wquad)
    canvas.draw(oquad)
    canvas.write(text, align='center', font=('Arial', 60, 'bold'))

    turtle.done()



    return 0


if __name__ == "__main__":
    sys.exit(main())