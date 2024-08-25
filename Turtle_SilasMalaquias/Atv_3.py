from turtle import *
from random import *


def drawStar(satarSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(satarSize)
    end_fill()
    penup()
    

bgcolor("MidnightBlue")

drawStar(50, "Red")
forward(100)
drawStar(30, "White")
left(120)
forward(150)
drawStar(70, "Green")

hideturtle()
done()
