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


def drawPetal(t: Turtle, angle: int) -> None:
    """
    Draw one petal with certain angle and t as a
    Turtle Object.
    """
    n = 10

    drawPolyline(bob, n, 5, angle/n)
    lt(t, 180-angle)
    drawPolyline(bob, n, 5, angle/n)
    lt(t, 180)


def drawFlower(t: Turtle, p: int) -> None:
    """
    Draw a flower with p argument as an number of petals and t as
    a Turtle Object.
    """
    for l in range(p):
        drawPetal(bob, 360/p)
    wait_for_user()


drawFlower(bob, 11)