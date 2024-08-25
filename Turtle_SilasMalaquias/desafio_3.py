from turtle import *
from random import *

starColours = ["#058396", "#0275A6", "#827E01"]

def moveToRandomLocation():
    penup()
    setpos(randint(-400, 400), randint(-400, 400))
    pendown()
    

def draw_circle(radius, color):
    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()


# def drawPlanet(satarSize,starColours):
#     color(starColours)
#     pendown()
#     speed(11)
#     begin_fill()
#     for i in range(360):
#         right(1)
#         forward(satarSize)
#     end_fill()
#     penup()

def drawStar(satarSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(satarSize)
    end_fill()
    penup()
    
def drawGalaxy(numberOfStars):
    starColours = ["#058396", "#0275A6", "#827E01"]
    moveToRandomLocation()
    
    for star in range(numberOfStars):
        penup()
        left( randint(-180, 180) )
        forward( randint(5,20) )
        pendown()
        
        drawStar(2, choice(starColours))

def drawConstellation(numberOfStars):
    moveToRandomLocation()
    
    for star in range(numberOfStars-1):
        drawStar(randint(7,15), "white")
        pendown()
        left(randint(-90,90))
        forward(randint(30,70))
        
    drawStar(randint(7,15), "White")

speed(11)

bgcolor("Black")

color("white")
for i in range(1, 20):
    penup()
    goto(0, -30 * i - 30)
    pendown()
    circle(30 * i + 30)

for star in range(50):
    moveToRandomLocation()
    drawStar(randint(5,25), "White")

for galaxy in range(5):
    drawGalaxy(50)
    
for constellation in range(5):
    drawConstellation(randint(4,7))
    
# for planet in range(3):
#     moveToRandomLocation()
#     drawPlanet(randint(1,2), choice(starColours))

planet_colors = ["blue", "green", "red", "purple", "orange", "brown", "beige"]
planet_positions = [(70, 0), (-120, 50), (100, -80), (-50, -120), (150, 150), (-200, 200), (200, -200)]
planet_sizes = [20, 15, 25, 10, 30, 20, 30]

for pos, size, color in zip(planet_positions, planet_sizes, planet_colors):
    penup()
    goto(pos)
    pendown()
    draw_circle(size, color)
    

hideturtle()
done()