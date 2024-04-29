from turtle import *
shape("turtle")

for i in range(5):
    forward(100)
    right(72)
    
left(90)
penup()
forward(100)
pendown()
right(90)

for i in range(6):
    forward(100)
    left(60)
    
left(180)
penup()
forward(200)
pendown()

speed(11)
for i in range(360):
    forward(1)
    right(1)
    
done()