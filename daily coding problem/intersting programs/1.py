import turtle
t=turtle.Turtle()
t.color("cyan")
for side in range(19):
    t.forward(10*side)
    t.right(300/3)
    t.hideturtle()
