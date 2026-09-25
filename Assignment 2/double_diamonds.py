"""this program is generate two diamonds using turtle graphics"""

import turtle

# predfine the diamond side lenght - fill the code
# predfine the fill color - fill the code

# setup the turrtle window

turtle.setup(500,600)

# steup the turtle
turtle.showturtle()
turtle.fillcolor("blue")
turtle.speed(1)

LEFT_SIDE_LENGTH = 100
RIGHT_SIDE_LENGTH = 100

# draw the lest-side diamond first using the predfined SIDE_LENGTH - fill the code
turtle.begin_fill()
# fill the code to draw the left-side diamond
turtle.left(135)
turtle.forward(LEFT_SIDE_LENGTH)
turtle.left(90)
turtle.forward(LEFT_SIDE_LENGTH)
turtle.left(90)
turtle.forward(LEFT_SIDE_LENGTH)
turtle.left(90)
turtle.forward(LEFT_SIDE_LENGTH)
turtle.end_fill()

# draw the right-side diamond next - fill the code

turtle.begin_fill()
turtle.left(0)
turtle.forward(RIGHT_SIDE_LENGTH)
turtle.right(90)
turtle.forward(RIGHT_SIDE_LENGTH)
turtle.right(90)
turtle.forward(RIGHT_SIDE_LENGTH)
turtle.right(90)
turtle.forward(RIGHT_SIDE_LENGTH)
turtle.end_fill()

turtle.done()