from turtle import *
shape("turtle")

# Quadrado
# for i in range(4):
#     forward(100)
#     right(90)

# triangulo
# for i in range(3):
#     forward(100)
#     right(120)
    
# casa
# for i in range (4):
#     forward(100)
#     right(90)
    
# left(45)
# forward(70)
# right(90)
# forward(70)

for steps in range(100):
    for c in ('blue', 'red', 'green','purple','orange','black'):
        speed(11)
        color(c)
        pensize(3)
        forward(steps)
        right(30)

done()