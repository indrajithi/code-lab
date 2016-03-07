import math
from swampy.TurtleWorld import *
world = TurtleWorld()
tur1 = Turtle()
print tur1

def polyline(t, n, length, angle):
    """Draws N line segments.

    t: Turtle
    n: number of lines
    length: length of each segment
    angle: destance between each segment
    """

    for i in range(n):
        fd(t, length)
        lt(t, angle)

tur1.delay = 0
polyline(tur1, 5 , 10, 1)
raw_input(">>>>")
