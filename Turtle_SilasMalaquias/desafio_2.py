from turtle import *

def drawPlanet(satarSize, starColour):
    color(starColour)
    pendown()
    speed(11)
    begin_fill()
    for i in range(360):
        right(1)
        forward(satarSize)
    end_fill()
    penup()
    

bgcolor("MidnightBlue")


drawPlanet(2, "Green")

hideturtle()
done()