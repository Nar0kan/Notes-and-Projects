from swampy.TurtleWorld import *


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01


def draw(t, length, n):
    if n == 0:
        return None
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

for i in range(6):
    draw(bob, 10, 3)
    lt(bob, 60)