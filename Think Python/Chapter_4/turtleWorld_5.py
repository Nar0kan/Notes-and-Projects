from swampy.TurtleWorld import *
from math import pi

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def polyline(t: TurtleWorld, n: int, length: int, angle: int) -> None:
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t: TurtleWorld, n: int, length: int) -> None:
    angle = 360.0 / n
    polyline(t, n, length, angle)


def circle(t: TurtleWorld, r: int) -> None:
    arc(t, r, 360)


def arc(t: TurtleWorld, r: int, angle: int) -> None:
    fraction = 2*pi*r*angle/360
    n = int(fraction/3) + 1

    step_length = fraction/n
    step_angle = float(angle)/n
    polyline(t, n, step_length, step_angle)



arc(bob, 20, 320)
wait_for_user()