import turtle

pen = turtle.Turtle()


def teken_vierkant(lengte):
    for _ in range(4):
        pen.forward(lengte)
        pen.left(90)


teken_vierkant(120)

turtle.exitonclick()
