from swampy.TurtleWorld import *
from math import floor


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01


def drawKochCurve(t, length) -> None:
    if length < 1: fd(t, floor(length*3))
    else:
        S = floor(length*3)
        fd(floor(S/3**length))


def koch(t: Turtle, length) -> None:
    drawKochCurve(t, length/3)
    lt(t, 60)
    drawKochCurve(t, length/3)
    rt(t, 120)
    drawKochCurve(t, length/3)
    lt(t, 60)
    drawKochCurve(t, length/3)


koch(bob, 120)