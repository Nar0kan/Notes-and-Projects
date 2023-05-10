from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def poligon(t: TurtleWorld, length: int, n: int) -> None:
    for i in range(n):
        fd(t, length)
        lt(t, 360/n)

poligon(bob, 200, 16)
wait_for_user()