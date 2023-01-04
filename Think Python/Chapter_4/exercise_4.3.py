from swampy.TurtleWorld import *
from math import pi


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1


def drawPolyline(t: Turtle, n: int, length: int, angle: int) -> None:
    """
    Draw a polyline with t parameter as a Turtle Object.
    n is the amount of line segments each with certain length.
    angle is specified between these lines.
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def drawTriangle(t: Turtle, n: int, length: int) -> None:
    """
    Draw a polygon with determined n lines, where
    each one has length and t as a Turtle Object.
    """
    angle = 360.0 / n

    for i in range(n):
        fd(t, length)
        lt(t, 180-angle/2)
        print(angle/2)
        fd(t, length)
        lt(t, 180)
        fd(t, length)
        rt(t, angle/4)
    
    wait_for_user()


drawTriangle(bob, 5, 100)