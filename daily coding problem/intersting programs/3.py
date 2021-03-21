import turtle
amy=turtle.Turtle()
amy.color("cyan")
amy.speed(0)
def draw_square(length):
    amy.forward(length)
    amy.right(90)
    amy.width(2)
    for side in range(4):
        amy.forward(50)
        amy.right(90)



amy.penup()
amy.back(20)
amy.pendown()

for sqr in range(80):
    draw_square(5)
    amy.forward(5)
    amy.left(5)
amy.hideturtle()
