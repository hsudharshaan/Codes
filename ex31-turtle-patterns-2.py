#ex31-turtle-patterns-2
# make a back ground of different shapes as patterns

from turtle import *

width(10)
speed(7.5)

def triangle():
    pencolor("red")
    forward(60)
    right(120)
    pencolor("purple")
    forward(60)
    right(120)
    pencolor("blue")
    forward(60)
    right(120)
    pencolor("orange")
    forward(60)
    right(120)

def sqare():
    pencolor("red")
    forward(50)
    right(90)
    pencolor("yellow")
    forward(50)
    right(90)
    pencolor("purple")
    forward(50)
    right(90)
    pencolor("blue")
    forward(50)
    right(90)

tr