#ex29-turtle-designs
#make a design using squares

from turtle import *

speed(0)
def drawsquares(num):
    for i in range (4):
        forward(num)
        right(90)

for i in range(360):
    drawsquares(100)
    right(1)
