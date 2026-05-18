import turtle


def teken_vierkant():
    pen = turtle.Turtle()

    for _ in range(4):
        pen.forward(100)
        pen.left(90)


teken_vierkant()
turtle.exitonclick()
