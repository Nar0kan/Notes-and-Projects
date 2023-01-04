from swampy.TurtleWorld import *
from math import pi

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01


def drawPolyline(t: Turtle, n: int, length: int, angle: int) -> None:
    """
    Draw a polyline with t parameter as a Turtle Object.
    n is the amount of line segments each with certain length.
    angle is specified between these lines.
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def drawPolygon(t: Turtle, n: int, length: int) -> None:
    """
    Draw a polygon with determined n lines, where
    each one has length and t as a Turtle Object.
    """
    angle = 360.0 / n
    drawPolyline(t, n, length, angle)


def drawArc(t: Turtle, r: int, angle: int) -> None:
    """
    Draw an Arc with specified angle, r as radius and
    t as a Turtle Object.
    """
    fraction = 2*pi*r*angle/360
    n = int(fraction/3) + 1

    step_length = fraction/n
    step_angle = float(angle)/n
    drawPolyline(t, n, step_length, step_angle)


def drawCircle(t: Turtle, r: int) -> None:
    """
    Draw circle with specified t as the Turtle Object
    and r as a radius of the circle.
    """
    drawArc(t, r, 360)


drawCircle(bob, 20)
wait_for_user()