from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def poligon(t: TurtleWorld, length: int, n: int) -> None:
    for i in range(n):
        fd(t, length)
        lt(t, 360/n)


def circle(t: TurtleWorld, r: int) -> None:
    from math import pi
    circumference = 2*pi*r
    poligon(bob, circumference/20, 20)
    lt(t, 90)
    fd(t, r)


circle(bob, 20)
wait_for_user()