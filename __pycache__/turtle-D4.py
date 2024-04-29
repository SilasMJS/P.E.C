from turtle import *
shape("turtle")
speed(11)
lados = 6
angulo = 360 / lados

for i in range(lados):
    forward(100)
    left(angulo)
    
done()