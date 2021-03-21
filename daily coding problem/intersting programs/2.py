import turtle

def spiral(sides,turn,color,width):
    t=turtle.Turtle()
    t.color(color)
    t.width(width)
    t.speed(0)
    for n in range(sides):
        t.forward(n)
        t.right(turn)
        t.penup()
        t.left(60)
        t.forward(10)
        t.right(60)
        t.pendown()
        t.hideturtle()
spiral(230,60,'cyan',5)
