import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
   return 12 * math.cos(k) - 5 * math.cos(2* k) - 2 * math.cos(3 * k) - math.cos(4 + k)

speed(10000000000)
bgcolor("pink")
#begin_fill()

for i in range(1000):
    color("red")
    #pendown()
    goto(hearta(i) * 20, heartb(i) * 20)
#end_fill()
goto(0,0)
done()
