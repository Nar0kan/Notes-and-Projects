from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(t: TurtleWorld, length: int) -> None:
    for i in range(4):
        fd(t, length)
        lt(t)

square(bob, 20)
wait_for_user()