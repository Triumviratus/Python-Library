#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------

import turtle
import random

window = turtle.Screen()

def create(x, y):
    racer = turtle.Turtle()
    racer.up()
    racer.shape("turtle")
    racer.color(random.random(), random.random(), random.random())
    racer.goto(x, y)
    racer.down()
    racer.stamp()
    return racer

racer_01 = create(-200, 100)
racer_02 = create(-200, 0)
racer_03 = create(-200, -100)

for i in range(10):
    racer_01.forward(random.randint(1, 40))
    racer_01.dot()
    racer_02.forward(random.randint(1, 40))
    racer_03.dot()
    racer_03.forward(random.randint(1, 40))
    racer_03.dot()

if (racer_01.xcor() > racer_02.xcor()) and (racer_01.xcor() > racer_03.xcor()):
    print("\nTurtle Racer 01 Emerges Victorious\n")
    
elif ((racer_02.xcor() > racer_01.xcor()) and (racer_02.xcor() > racer_03.xcor())):
    print("\nTurtle Racer 02 Emerges Victorious\n")

elif ((racer_03.xcor() > racer_01.xcor()) and (racer_03.xcor() > racer_02.xcor())):
    print("\nTurtle Racer 03 Emerges Victorious\n")

else:
    print("\nTurtle Racer 02 Emerges Victorious\n")

window.exitonclick()
