import turtle

def initials():
    window = turtle.Screen()
    window.bgcolor("pink")

    a = turtle.Turtle()
    a.left(90)
    a.forward(250)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(250)
    a.left(180)
    a.forward(175)
    a.left(90)
    a.forward(100)

    n = turtle.Turtle()
    n.left(90)
    n.forward(250)
    n.right(90)
    n.forward(25)
    n.right(75)
    n.forward(250)

    window.exitonclick()

initials()
