from turtle import *

def drawHexagono():
    lados = 6
    angulo = 360 / lados
    pendown()
    begin_fill()
    for i in range(lados):
        forward(100)
        left(angulo)
        
    end_fill()
    penup()
    
color("WhiteSmoke")
bgcolor("MidnightBlue")


drawHexagono()
forward(200)
drawHexagono()
left(200)
forward(150)
drawHexagono()

hideturtle()

done()