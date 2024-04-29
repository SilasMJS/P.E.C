from turtle import *
shape("turtle")

speed(11)

for count in range(4):
    forward(100)
    right(90)

penup()
left(90)
forward(150)
pendown()

for count in range(8):
    forward(100)
    right(45)
    
penup()
left(90)
forward(100)
pendown()

for count in range(30):
    forward(5)
    penup()
    forward(5)
    pendown()
    
done()