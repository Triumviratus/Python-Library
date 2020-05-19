#-----------------------------------------------------------------------
# Ambrose Ryan Xavier
#-----------------------------------------------------------------------

import turtle
import random

border = turtle.Turtle()
border.hideturtle()

border.speed(0)
border.up()
border.goto(-300, 300)
border.down()
for side in range(4):
    border.forward(600)
    border.right(90)

candy = turtle.Turtle()
candy.color("orange")
candy.hideturtle()
candy.speed(0)

handle = turtle.Turtle()
handle.color("blue")
handle.width(5)
handle.hideturtle()
handle.speed(0)
handle.right(90)

def draw_candy():
    z = random.randint(10, 30)
    x = random.randrange(-300 + z, 300 - z)
    y = random.randrange(-300 + z*2, 300 - z*2)
    candy.up()
    candy.goto(x, y)
    candy.down()
    handle.up()
    handle.goto(x, y)
    handle.down()
    handle.forward(z*2)
    candy.begin_fill()
    candy.circle(z)
    candy.end_fill()

for i in range(100):
    draw_candy()
    print(str(i))

import turtle
import random

window = turtle.Screen()

square = turtle.Turtle()
square.speed(0)
square.hideturtle()
square.up()
square.goto(-200, 200)
square.down()

for i in range(4):
    square.forward(50)
    square.right(90)

square.up()
square.goto(-200, 200)
square.write("Change Color")

paintbrush = turtle.Turtle()
paintbrush.shape("circle")

def drawing_controls(x, y):
    if (-200 <= x <= -150) and (150 <= y <= 200):
        colorR = random.random()
        colorG = random.random()
        colorB = random.random()
        paintbrush.color(colorR, colorG, colorB)
        square.color(colorR, colorG, colorB)
        square.up()
        square.goto(-200, 200)
        square.down()

        for i in range(4):
            square.forward(50)
            square.right(90)

window.onclick(drawing_controls)
paintbrush.onrelease(paintbrush.goto)
