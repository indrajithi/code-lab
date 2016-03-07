from sys import argv
from swampy.TurtleWorld import *
import math
#prg, n, length = argv



def polyline(tur, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(tur,length)
        lt(tur, angle)

def polygon(tur, n, length):
    angle = 360.0 / n
    for i in range(n):
        polyline(tur, n, length)
        lt(tur)

def circle(tur, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3 ) + 1
    length = circumference / n
    polyline(tur, n, length)


#n, lenght, angle = map(int,raw_input("enter n length and angle :").split())
world = TurtleWorld()
tur1 = Turtle()
print tur1
tur1.delay = 0.1
r = int(raw_input("r = "))
#length = int(raw_input("length = "))
#angle = int(raw_input("angle = "))
#angle = 360.0 / n

circle(tur1, r)
#polyline(tur1, n, length)
#polygon(tur1, n , length)
raw_input()
