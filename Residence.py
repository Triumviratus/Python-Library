#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------

import turtle

square = turtle.Turtle()
square.hideturtle()

rectangle = turtle.Turtle()
rectangle.hideturtle()

triangle = turtle.Turtle()
triangle.hideturtle()

def draw_rectangle(some_turtle, x, y, h_length, v_length):
    some_turtle.up()
    some_turtle.goto(x, y)
    some_turtle.down()
    for side in range(2):
        some_turtle.forward(h_length)
        some_turtle.right(90)
        some_turtle.forward(v_length)
        some_turtle.right(90)

# House Outline
draw_rectangle(square, -50, 50, 100, 100)

# Roof

triangle.up()
triangle.color("blue")
triangle.goto(-50, 50)
triangle.down()
triangle.begin_fill()
triangle.goto(0, 100)
triangle.goto(50, 50)
triangle.goto(-50, 50)
triangle.end_fill()

# Door
rectangle.color("purple")
rectangle.begin_fill()
draw_rectangle(rectangle, -10, -10, 20, 40)
rectangle.end_fill()

# Left Window
draw_rectangle(square, -30, 30, 20, 20)

# Right Window
draw_rectangle(square, 10, 30, 20, 20)
