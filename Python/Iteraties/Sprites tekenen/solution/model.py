import turtle


def teken_sprite(schildpad, aantal_beentjes, lengte):
    draaihoek = 360 / aantal_beentjes

    for _ in range(aantal_beentjes):
        schildpad.forward(lengte)
        schildpad.backward(lengte)
        schildpad.left(draaihoek)


venster = turtle.Screen()
venster.title("Sprites met 3, 5 en 8 beentjes")

pen = turtle.Turtle()
pen.speed(0)

pen.penup()
pen.goto(-200, 0)
pen.pendown()
teken_sprite(pen, 3, 50)

pen.penup()
pen.goto(0, 0)
pen.pendown()
teken_sprite(pen, 5, 50)

pen.penup()
pen.goto(200, 0)
pen.pendown()
teken_sprite(pen, 8, 50)

pen.hideturtle()
venster.exitonclick()
