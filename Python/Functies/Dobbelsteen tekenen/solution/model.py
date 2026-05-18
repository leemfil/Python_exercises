import turtle

pen = turtle.Turtle()

def ga_naar(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def teken_stip(x, y):
    ga_naar(x, y)
    pen.dot(20)


def teken_vierkant():
    ga_naar(-50, -50)

    for _ in range(4):
        pen.forward(100)
        pen.left(90)


teken_vierkant()
teken_stip(-25, 25)
teken_stip(25, 25)
teken_stip(0, 0)
teken_stip(-25, -25)
teken_stip(25, -25)

turtle.exitonclick()
