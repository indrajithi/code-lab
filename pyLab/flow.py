import math
from swampy.TurtleWorld import *
from polygon import *
#from TurtleWorld import *
world = TurtleWorld()
t = Turtle()
print t

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t,length)
        lt(t,angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n , length, angle)

def arc(t, r, angle):
    arc_len = 2* math.pi * r * angle / 360
    n = int(arc_len /3) + 1
    stp_len = arc_len / n
    stp_ang = float(angle) / n
    polyline(t, n , stp_len, stp_ang)

def pettel(t, r, angle):
    arc_len = r * angle * math.pi / 180
    n = int(arc_len /3) + 1
    stp_len = arc_len / n
    stp_ang =   float(angle) / n
    polyline(t, n , stp_len, stp_ang)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180 - angle)
def circle(t, r):
    arc(t, r, 360)


t.delay = 0.01
#circle(t, 50)
#arc(t, 100 , 180 )

def flower(t, n, r, ang):
   # ang = 360.0 / n
    for i in range(n):
        petal(t, r, ang)
        lt(t, 360.0 / n)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

#move(bob, -100)
#flower(t, 7, 60.0, 60.0)
draw(t, 100,30 )
#move(bob, 100)
#flower(t, 10, 40.0, 80.0)

#move(bob, 100)
#flower(t,20 , 200.0, 20.0)

die(t)
wait_for_user()

