import turtle

def draw_shapes(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

    # caroline = turtle.Turtle()
    # caroline.color("blue")
    # caroline.circle(100)
    #
    # meep = turtle.Turtle()
    # meep.color("red")
    # meep.forward(100)
    # meep.left(120)
    # meep.forward(100)
    # meep.left(120)
    # meep.forward(100)

def draw_circle_of_squares():
    window = turtle.Screen()
    window.bgcolor("pink")

    douglass = turtle.Turtle()

    for i in range(1,37):
        draw_shapes(douglass)
        douglass.right(10)
        douglass.speed(5)

    window.exitonclick()


draw_circle_of_squares()
