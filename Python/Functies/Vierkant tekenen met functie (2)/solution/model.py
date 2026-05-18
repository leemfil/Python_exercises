import turtle


def teken_vierkant(lengte):
    pen = turtle.Turtle()

    for _ in range(4):
        pen.forward(lengte)
        pen.left(90)


zijde = int(input("Geef de lengte van de zijde: "))
teken_vierkant(zijde)

turtle.exitonclick()
